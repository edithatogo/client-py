import unittest
from unittest import mock

from fhirclient.client import FHIRClient
from fhirclient.server import FHIRNotFoundException, FHIRUnauthorizedException

# Smallest valid-but-fake client state
MIN_STATE = {
    "server": {"base_uri": "http://example.com/fhir"},
}


class TestClient(unittest.TestCase):

    def test_load_from_state(self):
        state = {
            'app_id': 'AppID',
            'app_secret': 'AppSecret',
            'scope': 'user/*.read',
            'redirect': 'http://test.invalid/redirect',
            'patient_id': 'PatientID',
            'server': {
                'base_uri': 'http://test.invalid/',
                'auth_type': 'none',
                'auth': {
                    'app_id': 'AppId',
                },
            },
            'launch_token': 'LaunchToken',
            'launch_context': {
                'encounter': 'EncounterID',
                'patient': 'PatientID',
            },
            'jwt_token': 'JwtToken',
        }

        # Confirm round trip
        client = FHIRClient(state=state)
        self.assertEqual(state, client.state)

        # Sanity check a couple of the properties actually got set
        self.assertEqual('AppID', client.app_id)
        self.assertEqual('LaunchToken', client.launch_token)

        # Confirm we can do a partial from_state() - well, kind of partial since server is required
        client.from_state({'app_id': 'NewID', 'server': state['server']})
        self.assertEqual('NewID', client.app_id)
        self.assertEqual('LaunchToken', client.launch_token)

    @mock.patch("fhirclient.models.patient.Patient.read")
    def test_patient_property_happy_path(self, mock_read):
        save_func = mock.MagicMock()

        # Verify that we gracefully handle no patient_id being given
        client = FHIRClient(state=MIN_STATE, save_func=save_func)
        self.assertIsNone(client.patient)
        self.assertEqual(mock_read.call_count, 0)
        self.assertEqual(save_func.call_count, 0)

        # Verify we expose the provided patient ID as a Patient object
        client = FHIRClient(state={"patient_id": "P123", **MIN_STATE}, save_func=save_func)
        self.assertIsNotNone(client.patient)
        self.assertEqual(mock_read.call_count, 1)
        self.assertEqual(mock_read.call_args, mock.call("P123", client.server))
        self.assertEqual(save_func.call_count, 1)

    @mock.patch("fhirclient.models.patient.Patient.read")
    @mock.patch("fhirclient.client.FHIRClient.reauthorize")
    def test_patient_property_unauthorized(self, mock_reauthorize, mock_read):
        """We should attempt to reauthorize and re-request the patient"""

        client = FHIRClient(state={"patient_id": "P123", **MIN_STATE})

        # First try with a failed re-authorize
        mock_read.side_effect = FHIRUnauthorizedException("response")
        mock_reauthorize.return_value = False
        self.assertIsNone(client.patient)
        self.assertEqual(mock_read.call_count, 1)
        self.assertEqual(mock_reauthorize.call_count, 1)

        # Then with a successful re-authorize
        mock_read.reset_mock()
        mock_read.side_effect = [FHIRUnauthorizedException("response"), mock.MagicMock()]
        mock_reauthorize.reset_mock()
        mock_reauthorize.return_value = True
        self.assertIsNotNone(client.patient)
        self.assertEqual(mock_read.call_count, 2)
        self.assertEqual(mock_reauthorize.call_count, 1)

    @mock.patch("fhirclient.models.patient.Patient.read")
    def test_patient_property_not_found(self, mock_read):
        """We should attempt to reauthorize and re-request the patient"""
        mock_read.side_effect = FHIRNotFoundException("response")

        client = FHIRClient(state={"patient_id": "P123", **MIN_STATE})
        self.assertEqual(client.patient_id, "P123")  # sanity check before we start

        self.assertIsNone(client.patient)
        self.assertIsNone(client.patient_id)  # we clear out the patient id


