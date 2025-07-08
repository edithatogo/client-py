# Roadmap

This document outlines the development roadmap for `fhirclient` (smart-on-fhir/client-py). It includes major initiatives to address existing issues, enhance functionality, and ensure the library remains up-to-date with FHIR standards.

## Q1 2025 (Current Focus)

*   **Critical Bug Fixes:**
    *   Address [#171](https://github.com/smart-on-fhir/client-py/issues/171): Fix package level imports causing `pip install` failures.
    *   Address [#126](https://github.com/smart-on-fhir/client-py/issues/126): Resolve deprecated implicit grant flow in `auth.py`.
    *   Address [#140](https://github.com/smart-on-fhir/client-py/issues/140): Fix `fhirsearch` for `_include` with renamed reference fields.
    *   Address [#124](https://github.com/smart-on-fhir/client-py/issues/124): Correctly parse incorrectly labeled DSTU 2 API responses.
*   **Project Infrastructure & DX (Developer Experience):**
    *   Implement CI Linting ([#155](https://github.com/smart-on-fhir/client-py/issues/155)) to improve code quality and consistency.
    *   Establish comprehensive project management and agent collaboration files (`todo.md`, `changelog.md`, `gemini.md`, `agents.md`, `session_logs.md`).
*   **Documentation - Phase 1:**
    *   Address [#101](https://github.com/smart-on-fhir/client-py/issues/101): Document usage with SMART Backend Services.
    *   Begin general improvements for [#153](https://github.com/smart-on-fhir/client-py/issues/153).

## Q2 2025

*   **FHIR R5 Support - Phase 1 & 2 (Initiative from [#161](https://github.com/smart-on-fhir/client-py/issues/161)):**
    *   Update model generation scripts (`generate_models.sh`, `fhir-parser`) for R5.
    *   Generate initial R5 models for common resources.
    *   Adapt client functionality (`FHIRClient`, `FHIRServer`) for R5.
    *   Develop R5-specific test suites.
*   **Enhanced Authentication ([#178](https://github.com/smart-on-fhir/client-py/issues/178)):**
    *   Allow custom parameters in authentication requests.
*   **Documentation - Phase 2:**
    *   Continue comprehensive review and updates based on [#153](https://github.com/smart-on-fhir/client-py/issues/153).
    *   Document new R5 features and authentication enhancements.

## Q3 2025

*   **FHIR R5 Support - Phase 3 (Completion):**
    *   Generate and validate all R5 models.
    *   Comprehensive testing of R5 functionalities.
    *   Update examples and demos for R5.
*   **Technical Debt Reduction:**
    *   Review and automate manual release processes (from `MAINTAINERS.md`).
    *   Investigate and update outdated dependencies.
*   **Further Issue Resolution:**
    *   Address remaining bugs and feature requests from `todo.md` based on priority.

## Q4 2025 & Beyond

*   **Advanced Features (Potential):**
    *   Explore asynchronous client operations.
    *   Consider architectural changes like Pydantic models ([#143](https://github.com/smart-on-fhir/client-py/issues/143)) if deemed beneficial after R5 stabilization.
*   **Ongoing Maintenance:**
    *   Regular updates for new FHIR versions and patch releases.
    *   Continuous improvement of documentation and tests.
    *   Community support and issue triage.

This roadmap is a living document and will be updated as priorities shift or new information becomes available. Feedback and contributions are welcome.
