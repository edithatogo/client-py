import unittest
import base64
import hashlib
try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch

from fhirclient.auth import FHIROAuth2Auth
from fhirclient.server import FHIRServer


class PKCETests(unittest.TestCase):

    def setUp(self):
        self.settings_public = {
            'app_id': 'public_client_id',
            'api_base': 'https://fhir.example.com/R4',
            'redirect_uri': 'http://localhost/callback',
            'authorize_uri': 'https://fhir.example.com/oauth/authorize',
            'token_uri': 'https://fhir.example.com/oauth/token',
        }
        self.auth_public = FHIROAuth2Auth(state={
            'app_id': self.settings_public['app_id'],
            'redirect_uri': self.settings_public['redirect_uri'],
            '_authorize_uri': self.settings_public['authorize_uri'],
            '_token_uri': self.settings_public['token_uri'],
            'aud': self.settings_public['api_base'],
            'app_secret': None, # Explicitly None for public client state
        })

        self.settings_confidential = {
            'app_id': 'confidential_client_id',
            'app_secret': 'super_secret',
            'api_base': 'https://fhir.example.com/R4',
            'redirect_uri': 'http://localhost/callback',
            'authorize_uri': 'https://fhir.example.com/oauth/authorize',
            'token_uri': 'https://fhir.example.com/oauth/token',
        }
        self.auth_confidential = FHIROAuth2Auth(state={
            'app_id': self.settings_confidential['app_id'],
            'app_secret': self.settings_confidential['app_secret'],
            'redirect_uri': self.settings_confidential['redirect_uri'],
            '_authorize_uri': self.settings_confidential['authorize_uri'],
            '_token_uri': self.settings_confidential['token_uri'],
            'aud': self.settings_confidential['api_base'],
        })

        # Mock FHIRServer instance needed by auth methods
        self.mock_server = MagicMock(spec=FHIRServer)
        self.mock_server.desired_scope = "patient/*.read"
        self.mock_server.launch_token = None
        # Mock the should_save_state method
        self.mock_server.should_save_state = MagicMock()

    @patch('fhirclient.auth.secrets.token_urlsafe')
    def test_pkce_params_for_public_client(self, mock_token_urlsafe):
        """Verify PKCE parameters are added for public clients."""
        mock_token_urlsafe.return_value = "a_mocked_code_verifier_string_that_is_definitely_not_empty_and_long_enough"
        auth_params = self.auth_public._authorize_params(self.mock_server)

        self.assertIsNotNone(self.auth_public.code_verifier)
        self.assertIn('code_challenge', auth_params)
        self.assertIn('code_challenge_method', auth_params)
        self.assertEqual(auth_params['code_challenge_method'], 'S256')

        # Verify the code_challenge is the S256 hash of the verifier
        hashed_verifier = hashlib.sha256(self.auth_public.code_verifier.encode('utf-8')).digest()
        expected_challenge = base64.urlsafe_b64encode(hashed_verifier).rstrip(b'=').decode('utf-8')
        self.assertEqual(auth_params['code_challenge'], expected_challenge)

        # Ensure should_save_state was called because code_verifier was generated
        self.mock_server.should_save_state.assert_called()

        # Now check token exchange params
        code_exchange_params = self.auth_public._code_exchange_params('mock_code')
        self.assertIn('code_verifier', code_exchange_params)
        self.assertEqual(code_exchange_params['code_verifier'], self.auth_public.code_verifier)

    def test_no_pkce_params_for_confidential_client(self):
        """Verify PKCE parameters are NOT added for confidential clients."""
        self.mock_server.should_save_state.reset_mock() # Reset mock for this test
        # Pre-set auth_state to prevent it from being generated and triggering should_save_state
        self.auth_confidential.auth_state = "pre_existing_state"

        auth_params = self.auth_confidential._authorize_params(self.mock_server)

        self.assertIsNone(self.auth_confidential.code_verifier)
        self.assertNotIn('code_challenge', auth_params)
        self.assertNotIn('code_challenge_method', auth_params)

        # Ensure should_save_state was NOT called for PKCE reasons
        self.mock_server.should_save_state.assert_not_called()

        # Now check token exchange params
        code_exchange_params = self.auth_confidential._code_exchange_params('mock_code')
        self.assertNotIn('code_verifier', code_exchange_params)

    def test_pkce_state_management(self):
        """Verify code_verifier is saved to and loaded from state."""
        # 1. Generate PKCE params (and code_verifier)
        self.auth_public._authorize_params(self.mock_server)
        original_verifier = self.auth_public.code_verifier
        self.assertIsNotNone(original_verifier)

        # 2. Get state and check verifier is in it
        state = self.auth_public.state
        self.assertEqual(state.get('code_verifier'), original_verifier)

        # 3. Create new auth instance from this state
        new_auth_public = FHIROAuth2Auth(state=state)
        self.assertEqual(new_auth_public.code_verifier, original_verifier)

    @patch('fhirclient.auth.secrets.token_urlsafe')
    def test_pkce_code_verifier_cleared_and_reset(self, mock_token_urlsafe):
        """Verify code_verifier is cleared after token exchange and on reset."""
        mock_token_urlsafe.return_value = "another_mocked_verifier_for_this_test_case_to_use_effectively"
        # Setup: Generate code_verifier
        self.auth_public._authorize_params(self.mock_server)
        self.assertIsNotNone(self.auth_public.code_verifier)
        self.assertEqual(self.auth_public.code_verifier, "another_mocked_verifier_for_this_test_case_to_use_effectively")

        # Mock the server's post_as_form method for _request_access_token
        with patch.object(self.mock_server, 'post_as_form') as mock_post:
            # Simulate a successful token response
            mock_post.return_value.json.return_value = {
                'access_token': 'mock_access_token',
                'expires_in': 3600,
                'token_type': 'Bearer'
            }

            # Perform token exchange
            exchange_params = self.auth_public._code_exchange_params('mock_auth_code')
            self.assertIn('code_verifier', exchange_params) # Verifier should be in params

            self.auth_public._request_access_token(self.mock_server, exchange_params)

            # Verifier should be cleared now
            self.assertIsNone(self.auth_public.code_verifier)

        # Test reset
        self.auth_public._authorize_params(self.mock_server) # Generate again
        self.assertIsNotNone(self.auth_public.code_verifier)
        self.auth_public.reset()
        self.assertIsNone(self.auth_public.code_verifier)