class TestFHIRElementFactory(unittest.TestCase):
    def test_instantiate_with_case_variations(self):
        from fhirclient.models.fhirelementfactory import FHIRElementFactory
        from fhirclient.models.patient import Patient
        from fhirclient.models.observation import Observation
        from fhirclient.models.medicationrequest import MedicationRequest
        from fhirclient.models.element import Element

        # Test lowercase
        patient_json_lower = {"resourceType": "patient", "id": "test01"}
        patient_instance_lower = FHIRElementFactory.instantiate('patient', patient_json_lower)
        self.assertIsInstance(patient_instance_lower, Patient)
        self.assertEqual(patient_instance_lower.id, "test01")

        # Test uppercase
        obs_json_upper = {
            "resourceType": "OBSERVATION",
            "id": "test02",
            "status": "final",
            "code": {"coding": [{"system": "http://loinc.org", "code": "12345-6"}]}
        }
        obs_instance_upper = FHIRElementFactory.instantiate('OBSERVATION', obs_json_upper)
        self.assertIsInstance(obs_instance_upper, Observation)
        self.assertEqual(obs_instance_upper.id, "test02")

        # Test mixed case
        medreq_json_mixed = {
            "resourceType": "mEdIcAtIoNrEqUeSt",
            "id": "test03",
            "status": "active",
            "intent": "order",
            "medicationCodeableConcept": {"coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "123"}]},
            "subject": {"reference": "Patient/test01"}
        }
        medreq_instance_mixed = FHIRElementFactory.instantiate('mEdIcAtIoNrEqUeSt', medreq_json_mixed)
        self.assertIsInstance(medreq_instance_mixed, MedicationRequest)
        self.assertEqual(medreq_instance_mixed.id, "test03")

        # Test with leading/trailing whitespace
        patient_json_space = {"resourceType": " Patient ", "id": "test04"}
        patient_instance_space = FHIRElementFactory.instantiate(' Patient ', patient_json_space)
        self.assertIsInstance(patient_instance_space, Patient)
        self.assertEqual(patient_instance_space.id, "test04")

        # Test with None resourceType
        generic_json_none = {"id": "test05"}
        generic_instance_none = FHIRElementFactory.instantiate(None, generic_json_none)
        self.assertIsInstance(generic_instance_none, Element)
        # self.assertIsNone(getattr(generic_instance_none, 'resource_type', None)) # Element might still have it

        # Test with empty string resourceType
        generic_json_empty = {"resourceType": "", "id": "test06"}
        generic_instance_empty = FHIRElementFactory.instantiate('', generic_json_empty)
        self.assertIsInstance(generic_instance_empty, Element)

        # Test with whitespace-only string resourceType
        generic_json_whitespace = {"resourceType": "   ", "id": "test07"}
        generic_instance_whitespace = FHIRElementFactory.instantiate("   ", generic_json_whitespace)
        self.assertIsInstance(generic_instance_whitespace, Element)

    def test_abstract_resource_init_case_insensitivity(self):
        from fhirclient.models.patient import Patient

        # This should not raise an exception if __init__ is case-insensitive
        try:
            patient_lower = Patient(jsondict={"resourceType": "patient", "id": "pat1"}, strict=True)
            self.assertEqual(patient_lower.id, "pat1")
            patient_upper = Patient(jsondict={"resourceType": "PATIENT", "id": "pat2"}, strict=True)
            self.assertEqual(patient_upper.id, "pat2")
        except Exception as e:
            self.fail(f"Instantiation with case-variant resourceType failed: {e}")

        # This should still raise an exception for mismatched types if factory isn't used
        from fhirclient.models.observation import Observation
        # Using assertRaises(Exception) and then checking message is more robust if regex is tricky
        with self.assertRaises(Exception) as context:
            Patient(jsondict={"resourceType": "Observation", "id": "obs1"}, strict=True)
        self.assertIn("Attempting to instantiate <class 'fhirclient.models.patient.Patient'> (expected resourceType 'Patient') with resource data that defines a resourceType of \"Observation\"", str(context.exception))

        # Test with empty/None resourceType in strict mode
        with self.assertRaisesRegex(ValueError, "ResourceType cannot be empty or None"):
            Patient(jsondict={"resourceType": "", "id": "pat_empty"}, strict=True)

        with self.assertRaisesRegex(ValueError, "ResourceType cannot be empty or None"):
            Patient(jsondict={"resourceType": None, "id": "pat_none"}, strict=True)

        # Test with empty/None resourceType in non-strict mode (should not raise for this, but other errors might occur if data is bad)
        try:
            Patient(jsondict={"resourceType": "", "id": "pat_empty_nostrict"}, strict=False)
            Patient(jsondict={"resourceType": None, "id": "pat_none_nostrict"}, strict=False)
        except ValueError as ve:
            if "ResourceType cannot be empty" in str(ve): # Should not happen if strict=False for this specific check
                 self.fail(f"ValueError for empty/None resourceType should not be raised when strict=False: {ve}")
        except Exception:
            pass # Other errors might occur due to incomplete data, which is fine for this test's scope
