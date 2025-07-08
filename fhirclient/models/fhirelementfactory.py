#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2024-07-22.
#  2024, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".
        
        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        cleaned_resource_type = resource_type.strip() if resource_type else None
        if not cleaned_resource_type:
            from . import element # Fallback for empty or None resourceType
            return element.Element(jsondict)

        resource_type_lower = cleaned_resource_type.lower()

        if "account" == resource_type_lower:
            from . import account
            return account.Account(jsondict)
        if "accountcoverage" == resource_type_lower:
            from . import account
            return account.AccountCoverage(jsondict)
        if "accountguarantor" == resource_type_lower:
            from . import account
            return account.AccountGuarantor(jsondict)
        if "activitydefinition" == resource_type_lower:
            from . import activitydefinition
            return activitydefinition.ActivityDefinition(jsondict)
        if "activitydefinitiondynamicvalue" == resource_type_lower:
            from . import activitydefinition
            return activitydefinition.ActivityDefinitionDynamicValue(jsondict)
        if "activitydefinitionparticipant" == resource_type_lower:
            from . import activitydefinition
            return activitydefinition.ActivityDefinitionParticipant(jsondict)
        if "address" == resource_type_lower:
            from . import address
            return address.Address(jsondict)
        if "adverseevent" == resource_type_lower:
            from . import adverseevent
            return adverseevent.AdverseEvent(jsondict)
        if "adverseeventsuspectentity" == resource_type_lower:
            from . import adverseevent
            return adverseevent.AdverseEventSuspectEntity(jsondict)
        if "adverseeventsuspectentitycausality" == resource_type_lower:
            from . import adverseevent
            return adverseevent.AdverseEventSuspectEntityCausality(jsondict)
        if "age" == resource_type_lower:
            from . import age
            return age.Age(jsondict)
        if "allergyintolerance" == resource_type_lower:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict)
        if "allergyintolerancereaction" == resource_type_lower:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntoleranceReaction(jsondict)
        if "annotation" == resource_type_lower:
            from . import annotation
            return annotation.Annotation(jsondict)
        if "appointment" == resource_type_lower:
            from . import appointment
            return appointment.Appointment(jsondict)
        if "appointmentparticipant" == resource_type_lower:
            from . import appointment
            return appointment.AppointmentParticipant(jsondict)
        if "appointmentresponse" == resource_type_lower:
            from . import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict)
        if "attachment" == resource_type_lower:
            from . import attachment
            return attachment.Attachment(jsondict)
        if "auditevent" == resource_type_lower:
            from . import auditevent
            return auditevent.AuditEvent(jsondict)
        if "auditeventagent" == resource_type_lower:
            from . import auditevent
            return auditevent.AuditEventAgent(jsondict)
        if "auditeventagentnetwork" == resource_type_lower:
            from . import auditevent
            return auditevent.AuditEventAgentNetwork(jsondict)
        if "auditevententity" == resource_type_lower:
            from . import auditevent
            return auditevent.AuditEventEntity(jsondict)
        if "auditevententitydetail" == resource_type_lower:
            from . import auditevent
            return auditevent.AuditEventEntityDetail(jsondict)
        if "auditeventsource" == resource_type_lower:
            from . import auditevent
            return auditevent.AuditEventSource(jsondict)
        if "backboneelement" == resource_type_lower:
            from . import backboneelement
            return backboneelement.BackboneElement(jsondict)
        if "basic" == resource_type_lower:
            from . import basic
            return basic.Basic(jsondict)
        if "binary" == resource_type_lower:
            from . import binary
            return binary.Binary(jsondict)
        if "biologicallyderivedproduct" == resource_type_lower:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProduct(jsondict)
        if "biologicallyderivedproductcollection" == resource_type_lower:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductCollection(jsondict)
        if "biologicallyderivedproductmanipulation" == resource_type_lower:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductManipulation(jsondict)
        if "biologicallyderivedproductprocessing" == resource_type_lower:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductProcessing(jsondict)
        if "biologicallyderivedproductstorage" == resource_type_lower:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductStorage(jsondict)
        if "bodystructure" == resource_type_lower:
            from . import bodystructure
            return bodystructure.BodyStructure(jsondict)
        if "bundle" == resource_type_lower:
            from . import bundle
            return bundle.Bundle(jsondict)
        if "bundleentry" == resource_type_lower:
            from . import bundle
            return bundle.BundleEntry(jsondict)
        if "bundleentryrequest" == resource_type_lower:
            from . import bundle
            return bundle.BundleEntryRequest(jsondict)
        if "bundleentryresponse" == resource_type_lower:
            from . import bundle
            return bundle.BundleEntryResponse(jsondict)
        if "bundleentrysearch" == resource_type_lower:
            from . import bundle
            return bundle.BundleEntrySearch(jsondict)
        if "bundlelink" == resource_type_lower:
            from . import bundle
            return bundle.BundleLink(jsondict)
        if "capabilitystatement" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatement(jsondict)
        if "capabilitystatementdocument" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementDocument(jsondict)
        if "capabilitystatementimplementation" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementImplementation(jsondict)
        if "capabilitystatementmessaging" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessaging(jsondict)
        if "capabilitystatementmessagingendpoint" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingEndpoint(jsondict)
        if "capabilitystatementmessagingsupportedmessage" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingSupportedMessage(jsondict)
        if "capabilitystatementrest" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRest(jsondict)
        if "capabilitystatementrestinteraction" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestInteraction(jsondict)
        if "capabilitystatementrestresource" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResource(jsondict)
        if "capabilitystatementrestresourceinteraction" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceInteraction(jsondict)
        if "capabilitystatementrestresourceoperation" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceOperation(jsondict)
        if "capabilitystatementrestresourcesearchparam" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceSearchParam(jsondict)
        if "capabilitystatementrestsecurity" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestSecurity(jsondict)
        if "capabilitystatementsoftware" == resource_type_lower:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementSoftware(jsondict)
        if "careplan" == resource_type_lower:
            from . import careplan
            return careplan.CarePlan(jsondict)
        if "careplanactivity" == resource_type_lower:
            from . import careplan
            return careplan.CarePlanActivity(jsondict)
        if "careplanactivitydetail" == resource_type_lower:
            from . import careplan
            return careplan.CarePlanActivityDetail(jsondict)
        if "careteam" == resource_type_lower:
            from . import careteam
            return careteam.CareTeam(jsondict)
        if "careteamparticipant" == resource_type_lower:
            from . import careteam
            return careteam.CareTeamParticipant(jsondict)
        if "catalogentry" == resource_type_lower:
            from . import catalogentry
            return catalogentry.CatalogEntry(jsondict)
        if "catalogentryrelatedentry" == resource_type_lower:
            from . import catalogentry
            return catalogentry.CatalogEntryRelatedEntry(jsondict)
        if "chargeitem" == resource_type_lower:
            from . import chargeitem
            return chargeitem.ChargeItem(jsondict)
        if "chargeitemdefinition" == resource_type_lower:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinition(jsondict)
        if "chargeitemdefinitionapplicability" == resource_type_lower:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionApplicability(jsondict)
        if "chargeitemdefinitionpropertygroup" == resource_type_lower:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionPropertyGroup(jsondict)
        if "chargeitemdefinitionpropertygrouppricecomponent" == resource_type_lower:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionPropertyGroupPriceComponent(jsondict)
        if "chargeitemperformer" == resource_type_lower:
            from . import chargeitem
            return chargeitem.ChargeItemPerformer(jsondict)
        if "claim" == resource_type_lower:
            from . import claim
            return claim.Claim(jsondict)
        if "claimaccident" == resource_type_lower:
            from . import claim
            return claim.ClaimAccident(jsondict)
        if "claimcareteam" == resource_type_lower:
            from . import claim
            return claim.ClaimCareTeam(jsondict)
        if "claimdiagnosis" == resource_type_lower:
            from . import claim
            return claim.ClaimDiagnosis(jsondict)
        if "claiminsurance" == resource_type_lower:
            from . import claim
            return claim.ClaimInsurance(jsondict)
        if "claimitem" == resource_type_lower:
            from . import claim
            return claim.ClaimItem(jsondict)
        if "claimitemdetail" == resource_type_lower:
            from . import claim
            return claim.ClaimItemDetail(jsondict)
        if "claimitemdetailsubdetail" == resource_type_lower:
            from . import claim
            return claim.ClaimItemDetailSubDetail(jsondict)
        if "claimpayee" == resource_type_lower:
            from . import claim
            return claim.ClaimPayee(jsondict)
        if "claimprocedure" == resource_type_lower:
            from . import claim
            return claim.ClaimProcedure(jsondict)
        if "claimrelated" == resource_type_lower:
            from . import claim
            return claim.ClaimRelated(jsondict)
        if "claimresponse" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "claimresponseadditem" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItem(jsondict)
        if "claimresponseadditemdetail" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetail(jsondict)
        if "claimresponseadditemdetailsubdetail" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetailSubDetail(jsondict)
        if "claimresponseerror" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseError(jsondict)
        if "claimresponseinsurance" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseInsurance(jsondict)
        if "claimresponseitem" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseItem(jsondict)
        if "claimresponseitemadjudication" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseItemAdjudication(jsondict)
        if "claimresponseitemdetail" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetail(jsondict)
        if "claimresponseitemdetailsubdetail" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict)
        if "claimresponsepayment" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponsePayment(jsondict)
        if "claimresponseprocessnote" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseProcessNote(jsondict)
        if "claimresponsetotal" == resource_type_lower:
            from . import claimresponse
            return claimresponse.ClaimResponseTotal(jsondict)
        if "claimsupportinginfo" == resource_type_lower:
            from . import claim
            return claim.ClaimSupportingInfo(jsondict)
        if "clinicalimpression" == resource_type_lower:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict)
        if "clinicalimpressionfinding" == resource_type_lower:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionFinding(jsondict)
        if "clinicalimpressioninvestigation" == resource_type_lower:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionInvestigation(jsondict)
        if "codesystem" == resource_type_lower:
            from . import codesystem
            return codesystem.CodeSystem(jsondict)
        if "codesystemconcept" == resource_type_lower:
            from . import codesystem
            return codesystem.CodeSystemConcept(jsondict)
        if "codesystemconceptdesignation" == resource_type_lower:
            from . import codesystem
            return codesystem.CodeSystemConceptDesignation(jsondict)
        if "codesystemconceptproperty" == resource_type_lower:
            from . import codesystem
            return codesystem.CodeSystemConceptProperty(jsondict)
        if "codesystemfilter" == resource_type_lower:
            from . import codesystem
            return codesystem.CodeSystemFilter(jsondict)
        if "codesystemproperty" == resource_type_lower:
            from . import codesystem
            return codesystem.CodeSystemProperty(jsondict)
        if "codeableconcept" == resource_type_lower:
            from . import codeableconcept
            return codeableconcept.CodeableConcept(jsondict)
        if "coding" == resource_type_lower:
            from . import coding
            return coding.Coding(jsondict)
        if "communication" == resource_type_lower:
            from . import communication
            return communication.Communication(jsondict)
        if "communicationpayload" == resource_type_lower:
            from . import communication
            return communication.CommunicationPayload(jsondict)
        if "communicationrequest" == resource_type_lower:
            from . import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict)
        if "communicationrequestpayload" == resource_type_lower:
            from . import communicationrequest
            return communicationrequest.CommunicationRequestPayload(jsondict)
        if "compartmentdefinition" == resource_type_lower:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinition(jsondict)
        if "compartmentdefinitionresource" == resource_type_lower:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinitionResource(jsondict)
        if "composition" == resource_type_lower:
            from . import composition
            return composition.Composition(jsondict)
        if "compositionattester" == resource_type_lower:
            from . import composition
            return composition.CompositionAttester(jsondict)
        if "compositionevent" == resource_type_lower:
            from . import composition
            return composition.CompositionEvent(jsondict)
        if "compositionrelatesto" == resource_type_lower:
            from . import composition
            return composition.CompositionRelatesTo(jsondict)
        if "compositionsection" == resource_type_lower:
            from . import composition
            return composition.CompositionSection(jsondict)
        if "conceptmap" == resource_type_lower:
            from . import conceptmap
            return conceptmap.ConceptMap(jsondict)
        if "conceptmapgroup" == resource_type_lower:
            from . import conceptmap
            return conceptmap.ConceptMapGroup(jsondict)
        if "conceptmapgroupelement" == resource_type_lower:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElement(jsondict)
        if "conceptmapgroupelementtarget" == resource_type_lower:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElementTarget(jsondict)
        if "conceptmapgroupelementtargetdependson" == resource_type_lower:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElementTargetDependsOn(jsondict)
        if "conceptmapgroupunmapped" == resource_type_lower:
            from . import conceptmap
            return conceptmap.ConceptMapGroupUnmapped(jsondict)
        if "condition" == resource_type_lower:
            from . import condition
            return condition.Condition(jsondict)
        if "conditionevidence" == resource_type_lower:
            from . import condition
            return condition.ConditionEvidence(jsondict)
        if "conditionstage" == resource_type_lower:
            from . import condition
            return condition.ConditionStage(jsondict)
        if "consent" == resource_type_lower:
            from . import consent
            return consent.Consent(jsondict)
        if "consentpolicy" == resource_type_lower:
            from . import consent
            return consent.ConsentPolicy(jsondict)
        if "consentprovision" == resource_type_lower:
            from . import consent
            return consent.ConsentProvision(jsondict)
        if "consentprovisionactor" == resource_type_lower:
            from . import consent
            return consent.ConsentProvisionActor(jsondict)
        if "consentprovisiondata" == resource_type_lower:
            from . import consent
            return consent.ConsentProvisionData(jsondict)
        if "consentverification" == resource_type_lower:
            from . import consent
            return consent.ConsentVerification(jsondict)
        if "contactdetail" == resource_type_lower:
            from . import contactdetail
            return contactdetail.ContactDetail(jsondict)
        if "contactpoint" == resource_type_lower:
            from . import contactpoint
            return contactpoint.ContactPoint(jsondict)
        if "contract" == resource_type_lower:
            from . import contract
            return contract.Contract(jsondict)
        if "contractcontentdefinition" == resource_type_lower:
            from . import contract
            return contract.ContractContentDefinition(jsondict)
        if "contractfriendly" == resource_type_lower:
            from . import contract
            return contract.ContractFriendly(jsondict)
        if "contractlegal" == resource_type_lower:
            from . import contract
            return contract.ContractLegal(jsondict)
        if "contractrule" == resource_type_lower:
            from . import contract
            return contract.ContractRule(jsondict)
        if "contractsigner" == resource_type_lower:
            from . import contract
            return contract.ContractSigner(jsondict)
        if "contractterm" == resource_type_lower:
            from . import contract
            return contract.ContractTerm(jsondict)
        if "contracttermaction" == resource_type_lower:
            from . import contract
            return contract.ContractTermAction(jsondict)
        if "contracttermactionsubject" == resource_type_lower:
            from . import contract
            return contract.ContractTermActionSubject(jsondict)
        if "contracttermasset" == resource_type_lower:
            from . import contract
            return contract.ContractTermAsset(jsondict)
        if "contracttermassetcontext" == resource_type_lower:
            from . import contract
            return contract.ContractTermAssetContext(jsondict)
        if "contracttermassetvalueditem" == resource_type_lower:
            from . import contract
            return contract.ContractTermAssetValuedItem(jsondict)
        if "contracttermoffer" == resource_type_lower:
            from . import contract
            return contract.ContractTermOffer(jsondict)
        if "contracttermofferanswer" == resource_type_lower:
            from . import contract
            return contract.ContractTermOfferAnswer(jsondict)
        if "contracttermofferparty" == resource_type_lower:
            from . import contract
            return contract.ContractTermOfferParty(jsondict)
        if "contracttermsecuritylabel" == resource_type_lower:
            from . import contract
            return contract.ContractTermSecurityLabel(jsondict)
        if "contributor" == resource_type_lower:
            from . import contributor
            return contributor.Contributor(jsondict)
        if "count" == resource_type_lower:
            from . import count
            return count.Count(jsondict)
        if "coverage" == resource_type_lower:
            from . import coverage
            return coverage.Coverage(jsondict)
        if "coverageclass" == resource_type_lower:
            from . import coverage
            return coverage.CoverageClass(jsondict)
        if "coveragecosttobeneficiary" == resource_type_lower:
            from . import coverage
            return coverage.CoverageCostToBeneficiary(jsondict)
        if "coveragecosttobeneficiaryexception" == resource_type_lower:
            from . import coverage
            return coverage.CoverageCostToBeneficiaryException(jsondict)
        if "coverageeligibilityrequest" == resource_type_lower:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequest(jsondict)
        if "coverageeligibilityrequestinsurance" == resource_type_lower:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestInsurance(jsondict)
        if "coverageeligibilityrequestitem" == resource_type_lower:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestItem(jsondict)
        if "coverageeligibilityrequestitemdiagnosis" == resource_type_lower:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis(jsondict)
        if "coverageeligibilityrequestsupportinginfo" == resource_type_lower:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo(jsondict)
        if "coverageeligibilityresponse" == resource_type_lower:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponse(jsondict)
        if "coverageeligibilityresponseerror" == resource_type_lower:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseError(jsondict)
        if "coverageeligibilityresponseinsurance" == resource_type_lower:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsurance(jsondict)
        if "coverageeligibilityresponseinsuranceitem" == resource_type_lower:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem(jsondict)
        if "coverageeligibilityresponseinsuranceitembenefit" == resource_type_lower:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit(jsondict)
        if "datarequirement" == resource_type_lower:
            from . import datarequirement
            return datarequirement.DataRequirement(jsondict)
        if "datarequirementcodefilter" == resource_type_lower:
            from . import datarequirement
            return datarequirement.DataRequirementCodeFilter(jsondict)
        if "datarequirementdatefilter" == resource_type_lower:
            from . import datarequirement
            return datarequirement.DataRequirementDateFilter(jsondict)
        if "datarequirementsort" == resource_type_lower:
            from . import datarequirement
            return datarequirement.DataRequirementSort(jsondict)
        if "detectedissue" == resource_type_lower:
            from . import detectedissue
            return detectedissue.DetectedIssue(jsondict)
        if "detectedissueevidence" == resource_type_lower:
            from . import detectedissue
            return detectedissue.DetectedIssueEvidence(jsondict)
        if "detectedissuemitigation" == resource_type_lower:
            from . import detectedissue
            return detectedissue.DetectedIssueMitigation(jsondict)
        if "device" == resource_type_lower:
            from . import device
            return device.Device(jsondict)
        if "devicedefinition" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinition(jsondict)
        if "devicedefinitioncapability" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionCapability(jsondict)
        if "devicedefinitiondevicename" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionDeviceName(jsondict)
        if "devicedefinitionmaterial" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionMaterial(jsondict)
        if "devicedefinitionproperty" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionProperty(jsondict)
        if "devicedefinitionspecialization" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionSpecialization(jsondict)
        if "devicedefinitionudideviceidentifier" == resource_type_lower:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionUdiDeviceIdentifier(jsondict)
        if "devicedevicename" == resource_type_lower:
            from . import device
            return device.DeviceDeviceName(jsondict)
        if "devicemetric" == resource_type_lower:
            from . import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "devicemetriccalibration" == resource_type_lower:
            from . import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict)
        if "deviceproperty" == resource_type_lower:
            from . import device
            return device.DeviceProperty(jsondict)
        if "devicerequest" == resource_type_lower:
            from . import devicerequest
            return devicerequest.DeviceRequest(jsondict)
        if "devicerequestparameter" == resource_type_lower:
            from . import devicerequest
            return devicerequest.DeviceRequestParameter(jsondict)
        if "devicespecialization" == resource_type_lower:
            from . import device
            return device.DeviceSpecialization(jsondict)
        if "deviceudicarrier" == resource_type_lower:
            from . import device
            return device.DeviceUdiCarrier(jsondict)
        if "deviceusestatement" == resource_type_lower:
            from . import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "deviceversion" == resource_type_lower:
            from . import device
            return device.DeviceVersion(jsondict)
        if "diagnosticreport" == resource_type_lower:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "diagnosticreportmedia" == resource_type_lower:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportMedia(jsondict)
        if "distance" == resource_type_lower:
            from . import distance
            return distance.Distance(jsondict)
        if "documentmanifest" == resource_type_lower:
            from . import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "documentmanifestrelated" == resource_type_lower:
            from . import documentmanifest
            return documentmanifest.DocumentManifestRelated(jsondict)
        if "documentreference" == resource_type_lower:
            from . import documentreference
            return documentreference.DocumentReference(jsondict)
        if "documentreferencecontent" == resource_type_lower:
            from . import documentreference
            return documentreference.DocumentReferenceContent(jsondict)
        if "documentreferencecontext" == resource_type_lower:
            from . import documentreference
            return documentreference.DocumentReferenceContext(jsondict)
        if "documentreferencerelatesto" == resource_type_lower:
            from . import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "domainresource" == resource_type_lower:
            from . import domainresource
            return domainresource.DomainResource(jsondict)
        if "dosage" == resource_type_lower:
            from . import dosage
            return dosage.Dosage(jsondict)
        if "dosagedoseandrate" == resource_type_lower:
            from . import dosage
            return dosage.DosageDoseAndRate(jsondict)
        if "duration" == resource_type_lower:
            from . import duration
            return duration.Duration(jsondict)
        if "effectevidencesynthesis" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesis(jsondict)
        if "effectevidencesynthesiscertainty" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisCertainty(jsondict)
        if "effectevidencesynthesiscertaintycertaintysubcomponent" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisCertaintyCertaintySubcomponent(jsondict)
        if "effectevidencesynthesiseffectestimate" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimate(jsondict)
        if "effectevidencesynthesiseffectestimateprecisionestimate" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(jsondict)
        if "effectevidencesynthesisresultsbyexposure" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisResultsByExposure(jsondict)
        if "effectevidencesynthesissamplesize" == resource_type_lower:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisSampleSize(jsondict)
        if "element" == resource_type_lower:
            from . import element
            return element.Element(jsondict)
        if "elementdefinition" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinition(jsondict)
        if "elementdefinitionbase" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBase(jsondict)
        if "elementdefinitionbinding" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBinding(jsondict)
        if "elementdefinitionconstraint" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionConstraint(jsondict)
        if "elementdefinitionexample" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionExample(jsondict)
        if "elementdefinitionmapping" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionMapping(jsondict)
        if "elementdefinitionslicing" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicing(jsondict)
        if "elementdefinitionslicingdiscriminator" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicingDiscriminator(jsondict)
        if "elementdefinitiontype" == resource_type_lower:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionType(jsondict)
        if "encounter" == resource_type_lower:
            from . import encounter
            return encounter.Encounter(jsondict)
        if "encounterclasshistory" == resource_type_lower:
            from . import encounter
            return encounter.EncounterClassHistory(jsondict)
        if "encounterdiagnosis" == resource_type_lower:
            from . import encounter
            return encounter.EncounterDiagnosis(jsondict)
        if "encounterhospitalization" == resource_type_lower:
            from . import encounter
            return encounter.EncounterHospitalization(jsondict)
        if "encounterlocation" == resource_type_lower:
            from . import encounter
            return encounter.EncounterLocation(jsondict)
        if "encounterparticipant" == resource_type_lower:
            from . import encounter
            return encounter.EncounterParticipant(jsondict)
        if "encounterstatushistory" == resource_type_lower:
            from . import encounter
            return encounter.EncounterStatusHistory(jsondict)
        if "endpoint" == resource_type_lower:
            from . import endpoint
            return endpoint.Endpoint(jsondict)
        if "enrollmentrequest" == resource_type_lower:
            from . import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict)
        if "enrollmentresponse" == resource_type_lower:
            from . import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict)
        if "episodeofcare" == resource_type_lower:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict)
        if "episodeofcarediagnosis" == resource_type_lower:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareDiagnosis(jsondict)
        if "episodeofcarestatushistory" == resource_type_lower:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareStatusHistory(jsondict)
        if "eventdefinition" == resource_type_lower:
            from . import eventdefinition
            return eventdefinition.EventDefinition(jsondict)
        if "evidence" == resource_type_lower:
            from . import evidence
            return evidence.Evidence(jsondict)
        if "evidencevariable" == resource_type_lower:
            from . import evidencevariable
            return evidencevariable.EvidenceVariable(jsondict)
        if "evidencevariablecharacteristic" == resource_type_lower:
            from . import evidencevariable
            return evidencevariable.EvidenceVariableCharacteristic(jsondict)
        if "examplescenario" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenario(jsondict)
        if "examplescenarioactor" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioActor(jsondict)
        if "examplescenarioinstance" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstance(jsondict)
        if "examplescenarioinstancecontainedinstance" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstanceContainedInstance(jsondict)
        if "examplescenarioinstanceversion" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstanceVersion(jsondict)
        if "examplescenarioprocess" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcess(jsondict)
        if "examplescenarioprocessstep" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStep(jsondict)
        if "examplescenarioprocessstepalternative" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStepAlternative(jsondict)
        if "examplescenarioprocessstepoperation" == resource_type_lower:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStepOperation(jsondict)
        if "explanationofbenefit" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict)
        if "explanationofbenefitaccident" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAccident(jsondict)
        if "explanationofbenefitadditem" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItem(jsondict)
        if "explanationofbenefitadditemdetail" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetail(jsondict)
        if "explanationofbenefitadditemdetailsubdetail" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail(jsondict)
        if "explanationofbenefitbenefitbalance" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalance(jsondict)
        if "explanationofbenefitbenefitbalancefinancial" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial(jsondict)
        if "explanationofbenefitcareteam" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitCareTeam(jsondict)
        if "explanationofbenefitdiagnosis" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitDiagnosis(jsondict)
        if "explanationofbenefitinsurance" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitInsurance(jsondict)
        if "explanationofbenefititem" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItem(jsondict)
        if "explanationofbenefititemadjudication" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemAdjudication(jsondict)
        if "explanationofbenefititemdetail" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetail(jsondict)
        if "explanationofbenefititemdetailsubdetail" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail(jsondict)
        if "explanationofbenefitpayee" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayee(jsondict)
        if "explanationofbenefitpayment" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayment(jsondict)
        if "explanationofbenefitprocedure" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitProcedure(jsondict)
        if "explanationofbenefitprocessnote" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitProcessNote(jsondict)
        if "explanationofbenefitrelated" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitRelated(jsondict)
        if "explanationofbenefitsupportinginfo" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitSupportingInfo(jsondict)
        if "explanationofbenefittotal" == resource_type_lower:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitTotal(jsondict)
        if "expression" == resource_type_lower:
            from . import expression
            return expression.Expression(jsondict)
        if "extension" == resource_type_lower:
            from . import extension
            return extension.Extension(jsondict)
        if "familymemberhistory" == resource_type_lower:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict)
        if "familymemberhistorycondition" == resource_type_lower:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryCondition(jsondict)
        if "flag" == resource_type_lower:
            from . import flag
            return flag.Flag(jsondict)
        if "goal" == resource_type_lower:
            from . import goal
            return goal.Goal(jsondict)
        if "goaltarget" == resource_type_lower:
            from . import goal
            return goal.GoalTarget(jsondict)
        if "graphdefinition" == resource_type_lower:
            from . import graphdefinition
            return graphdefinition.GraphDefinition(jsondict)
        if "graphdefinitionlink" == resource_type_lower:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLink(jsondict)
        if "graphdefinitionlinktarget" == resource_type_lower:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLinkTarget(jsondict)
        if "graphdefinitionlinktargetcompartment" == resource_type_lower:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLinkTargetCompartment(jsondict)
        if "group" == resource_type_lower:
            from . import group
            return group.Group(jsondict)
        if "groupcharacteristic" == resource_type_lower:
            from . import group
            return group.GroupCharacteristic(jsondict)
        if "groupmember" == resource_type_lower:
            from . import group
            return group.GroupMember(jsondict)
        if "guidanceresponse" == resource_type_lower:
            from . import guidanceresponse
            return guidanceresponse.GuidanceResponse(jsondict)
        if "healthcareservice" == resource_type_lower:
            from . import healthcareservice
            return healthcareservice.HealthcareService(jsondict)
        if "healthcareserviceavailabletime" == resource_type_lower:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceAvailableTime(jsondict)
        if "healthcareserviceeligibility" == resource_type_lower:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceEligibility(jsondict)
        if "healthcareservicenotavailable" == resource_type_lower:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict)
        if "humanname" == resource_type_lower:
            from . import humanname
            return humanname.HumanName(jsondict)
        if "identifier" == resource_type_lower:
            from . import identifier
            return identifier.Identifier(jsondict)
        if "imagingstudy" == resource_type_lower:
            from . import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "imagingstudyseries" == resource_type_lower:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict)
        if "imagingstudyseriesinstance" == resource_type_lower:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict)
        if "imagingstudyseriesperformer" == resource_type_lower:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesPerformer(jsondict)
        if "immunization" == resource_type_lower:
            from . import immunization
            return immunization.Immunization(jsondict)
        if "immunizationeducation" == resource_type_lower:
            from . import immunization
            return immunization.ImmunizationEducation(jsondict)
        if "immunizationevaluation" == resource_type_lower:
            from . import immunizationevaluation
            return immunizationevaluation.ImmunizationEvaluation(jsondict)
        if "immunizationperformer" == resource_type_lower:
            from . import immunization
            return immunization.ImmunizationPerformer(jsondict)
        if "immunizationprotocolapplied" == resource_type_lower:
            from . import immunization
            return immunization.ImmunizationProtocolApplied(jsondict)
        if "immunizationreaction" == resource_type_lower:
            from . import immunization
            return immunization.ImmunizationReaction(jsondict)
        if "immunizationrecommendation" == resource_type_lower:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict)
        if "immunizationrecommendationrecommendation" == resource_type_lower:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendation(jsondict)
        if "immunizationrecommendationrecommendationdatecriterion" == resource_type_lower:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(jsondict)
        if "implementationguide" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuide(jsondict)
        if "implementationguidedefinition" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinition(jsondict)
        if "implementationguidedefinitiongrouping" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionGrouping(jsondict)
        if "implementationguidedefinitionpage" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionPage(jsondict)
        if "implementationguidedefinitionparameter" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionParameter(jsondict)
        if "implementationguidedefinitionresource" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionResource(jsondict)
        if "implementationguidedefinitiontemplate" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionTemplate(jsondict)
        if "implementationguidedependson" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideDependsOn(jsondict)
        if "implementationguideglobal" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideGlobal(jsondict)
        if "implementationguidemanifest" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifest(jsondict)
        if "implementationguidemanifestpage" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifestPage(jsondict)
        if "implementationguidemanifestresource" == resource_type_lower:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifestResource(jsondict)
        if "insuranceplan" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlan(jsondict)
        if "insuranceplancontact" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanContact(jsondict)
        if "insuranceplancoverage" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverage(jsondict)
        if "insuranceplancoveragebenefit" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverageBenefit(jsondict)
        if "insuranceplancoveragebenefitlimit" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverageBenefitLimit(jsondict)
        if "insuranceplanplan" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlan(jsondict)
        if "insuranceplanplangeneralcost" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanGeneralCost(jsondict)
        if "insuranceplanplanspecificcost" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCost(jsondict)
        if "insuranceplanplanspecificcostbenefit" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCostBenefit(jsondict)
        if "insuranceplanplanspecificcostbenefitcost" == resource_type_lower:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCostBenefitCost(jsondict)
        if "invoice" == resource_type_lower:
            from . import invoice
            return invoice.Invoice(jsondict)
        if "invoicelineitem" == resource_type_lower:
            from . import invoice
            return invoice.InvoiceLineItem(jsondict)
        if "invoicelineitempricecomponent" == resource_type_lower:
            from . import invoice
            return invoice.InvoiceLineItemPriceComponent(jsondict)
        if "invoiceparticipant" == resource_type_lower:
            from . import invoice
            return invoice.InvoiceParticipant(jsondict)
        if "library" == resource_type_lower:
            from . import library
            return library.Library(jsondict)
        if "linkage" == resource_type_lower:
            from . import linkage
            return linkage.Linkage(jsondict)
        if "linkageitem" == resource_type_lower:
            from . import linkage
            return linkage.LinkageItem(jsondict)
        if "list" == resource_type_lower:
            from . import list
            return list.List(jsondict)
        if "listentry" == resource_type_lower:
            from . import list
            return list.ListEntry(jsondict)
        if "location" == resource_type_lower:
            from . import location
            return location.Location(jsondict)
        if "locationhoursofoperation" == resource_type_lower:
            from . import location
            return location.LocationHoursOfOperation(jsondict)
        if "locationposition" == resource_type_lower:
            from . import location
            return location.LocationPosition(jsondict)
        if "marketingstatus" == resource_type_lower:
            from . import marketingstatus
            return marketingstatus.MarketingStatus(jsondict)
        if "measure" == resource_type_lower:
            from . import measure
            return measure.Measure(jsondict)
        if "measuregroup" == resource_type_lower:
            from . import measure
            return measure.MeasureGroup(jsondict)
        if "measuregrouppopulation" == resource_type_lower:
            from . import measure
            return measure.MeasureGroupPopulation(jsondict)
        if "measuregroupstratifier" == resource_type_lower:
            from . import measure
            return measure.MeasureGroupStratifier(jsondict)
        if "measuregroupstratifiercomponent" == resource_type_lower:
            from . import measure
            return measure.MeasureGroupStratifierComponent(jsondict)
        if "measurereport" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReport(jsondict)
        if "measurereportgroup" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReportGroup(jsondict)
        if "measurereportgrouppopulation" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReportGroupPopulation(jsondict)
        if "measurereportgroupstratifier" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifier(jsondict)
        if "measurereportgroupstratifierstratum" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratum(jsondict)
        if "measurereportgroupstratifierstratumcomponent" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratumComponent(jsondict)
        if "measurereportgroupstratifierstratumpopulation" == resource_type_lower:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratumPopulation(jsondict)
        if "measuresupplementaldata" == resource_type_lower:
            from . import measure
            return measure.MeasureSupplementalData(jsondict)
        if "media" == resource_type_lower:
            from . import media
            return media.Media(jsondict)
        if "medication" == resource_type_lower:
            from . import medication
            return medication.Medication(jsondict)
        if "medicationadministration" == resource_type_lower:
            from . import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict)
        if "medicationadministrationdosage" == resource_type_lower:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationDosage(jsondict)
        if "medicationadministrationperformer" == resource_type_lower:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationPerformer(jsondict)
        if "medicationbatch" == resource_type_lower:
            from . import medication
            return medication.MedicationBatch(jsondict)
        if "medicationdispense" == resource_type_lower:
            from . import medicationdispense
            return medicationdispense.MedicationDispense(jsondict)
        if "medicationdispenseperformer" == resource_type_lower:
            from . import medicationdispense
            return medicationdispense.MedicationDispensePerformer(jsondict)
        if "medicationdispensesubstitution" == resource_type_lower:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseSubstitution(jsondict)
        if "medicationingredient" == resource_type_lower:
            from . import medication
            return medication.MedicationIngredient(jsondict)
        if "medicationknowledge" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledge(jsondict)
        if "medicationknowledgeadministrationguidelines" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelines(jsondict)
        if "medicationknowledgeadministrationguidelinesdosage" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesDosage(jsondict)
        if "medicationknowledgeadministrationguidelinespatientcharacteristics" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(jsondict)
        if "medicationknowledgecost" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeCost(jsondict)
        if "medicationknowledgedrugcharacteristic" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeDrugCharacteristic(jsondict)
        if "medicationknowledgeingredient" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeIngredient(jsondict)
        if "medicationknowledgekinetics" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeKinetics(jsondict)
        if "medicationknowledgemedicineclassification" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMedicineClassification(jsondict)
        if "medicationknowledgemonitoringprogram" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMonitoringProgram(jsondict)
        if "medicationknowledgemonograph" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMonograph(jsondict)
        if "medicationknowledgepackaging" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgePackaging(jsondict)
        if "medicationknowledgeregulatory" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatory(jsondict)
        if "medicationknowledgeregulatorymaxdispense" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense(jsondict)
        if "medicationknowledgeregulatoryschedule" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatorySchedule(jsondict)
        if "medicationknowledgeregulatorysubstitution" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatorySubstitution(jsondict)
        if "medicationknowledgerelatedmedicationknowledge" == resource_type_lower:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge(jsondict)
        if "medicationrequest" == resource_type_lower:
            from . import medicationrequest
            return medicationrequest.MedicationRequest(jsondict)
        if "medicationrequestdispenserequest" == resource_type_lower:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequest(jsondict)
        if "medicationrequestdispenserequestinitialfill" == resource_type_lower:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequestInitialFill(jsondict)
        if "medicationrequestsubstitution" == resource_type_lower:
            from . import medicationrequest
            return medicationrequest.MedicationRequestSubstitution(jsondict)
        if "medicationstatement" == resource_type_lower:
            from . import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
        if "medicinalproduct" == resource_type_lower:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProduct(jsondict)
        if "medicinalproductauthorization" == resource_type_lower:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorization(jsondict)
        if "medicinalproductauthorizationjurisdictionalauthorization" == resource_type_lower:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorizationJurisdictionalAuthorization(jsondict)
        if "medicinalproductauthorizationprocedure" == resource_type_lower:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorizationProcedure(jsondict)
        if "medicinalproductcontraindication" == resource_type_lower:
            from . import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindication(jsondict)
        if "medicinalproductcontraindicationothertherapy" == resource_type_lower:
            from . import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindicationOtherTherapy(jsondict)
        if "medicinalproductindication" == resource_type_lower:
            from . import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndication(jsondict)
        if "medicinalproductindicationothertherapy" == resource_type_lower:
            from . import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndicationOtherTherapy(jsondict)
        if "medicinalproductingredient" == resource_type_lower:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredient(jsondict)
        if "medicinalproductingredientspecifiedsubstance" == resource_type_lower:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstance(jsondict)
        if "medicinalproductingredientspecifiedsubstancestrength" == resource_type_lower:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrength(jsondict)
        if "medicinalproductingredientspecifiedsubstancestrengthreferencestrength" == resource_type_lower:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(jsondict)
        if "medicinalproductingredientsubstance" == resource_type_lower:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSubstance(jsondict)
        if "medicinalproductinteraction" == resource_type_lower:
            from . import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteraction(jsondict)
        if "medicinalproductinteractioninteractant" == resource_type_lower:
            from . import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteractionInteractant(jsondict)
        if "medicinalproductmanufactured" == resource_type_lower:
            from . import medicinalproductmanufactured
            return medicinalproductmanufactured.MedicinalProductManufactured(jsondict)
        if "medicinalproductmanufacturingbusinessoperation" == resource_type_lower:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductManufacturingBusinessOperation(jsondict)
        if "medicinalproductname" == resource_type_lower:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductName(jsondict)
        if "medicinalproductnamecountrylanguage" == resource_type_lower:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductNameCountryLanguage(jsondict)
        if "medicinalproductnamenamepart" == resource_type_lower:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductNameNamePart(jsondict)
        if "medicinalproductpackaged" == resource_type_lower:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackaged(jsondict)
        if "medicinalproductpackagedbatchidentifier" == resource_type_lower:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackagedBatchIdentifier(jsondict)
        if "medicinalproductpackagedpackageitem" == resource_type_lower:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackagedPackageItem(jsondict)
        if "medicinalproductpharmaceutical" == resource_type_lower:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(jsondict)
        if "medicinalproductpharmaceuticalcharacteristics" == resource_type_lower:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalCharacteristics(jsondict)
        if "medicinalproductpharmaceuticalrouteofadministration" == resource_type_lower:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministration(jsondict)
        if "medicinalproductpharmaceuticalrouteofadministrationtargetspecies" == resource_type_lower:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(jsondict)
        if "medicinalproductpharmaceuticalrouteofadministrationtargetspecieswithdrawalperiod" == resource_type_lower:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(jsondict)
        if "medicinalproductspecialdesignation" == resource_type_lower:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductSpecialDesignation(jsondict)
        if "medicinalproductundesirableeffect" == resource_type_lower:
            from . import medicinalproductundesirableeffect
            return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(jsondict)
        if "messagedefinition" == resource_type_lower:
            from . import messagedefinition
            return messagedefinition.MessageDefinition(jsondict)
        if "messagedefinitionallowedresponse" == resource_type_lower:
            from . import messagedefinition
            return messagedefinition.MessageDefinitionAllowedResponse(jsondict)
        if "messagedefinitionfocus" == resource_type_lower:
            from . import messagedefinition
            return messagedefinition.MessageDefinitionFocus(jsondict)
        if "messageheader" == resource_type_lower:
            from . import messageheader
            return messageheader.MessageHeader(jsondict)
        if "messageheaderdestination" == resource_type_lower:
            from . import messageheader
            return messageheader.MessageHeaderDestination(jsondict)
        if "messageheaderresponse" == resource_type_lower:
            from . import messageheader
            return messageheader.MessageHeaderResponse(jsondict)
        if "messageheadersource" == resource_type_lower:
            from . import messageheader
            return messageheader.MessageHeaderSource(jsondict)
        if "meta" == resource_type_lower:
            from . import meta
            return meta.Meta(jsondict)
        if "metadataresource" == resource_type_lower:
            from . import metadataresource
            return metadataresource.MetadataResource(jsondict)
        if "molecularsequence" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequence(jsondict)
        if "molecularsequencequality" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceQuality(jsondict)
        if "molecularsequencequalityroc" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceQualityRoc(jsondict)
        if "molecularsequencereferenceseq" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceReferenceSeq(jsondict)
        if "molecularsequencerepository" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceRepository(jsondict)
        if "molecularsequencestructurevariant" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariant(jsondict)
        if "molecularsequencestructurevariantinner" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariantInner(jsondict)
        if "molecularsequencestructurevariantouter" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariantOuter(jsondict)
        if "molecularsequencevariant" == resource_type_lower:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceVariant(jsondict)
        if "money" == resource_type_lower:
            from . import money
            return money.Money(jsondict)
        if "namingsystem" == resource_type_lower:
            from . import namingsystem
            return namingsystem.NamingSystem(jsondict)
        if "namingsystemuniqueid" == resource_type_lower:
            from . import namingsystem
            return namingsystem.NamingSystemUniqueId(jsondict)
        if "narrative" == resource_type_lower:
            from . import narrative
            return narrative.Narrative(jsondict)
        if "nutritionorder" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrder(jsondict)
        if "nutritionorderenteralformula" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormula(jsondict)
        if "nutritionorderenteralformulaadministration" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormulaAdministration(jsondict)
        if "nutritionorderoraldiet" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDiet(jsondict)
        if "nutritionorderoraldietnutrient" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietNutrient(jsondict)
        if "nutritionorderoraldiettexture" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietTexture(jsondict)
        if "nutritionordersupplement" == resource_type_lower:
            from . import nutritionorder
            return nutritionorder.NutritionOrderSupplement(jsondict)
        if "observation" == resource_type_lower:
            from . import observation
            return observation.Observation(jsondict)
        if "observationcomponent" == resource_type_lower:
            from . import observation
            return observation.ObservationComponent(jsondict)
        if "observationdefinition" == resource_type_lower:
            from . import observationdefinition
            return observationdefinition.ObservationDefinition(jsondict)
        if "observationdefinitionqualifiedinterval" == resource_type_lower:
            from . import observationdefinition
            return observationdefinition.ObservationDefinitionQualifiedInterval(jsondict)
        if "observationdefinitionquantitativedetails" == resource_type_lower:
            from . import observationdefinition
            return observationdefinition.ObservationDefinitionQuantitativeDetails(jsondict)
        if "observationreferencerange" == resource_type_lower:
            from . import observation
            return observation.ObservationReferenceRange(jsondict)
        if "operationdefinition" == resource_type_lower:
            from . import operationdefinition
            return operationdefinition.OperationDefinition(jsondict)
        if "operationdefinitionoverload" == resource_type_lower:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionOverload(jsondict)
        if "operationdefinitionparameter" == resource_type_lower:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameter(jsondict)
        if "operationdefinitionparameterbinding" == resource_type_lower:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterBinding(jsondict)
        if "operationdefinitionparameterreferencedfrom" == resource_type_lower:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterReferencedFrom(jsondict)
        if "operationoutcome" == resource_type_lower:
            from . import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "operationoutcomeissue" == resource_type_lower:
            from . import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict)
        if "organization" == resource_type_lower:
            from . import organization
            return organization.Organization(jsondict)
        if "organizationaffiliation" == resource_type_lower:
            from . import organizationaffiliation
            return organizationaffiliation.OrganizationAffiliation(jsondict)
        if "organizationcontact" == resource_type_lower:
            from . import organization
            return organization.OrganizationContact(jsondict)
        if "parameterdefinition" == resource_type_lower:
            from . import parameterdefinition
            return parameterdefinition.ParameterDefinition(jsondict)
        if "parameters" == resource_type_lower:
            from . import parameters
            return parameters.Parameters(jsondict)
        if "parametersparameter" == resource_type_lower:
            from . import parameters
            return parameters.ParametersParameter(jsondict)
        if "patient" == resource_type_lower:
            from . import patient
            return patient.Patient(jsondict)
        if "patientcommunication" == resource_type_lower:
            from . import patient
            return patient.PatientCommunication(jsondict)
        if "patientcontact" == resource_type_lower:
            from . import patient
            return patient.PatientContact(jsondict)
        if "patientlink" == resource_type_lower:
            from . import patient
            return patient.PatientLink(jsondict)
        if "paymentnotice" == resource_type_lower:
            from . import paymentnotice
            return paymentnotice.PaymentNotice(jsondict)
        if "paymentreconciliation" == resource_type_lower:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict)
        if "paymentreconciliationdetail" == resource_type_lower:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationDetail(jsondict)
        if "paymentreconciliationprocessnote" == resource_type_lower:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationProcessNote(jsondict)
        if "period" == resource_type_lower:
            from . import period
            return period.Period(jsondict)
        if "person" == resource_type_lower:
            from . import person
            return person.Person(jsondict)
        if "personlink" == resource_type_lower:
            from . import person
            return person.PersonLink(jsondict)
        if "plandefinition" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinition(jsondict)
        if "plandefinitionaction" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionAction(jsondict)
        if "plandefinitionactioncondition" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionCondition(jsondict)
        if "plandefinitionactiondynamicvalue" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionDynamicValue(jsondict)
        if "plandefinitionactionparticipant" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionParticipant(jsondict)
        if "plandefinitionactionrelatedaction" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionRelatedAction(jsondict)
        if "plandefinitiongoal" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionGoal(jsondict)
        if "plandefinitiongoaltarget" == resource_type_lower:
            from . import plandefinition
            return plandefinition.PlanDefinitionGoalTarget(jsondict)
        if "population" == resource_type_lower:
            from . import population
            return population.Population(jsondict)
        if "practitioner" == resource_type_lower:
            from . import practitioner
            return practitioner.Practitioner(jsondict)
        if "practitionerqualification" == resource_type_lower:
            from . import practitioner
            return practitioner.PractitionerQualification(jsondict)
        if "practitionerrole" == resource_type_lower:
            from . import practitionerrole
            return practitionerrole.PractitionerRole(jsondict)
        if "practitionerroleavailabletime" == resource_type_lower:
            from . import practitionerrole
            return practitionerrole.PractitionerRoleAvailableTime(jsondict)
        if "practitionerrolenotavailable" == resource_type_lower:
            from . import practitionerrole
            return practitionerrole.PractitionerRoleNotAvailable(jsondict)
        if "procedure" == resource_type_lower:
            from . import procedure
            return procedure.Procedure(jsondict)
        if "procedurefocaldevice" == resource_type_lower:
            from . import procedure
            return procedure.ProcedureFocalDevice(jsondict)
        if "procedureperformer" == resource_type_lower:
            from . import procedure
            return procedure.ProcedurePerformer(jsondict)
        if "prodcharacteristic" == resource_type_lower:
            from . import prodcharacteristic
            return prodcharacteristic.ProdCharacteristic(jsondict)
        if "productshelflife" == resource_type_lower:
            from . import productshelflife
            return productshelflife.ProductShelfLife(jsondict)
        if "provenance" == resource_type_lower:
            from . import provenance
            return provenance.Provenance(jsondict)
        if "provenanceagent" == resource_type_lower:
            from . import provenance
            return provenance.ProvenanceAgent(jsondict)
        if "provenanceentity" == resource_type_lower:
            from . import provenance
            return provenance.ProvenanceEntity(jsondict)
        if "quantity" == resource_type_lower:
            from . import quantity
            return quantity.Quantity(jsondict)
        # Duplicated "Quantity" entry removed in manual edit. Original template might have this.
        if "questionnaire" == resource_type_lower:
            from . import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "questionnaireitem" == resource_type_lower:
            from . import questionnaire
            return questionnaire.QuestionnaireItem(jsondict)
        if "questionnaireitemansweroption" == resource_type_lower:
            from . import questionnaire
            return questionnaire.QuestionnaireItemAnswerOption(jsondict)
        if "questionnaireitemenablewhen" == resource_type_lower:
            from . import questionnaire
            return questionnaire.QuestionnaireItemEnableWhen(jsondict)
        if "questionnaireiteminitial" == resource_type_lower:
            from . import questionnaire
            return questionnaire.QuestionnaireItemInitial(jsondict)
        if "questionnaireresponse" == resource_type_lower:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponse(jsondict)
        if "questionnaireresponseitem" == resource_type_lower:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItem(jsondict)
        if "questionnaireresponseitemanswer" == resource_type_lower:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItemAnswer(jsondict)
        if "range" == resource_type_lower:
            from . import range
            return range.Range(jsondict)
        if "ratio" == resource_type_lower:
            from . import ratio
            return ratio.Ratio(jsondict)
        if "reference" == resource_type_lower:
            from . import reference
            return reference.Reference(jsondict)
        if "relatedartifact" == resource_type_lower:
            from . import relatedartifact
            return relatedartifact.RelatedArtifact(jsondict)
        if "relatedperson" == resource_type_lower:
            from . import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "relatedpersoncommunication" == resource_type_lower:
            from . import relatedperson
            return relatedperson.RelatedPersonCommunication(jsondict)
        if "requestgroup" == resource_type_lower:
            from . import requestgroup
            return requestgroup.RequestGroup(jsondict)
        if "requestgroupaction" == resource_type_lower:
            from . import requestgroup
            return requestgroup.RequestGroupAction(jsondict)
        if "requestgroupactioncondition" == resource_type_lower:
            from . import requestgroup
            return requestgroup.RequestGroupActionCondition(jsondict)
        if "requestgroupactionrelatedaction" == resource_type_lower:
            from . import requestgroup
            return requestgroup.RequestGroupActionRelatedAction(jsondict)
        if "researchdefinition" == resource_type_lower:
            from . import researchdefinition
            return researchdefinition.ResearchDefinition(jsondict)
        if "researchelementdefinition" == resource_type_lower:
            from . import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinition(jsondict)
        if "researchelementdefinitioncharacteristic" == resource_type_lower:
            from . import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinitionCharacteristic(jsondict)
        if "researchstudy" == resource_type_lower:
            from . import researchstudy
            return researchstudy.ResearchStudy(jsondict)
        if "researchstudyarm" == resource_type_lower:
            from . import researchstudy
            return researchstudy.ResearchStudyArm(jsondict)
        if "researchstudyobjective" == resource_type_lower:
            from . import researchstudy
            return researchstudy.ResearchStudyObjective(jsondict)
        if "researchsubject" == resource_type_lower:
            from . import researchsubject
            return researchsubject.ResearchSubject(jsondict)
        if "resource" == resource_type_lower:
            from . import resource
            return resource.Resource(jsondict)
        if "riskassessment" == resource_type_lower:
            from . import riskassessment
            return riskassessment.RiskAssessment(jsondict)
        if "riskassessmentprediction" == resource_type_lower:
            from . import riskassessment
            return riskassessment.RiskAssessmentPrediction(jsondict)
        if "riskevidencesynthesis" == resource_type_lower:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesis(jsondict)
        if "riskevidencesynthesiscertainty" == resource_type_lower:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisCertainty(jsondict)
        if "riskevidencesynthesiscertaintycertaintysubcomponent" == resource_type_lower:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisCertaintyCertaintySubcomponent(jsondict)
        if "riskevidencesynthesisriskestimate" == resource_type_lower:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimate(jsondict)
        if "riskevidencesynthesisriskestimateprecisionestimate" == resource_type_lower:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(jsondict)
        if "riskevidencesynthesissamplesize" == resource_type_lower:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisSampleSize(jsondict)
        if "sampleddata" == resource_type_lower:
            from . import sampleddata
            return sampleddata.SampledData(jsondict)
        if "schedule" == resource_type_lower:
            from . import schedule
            return schedule.Schedule(jsondict)
        if "searchparameter" == resource_type_lower:
            from . import searchparameter
            return searchparameter.SearchParameter(jsondict)
        if "searchparametercomponent" == resource_type_lower:
            from . import searchparameter
            return searchparameter.SearchParameterComponent(jsondict)
        if "servicerequest" == resource_type_lower:
            from . import servicerequest
            return servicerequest.ServiceRequest(jsondict)
        if "signature" == resource_type_lower:
            from . import signature
            return signature.Signature(jsondict)
        if "slot" == resource_type_lower:
            from . import slot
            return slot.Slot(jsondict)
        if "specimen" == resource_type_lower:
            from . import specimen
            return specimen.Specimen(jsondict)
        if "specimencollection" == resource_type_lower:
            from . import specimen
            return specimen.SpecimenCollection(jsondict)
        if "specimencontainer" == resource_type_lower:
            from . import specimen
            return specimen.SpecimenContainer(jsondict)
        if "specimendefinition" == resource_type_lower:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinition(jsondict)
        if "specimendefinitiontypetested" == resource_type_lower:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTested(jsondict)
        if "specimendefinitiontypetestedcontainer" == resource_type_lower:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedContainer(jsondict)
        if "specimendefinitiontypetestedcontaineradditive" == resource_type_lower:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive(jsondict)
        if "specimendefinitiontypetestedhandling" == resource_type_lower:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedHandling(jsondict)
        if "specimenprocessing" == resource_type_lower:
            from . import specimen
            return specimen.SpecimenProcessing(jsondict)
        if "structuredefinition" == resource_type_lower:
            from . import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
        if "structuredefinitioncontext" == resource_type_lower:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionContext(jsondict)
        if "structuredefinitiondifferential" == resource_type_lower:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionDifferential(jsondict)
        if "structuredefinitionmapping" == resource_type_lower:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionMapping(jsondict)
        if "structuredefinitionsnapshot" == resource_type_lower:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionSnapshot(jsondict)
        if "structuremap" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMap(jsondict)
        if "structuremapgroup" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroup(jsondict)
        if "structuremapgroupinput" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroupInput(jsondict)
        if "structuremapgrouprule" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroupRule(jsondict)
        if "structuremapgroupruledependent" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroupRuleDependent(jsondict)
        if "structuremapgrouprulesource" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroupRuleSource(jsondict)
        if "structuremapgroupruletarget" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTarget(jsondict)
        if "structuremapgroupruletargetparameter" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTargetParameter(jsondict)
        if "structuremapstructure" == resource_type_lower:
            from . import structuremap
            return structuremap.StructureMapStructure(jsondict)
        if "subscription" == resource_type_lower:
            from . import subscription
            return subscription.Subscription(jsondict)
        if "subscriptionchannel" == resource_type_lower:
            from . import subscription
            return subscription.SubscriptionChannel(jsondict)
        if "substance" == resource_type_lower:
            from . import substance
            return substance.Substance(jsondict)
        if "substanceamount" == resource_type_lower:
            from . import substanceamount
            return substanceamount.SubstanceAmount(jsondict)
        if "substanceamountreferencerange" == resource_type_lower:
            from . import substanceamount
            return substanceamount.SubstanceAmountReferenceRange(jsondict)
        if "substanceingredient" == resource_type_lower:
            from . import substance
            return substance.SubstanceIngredient(jsondict)
        if "substanceinstance" == resource_type_lower:
            from . import substance
            return substance.SubstanceInstance(jsondict)
        if "substancenucleicacid" == resource_type_lower:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcid(jsondict)
        if "substancenucleicacidsubunit" == resource_type_lower:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunit(jsondict)
        if "substancenucleicacidsubunitlinkage" == resource_type_lower:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunitLinkage(jsondict)
        if "substancenucleicacidsubunitsugar" == resource_type_lower:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunitSugar(jsondict)
        if "substancepolymer" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymer(jsondict)
        if "substancepolymermonomerset" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerMonomerSet(jsondict)
        if "substancepolymermonomersetstartingmaterial" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerMonomerSetStartingMaterial(jsondict)
        if "substancepolymerrepeat" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeat(jsondict)
        if "substancepolymerrepeatrepeatunit" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnit(jsondict)
        if "substancepolymerrepeatrepeatunitdegreeofpolymerisation" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(jsondict)
        if "substancepolymerrepeatrepeatunitstructuralrepresentation" == resource_type_lower:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnitStructuralRepresentation(jsondict)
        if "substanceprotein" == resource_type_lower:
            from . import substanceprotein
            return substanceprotein.SubstanceProtein(jsondict)
        if "substanceproteinsubunit" == resource_type_lower:
            from . import substanceprotein
            return substanceprotein.SubstanceProteinSubunit(jsondict)
        if "substancereferenceinformation" == resource_type_lower:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformation(jsondict)
        if "substancereferenceinformationclassification" == resource_type_lower:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationClassification(jsondict)
        if "substancereferenceinformationgene" == resource_type_lower:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationGene(jsondict)
        if "substancereferenceinformationgeneelement" == resource_type_lower:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationGeneElement(jsondict)
        if "substancereferenceinformationtarget" == resource_type_lower:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationTarget(jsondict)
        if "substancesourcematerial" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterial(jsondict)
        if "substancesourcematerialfractiondescription" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialFractionDescription(jsondict)
        if "substancesourcematerialorganism" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganism(jsondict)
        if "substancesourcematerialorganismauthor" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismAuthor(jsondict)
        if "substancesourcematerialorganismhybrid" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismHybrid(jsondict)
        if "substancesourcematerialorganismorganismgeneral" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismOrganismGeneral(jsondict)
        if "substancesourcematerialpartdescription" == resource_type_lower:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialPartDescription(jsondict)
        if "substancespecification" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecification(jsondict)
        if "substancespecificationmoiety" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationMoiety(jsondict)
        if "substancespecificationname" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationName(jsondict)
        if "substancespecificationnameofficial" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationNameOfficial(jsondict)
        if "substancespecificationproperty" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationProperty(jsondict)
        if "substancespecificationrelationship" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationRelationship(jsondict)
        if "substancespecificationstructure" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructure(jsondict)
        if "substancespecificationstructureisotope" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructureIsotope(jsondict)
        if "substancespecificationstructureisotopemolecularweight" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructureIsotopeMolecularWeight(jsondict)
        if "substancespecificationstructurerepresentation" == resource_type_lower:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructureRepresentation(jsondict)
        if "substancespecificationstr" == resource_type_lower: # Note: This might be a typo in original template, usually Structure or Code
            from . import substancespecification
            return substancespecification.SubstanceSpecificationstr(jsondict) # Keeping as-is if it's intentional
        if "supplydelivery" == resource_type_lower:
            from . import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict)
        if "supplydeliverysupplieditem" == resource_type_lower:
            from . import supplydelivery
            return supplydelivery.SupplyDeliverySuppliedItem(jsondict)
        if "supplyrequest" == resource_type_lower:
            from . import supplyrequest
            return supplyrequest.SupplyRequest(jsondict)
        if "supplyrequestparameter" == resource_type_lower:
            from . import supplyrequest
            return supplyrequest.SupplyRequestParameter(jsondict)
        if "task" == resource_type_lower:
            from . import task
            return task.Task(jsondict)
        if "taskinput" == resource_type_lower:
            from . import task
            return task.TaskInput(jsondict)
        if "taskoutput" == resource_type_lower:
            from . import task
            return task.TaskOutput(jsondict)
        if "taskrestriction" == resource_type_lower:
            from . import task
            return task.TaskRestriction(jsondict)
        if "terminologycapabilities" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilities(jsondict)
        if "terminologycapabilitiesclosure" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesClosure(jsondict)
        if "terminologycapabilitiescodesystem" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystem(jsondict)
        if "terminologycapabilitiescodesystemversion" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion(jsondict)
        if "terminologycapabilitiescodesystemversionfilter" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter(jsondict)
        if "terminologycapabilitiesexpansion" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesExpansion(jsondict)
        if "terminologycapabilitiesexpansionparameter" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesExpansionParameter(jsondict)
        if "terminologycapabilitiesimplementation" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesImplementation(jsondict)
        if "terminologycapabilitiessoftware" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesSoftware(jsondict)
        if "terminologycapabilitiestranslation" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesTranslation(jsondict)
        if "terminologycapabilitiesvalidatecode" == resource_type_lower:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesValidateCode(jsondict)
        if "testreport" == resource_type_lower:
            from . import testreport
            return testreport.TestReport(jsondict)
        if "testreportparticipant" == resource_type_lower:
            from . import testreport
            return testreport.TestReportParticipant(jsondict)
        if "testreportsetup" == resource_type_lower:
            from . import testreport
            return testreport.TestReportSetup(jsondict)
        if "testreportsetupaction" == resource_type_lower:
            from . import testreport
            return testreport.TestReportSetupAction(jsondict)
        if "testreportsetupactionassert" == resource_type_lower:
            from . import testreport
            return testreport.TestReportSetupActionAssert(jsondict)
        if "testreportsetupactionoperation" == resource_type_lower:
            from . import testreport
            return testreport.TestReportSetupActionOperation(jsondict)
        if "testreportteardown" == resource_type_lower:
            from . import testreport
            return testreport.TestReportTeardown(jsondict)
        if "testreportteardownaction" == resource_type_lower:
            from . import testreport
            return testreport.TestReportTeardownAction(jsondict)
        if "testreporttest" == resource_type_lower:
            from . import testreport
            return testreport.TestReportTest(jsondict)
        if "testreporttestaction" == resource_type_lower:
            from . import testreport
            return testreport.TestReportTestAction(jsondict)
        if "testscript" == resource_type_lower:
            from . import testscript
            return testscript.TestScript(jsondict)
        if "testscriptdestination" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptDestination(jsondict)
        if "testscriptfixture" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptFixture(jsondict)
        if "testscriptmetadata" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptMetadata(jsondict)
        if "testscriptmetadatacapability" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptMetadataCapability(jsondict)
        if "testscriptmetadatalink" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptMetadataLink(jsondict)
        if "testscriptorigin" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptOrigin(jsondict)
        if "testscriptsetup" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptSetup(jsondict)
        if "testscriptsetupaction" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptSetupAction(jsondict)
        if "testscriptsetupactionassert" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptSetupActionAssert(jsondict)
        if "testscriptsetupactionoperation" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptSetupActionOperation(jsondict)
        if "testscriptsetupactionoperationrequestheader" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptSetupActionOperationRequestHeader(jsondict)
        if "testscriptteardown" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptTeardown(jsondict)
        if "testscriptteardownaction" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptTeardownAction(jsondict)
        if "testscripttest" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptTest(jsondict)
        if "testscripttestaction" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptTestAction(jsondict)
        if "testscriptvariable" == resource_type_lower:
            from . import testscript
            return testscript.TestScriptVariable(jsondict)
        if "timing" == resource_type_lower:
            from . import timing
            return timing.Timing(jsondict)
        if "timingrepeat" == resource_type_lower:
            from . import timing
            return timing.TimingRepeat(jsondict)
        if "triggerdefinition" == resource_type_lower:
            from . import triggerdefinition
            return triggerdefinition.TriggerDefinition(jsondict)
        if "usagecontext" == resource_type_lower:
            from . import usagecontext
            return usagecontext.UsageContext(jsondict)
        if "valueset" == resource_type_lower:
            from . import valueset
            return valueset.ValueSet(jsondict)
        if "valuesetcompose" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetCompose(jsondict)
        if "valuesetcomposeinclude" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetComposeInclude(jsondict)
        if "valuesetcomposeincludeconcept" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetComposeIncludeConcept(jsondict)
        if "valuesetcomposeincludeconceptdesignation" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetComposeIncludeConceptDesignation(jsondict)
        if "valuesetcomposeincludefilter" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetComposeIncludeFilter(jsondict)
        if "valuesetexpansion" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetExpansion(jsondict)
        if "valuesetexpansioncontains" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetExpansionContains(jsondict)
        if "valuesetexpansionparameter" == resource_type_lower:
            from . import valueset
            return valueset.ValueSetExpansionParameter(jsondict)
        if "verificationresult" == resource_type_lower:
            from . import verificationresult
            return verificationresult.VerificationResult(jsondict)
        if "verificationresultattestation" == resource_type_lower:
            from . import verificationresult
            return verificationresult.VerificationResultAttestation(jsondict)
        if "verificationresultprimarysource" == resource_type_lower:
            from . import verificationresult
            return verificationresult.VerificationResultPrimarySource(jsondict)
        if "verificationresultvalidator" == resource_type_lower:
            from . import verificationresult
            return verificationresult.VerificationResultValidator(jsondict)
        if "visionprescription" == resource_type_lower:
            from . import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "visionprescriptionlensspecification" == resource_type_lower:
            from . import visionprescription
            return visionprescription.VisionPrescriptionLensSpecification(jsondict)
        if "visionprescriptionlensspecificationprism" == resource_type_lower:
            from . import visionprescription
            return visionprescription.VisionPrescriptionLensSpecificationPrism(jsondict)

        from . import element # Default fallback
        return element.Element(jsondict)