class CustomParamsTests(unittest.TestCase):
    def setUp(self):
        self.base_settings = {
            'app_id': 'test_app',
            'api_base': 'http://fhir.example.com/R4',
            'redirect_uri': 'http://localhost/callback',
            '_authorize_uri': 'http://fhir.example.com/authorize',
            '_token_uri': 'http://fhir.example.com/token',
            'aud': 'http://fhir.example.com/R4',
        }
        self.mock_server = MagicMock(spec=FHIRServer)
        self.mock_server.desired_scope = "patient/*.read"
        self.mock_server.launch_token = None
        self.mock_server.should_save_state = MagicMock()

    def test_custom_auth_params_added(self):
        custom_params = {'custom_one': 'value1', 'custom_two': 'value2'}
        auth = FHIROAuth2Auth(state={**self.base_settings, 'custom_auth_params': custom_params.copy()})

        authorize_url_params = auth._authorize_params(self.mock_server)

        self.assertIn('custom_one', authorize_url_params)
        self.assertEqual(authorize_url_params['custom_one'], 'value1')
        self.assertIn('custom_two', authorize_url_params)
        self.assertEqual(authorize_url_params['custom_two'], 'value2')
        self.assertIn('client_id', authorize_url_params) # Ensure standard params are still there

    def test_custom_auth_params_conflict_ignored(self):
        # 'client_id' is a standard param and should not be overridden
        custom_params = {'client_id': 'custom_client_id', 'custom_one': 'value1'}
        auth = FHIROAuth2Auth(state={**self.base_settings, 'custom_auth_params': custom_params.copy()})

        with patch.object(auth_logger, 'warning') as mock_warning:
            authorize_url_params = auth._authorize_params(self.mock_server)
            self.assertEqual(authorize_url_params['client_id'], 'test_app') # Standard one wins
            self.assertEqual(authorize_url_params['custom_one'], 'value1')
            mock_warning.assert_called_with("Custom auth param 'client_id' conflicts with a standard OAuth param and will be ignored.")

    def test_custom_token_params_added_to_code_exchange(self):
        custom_params = {'custom_token_param': 'token_val1'}
        auth = FHIROAuth2Auth(state={**self.base_settings, 'custom_token_params': custom_params.copy()})

        exchange_params = auth._code_exchange_params('mock_code')
        self.assertIn('custom_token_param', exchange_params)
        self.assertEqual(exchange_params['custom_token_param'], 'token_val1')
        self.assertIn('grant_type', exchange_params) # Standard param

    def test_custom_token_params_added_to_client_credentials(self):
        custom_params = {'custom_cc_param': 'cc_val'}
        auth = FHIROAuth2Auth(state={**self.base_settings, 'custom_token_params': custom_params.copy()})
        auth.jwt_token = None # Ensure not using JWT assertion path for this test

        token_req_params = auth._token_params(self.mock_server)
        self.assertIn('custom_cc_param', token_req_params)
        self.assertEqual(token_req_params['custom_cc_param'], 'cc_val')
        self.assertIn('grant_type', token_req_params)
        self.assertEqual(token_req_params['grant_type'], 'client_credentials')

    def test_custom_token_params_added_to_refresh_token(self):
        custom_params = {'custom_refresh_param': 'refresh_val'}
        auth = FHIROAuth2Auth(state={**self.base_settings, 'custom_token_params': custom_params.copy()})
        auth.refresh_token = 'mock_refresh_token'

        reauth_params = auth._reauthorize_params()
        self.assertIn('custom_refresh_param', reauth_params)
        self.assertEqual(reauth_params['custom_refresh_param'], 'refresh_val')
        self.assertIn('grant_type', reauth_params)
        self.assertEqual(reauth_params['grant_type'], 'refresh_token')

    def test_custom_token_params_conflict_ignored(self):
        # 'grant_type' is a standard param and should not be overridden
        custom_params = {'grant_type': 'custom_grant', 'custom_one': 'value1'}
        auth = FHIROAuth2Auth(state={**self.base_settings, 'custom_token_params': custom_params.copy()})
        auth.refresh_token = 'mock_refresh_token' # For _reauthorize_params path

        with patch.object(auth_logger, 'warning') as mock_warning:
            # Test with _code_exchange_params
            exchange_params = auth._code_exchange_params('mock_code')
            self.assertEqual(exchange_params['grant_type'], 'authorization_code')
            self.assertEqual(exchange_params['custom_one'], 'value1')
            mock_warning.assert_any_call("Custom token param 'grant_type' conflicts with a standard OAuth param for code exchange and will be ignored.")

            mock_warning.reset_mock()
            # Test with _token_params (client_credentials)
            token_req_params = auth._token_params(self.mock_server)
            self.assertEqual(token_req_params['grant_type'], 'client_credentials')
            self.assertEqual(token_req_params['custom_one'], 'value1') # Should still be there
            mock_warning.assert_any_call("Custom token param 'grant_type' conflicts with a standard OAuth param for client credentials and will be ignored.")

            mock_warning.reset_mock()
            # Test with _reauthorize_params
            reauth_params = auth._reauthorize_params()
            self.assertEqual(reauth_params['grant_type'], 'refresh_token')
            self.assertEqual(reauth_params['custom_one'], 'value1')
            mock_warning.assert_any_call("Custom token param 'grant_type' conflicts with a standard OAuth param for refresh token grant and will be ignored.")

    def test_state_persistence_with_custom_params(self):
        custom_auth = {'ca1': 'v1'}
        custom_token = {'ct1': 'v2'}
        auth = FHIROAuth2Auth(state={
            **self.base_settings,
            'custom_auth_params': custom_auth,
            'custom_token_params': custom_token
        })

        saved_state = auth.state
        self.assertEqual(saved_state['custom_auth_params'], custom_auth)
        self.assertEqual(saved_state['custom_token_params'], custom_token)

        new_auth = FHIROAuth2Auth(state=saved_state)
        self.assertEqual(new_auth.custom_auth_params, custom_auth)
        self.assertEqual(new_auth.custom_token_params, custom_token)

# Need to import logger from fhirclient.auth for mock_warning
from fhirclient import auth as fhir_auth_module
auth_logger = fhir_auth_module.logger

if __name__ == '__main__':
    unittest.main()
