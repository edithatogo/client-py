#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fhirclient.models.fhirsearch import FHIRSearch

if '__main__' == __name__:
    from fhirclient.models.patient import Patient
    print('1 '+FHIRSearch(Patient, {'name': 'Willis'}).construct())
    print('1 '+Patient.where({'name': 'Willis'}).construct())
    # print('1 '+Patient.where().name('Willis').construct())
    print('= Patient?name=Willis')
    print('')
    print('2 '+FHIRSearch(Patient, {'name': {'$exact': 'Willis'}}).construct())
    print('= Patient?name:exact=Willis')
    print('')
    print('3 '+FHIRSearch(Patient, {'name': {'$or': ['Willis', 'Wayne', 'Bruce']}}).construct())
    print('= Patient?name=Willis,Wayne,Bruce')
    print('')
    print('4 '+FHIRSearch(Patient, {'name': {'$and': ['Willis', {'$exact': 'Bruce'}]}}).construct())
    print('= Patient?name=Willis&name:exact=Bruce')
    print('')
    print('5 '+FHIRSearch(Patient, {'birthDate': {'$gt': '1950', '$lte': '1970'}}).construct())
    print('= Patient?birthDate=>1950&birthDate=<=1970')
    print('')
    print('6 '+FHIRSearch(Patient, {'subject.name': {'$exact': 'Willis'}}).construct())
    print('= Patient?subject.name:exact=Willis')
    print('')
    srch = FHIRSearch(Patient, {'subject': {'$type': 'Patient', 'name': 'Willis', 'birthDate': {'$gt': '1950', '$lte': '1970'}}})
    print('7 '+srch.construct())
    srch = Patient.where({'subject': {'$type': 'Patient', 'name': 'Willis', 'birthDate': {'$gt': '1950', '$lte': '1970'}}})
    print('7 '+srch.construct())
    print('= Patient?subject:Patient.name=Willis&subject:Patient.birthDate=>1950&subject:Patient.birthDate=<=1970')
    print('')
    print('8 '+FHIRSearch(Patient, {"name": {"$and": ["Willis", {"$exact": "Bruce"}]}, "birthDay": {"$and": [{"$lt": "1970", "$gte": "1950"}]}}).construct())
    print('= Patient?name=Willis&name:exact=Bruce&birthDay=>=1950&birthDay=<1970')
    print('')

    # Mock Observation class for testing _include with renamed search parameters
    class MockObservation(object):
        resource_type = "Observation"
        def __init__(self, jsondict=None, strict=True): pass
        def elementProperties(self): return [('subject', 'subject', 'FHIRReference', False, None, False)]

    # Mock Patient class for revinclude test
    class MockPatient(object):
        resource_type = "Patient"
        def __init__(self, jsondict=None, strict=True): pass
        def elementProperties(self): return []


    print('9: Test _include with a search parameter name that differs from attribute name')
    # User intends to include "Patient" resources linked via Observation's "patient" search parameter
    # (which maps to the 'subject' attribute in a real Observation model).
    # The FHIRSearch.include method should now accept 'patient' as reference_field.
    print('  ' + FHIRSearch(MockObservation).include('patient').construct())
    print('= Observation?_include=Observation:patient')
    print('')

    print('10: Test _revinclude with a search parameter name')
    # User intends to search for Observations and reverse include resources that refer to it via 'referring-obs'
    # (assuming 'referring-obs' is a search parameter on some other resource type that points to Observation).
    # For this test, we use MockPatient as the "other resource type" and 'referring-obs' as its search param.
    # This means: search Observations, also include Patients that have 'referring-obs=Observation/xyz'.
    # The call would be: FHIRSearch(MockObservation).include('referring-obs', MockPatient, reverse=True)
    # resulting in _revinclude=MockPatient:referring-obs
    # However, the current include() logic for reference_model in revinclude might be:
    # reference_model is the type being included.
    # FHIRSearch(ResourceTypeBeingSearched).include(search_param_on_IncludedType, IncludedType, reverse=True)
    # The test below is structured based on how _revinclude usually works:
    # "Search for X, include Ys that refer to X via Y.searchparam"
    # -> FHIRSearch(X).include('searchparam_on_Y', Y, reverse=True)
    # -> X?_revinclude=Y:searchparam_on_Y
    print('  ' + FHIRSearch(MockObservation).include('based-on', MockPatient, reverse=True).construct())
    print('= Observation?_revinclude=Patient:based-on') # 'based-on' is a param on Patient
    print('')

    print('11: Test _include with iteration (include specific target types)')
    # _include=Observation:patient:Patient or _include=Observation:patient:Group
    # The current .include() method does not support the :TargetType syntax directly.
    # It only takes one reference_field. This is advanced usage.
    # For now, we test that it handles the basic format correctly.
    # The FHIR spec allows _include=SourceType:SearchParam[:TargetType]
    # Our code currently produces SourceType:SearchParam.
    # This test just re-confirms basic _include for clarity.
    print('  ' + FHIRSearch(MockObservation).include('subject').construct()) # 'subject' is a direct attribute
    print('= Observation?_include=Observation:subject')
