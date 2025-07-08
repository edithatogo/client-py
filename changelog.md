# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project management files: `roadmap.md`, `changelog.md`, `todo.md`, `gemini.md`, `agents.md`, `session_logs.md`.

### Changed
- Maintainer instructions in `MAINTAINERS.md` updated to reflect the new location of `__version__`.

### Fixed
- Resolved potential `pip install` failures by moving `__version__` definition directly into `fhirclient/__init__.py` (Addresses #171).
- Corrected `FHIRSearch.include()` method in `fhir-parser-resources/fhirsearch.py` (and propagated to `fhirclient/models/fhirsearch.py`) to allow using search parameter names (not just direct attribute names) as the `reference_field`. This fixes issues with `_include` where the search parameter is renamed (Addresses #140).
- Improved robustness of resource parsing by making `resourceType` matching case-insensitive and tolerant of leading/trailing whitespace in `FHIRElementFactory` and `FHIRAbstractResource`. This helps handle variations from servers, including some older DSTU 2 systems (Addresses #124).

### Added
- Initial project management files: `roadmap.md`, `changelog.md`, `todo.md`, `gemini.md`, `agents.md`, `session_logs.md`.
- Ruff for linting and formatting, added to `dev` dependencies in `pyproject.toml`.
- CI workflow (`.github/workflows/ci.yaml`) updated to include a new job for linting (`ruff check .`) and format checking (`ruff format --check .`). (Addresses #155).
- Functionality to add custom parameters to OAuth2 authorization and token requests via `FHIRClient` settings: `custom_auth_params` and `custom_token_params` (Addresses #178).
- Documentation in `README.md` updated to include a section on "Using with SMART Backend Services" (client credentials, JWT client assertion) (Addresses #101).
- `FHIRClient` docstring updated to include `custom_auth_params` and `custom_token_params` settings.

### Security
- Implemented PKCE (Proof Key for Code Exchange) for the OAuth2 Authorization Code Flow to enhance security for public clients (those configured without a client secret). This addresses the underlying concern of issue #126. (Note: associated unit tests for public clients need follow-up).

### Removed
- (Work in progress for future releases based on `todo.md`)

---

*Older versions will be documented here as new releases are made.*
