# coding: utf-8

"""
    Suger API

    CRUD operations on a set of resources, including organizations, products, offers, entitlements, usage record groups for meterting, etc.

    The version of the OpenAPI document: 1.0
    Contact: support@suger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from suger_sdk_python.models.azure_marketplace_plan_resource import AzureMarketplacePlanResource

class TestAzureMarketplacePlanResource(unittest.TestCase):
    """AzureMarketplacePlanResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePlanResource:
        """Test AzureMarketplacePlanResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplacePlanResource`
        """
        model = AzureMarketplacePlanResource()
        if include_optional:
            return AzureMarketplacePlanResource(
                plan = {"deprecationSchedule":{"date":"date","reason":"criticalSecurityIssue","$schema":"$schema","alternative":{"product":"{}","plan":"{}"},"dateOffset":"dateOffset"},"lifecycleState":null,"product":"product","displayRank":3,"$schema":"$schema","azureGovernmentCertifications":[{"link":"link","name":"name"},{"link":"link","name":"name"}],"resourceName":"resourceName","azureRegions":["azureRegions","azureRegions"],"subtype":"managedApplication","identity":{"externalId":"externalId"},"alias":"alias","id":"id","validations":[{"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"},{"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"}]},
                plan_listing = {"summary":"summary","lifecycleState":null,"product":"product","$schema":"$schema","kind":"azureVM-plan","languageId":"languageId","name":"name","description":"description","resourceName":"resourceName","id":"id","validations":[{"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"},{"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"}],"plan":"plan"},
                price_and_availability_plan = {"audience":"public","product":"product","softwareReservation":[{"percentageSave":6.704019297950036,"term":3.353193347011243,"type":"month"},{"percentageSave":6.704019297950036,"term":3.353193347011243,"type":"month"}],"$schema":"$schema","visibility":"visible","meterDefine":"meterDefine","billingTag":"billingTag","resourceName":"resourceName","trial":{"type":"day","value":7.386281948385884},"markets":["markets","markets"],"privateAudiences":[{"id":"id","label":"label","type":"none"},{"id":"id","label":"label","type":"none"}],"id":"id","validations":[{"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"},{"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"}],"plan":"plan","pricing":{"customMeters":{"priceInputOption":"perMarket","meters":{"key":{"pricePerPaymentInUsd":6.778324963048013,"includedQuantities":[{"quantity":2.8841621266687802,"isInfinite":true,"billingTerm":{"type":"day","value":7.386281948385884}},{"quantity":2.8841621266687802,"isInfinite":true,"billingTerm":{"type":"day","value":7.386281948385884}}],"billingTerm":{"type":"day","value":7.386281948385884},"paymentOption":{"type":"day","value":7.386281948385884},"prices":[{"pricePerPaymentInUsd":6.878052220127876,"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},{"pricePerPaymentInUsd":6.878052220127876,"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]}]}}},"licenseModel":"byol","systemMeterPricing":{"price":5.944895607614016,"priceInputOption":"perCore","prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},"corePricing":{"price":6.965117697638846,"priceInputOption":"free","pricePerCoreSize":"{}","pricePerCore":1.284659006116532,"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},"recurrentPrice":{"recurrentPriceMode":"flatRate","userLimits":{"min":6.84685269835264,"max":1.4894159098541704},"priceInputOption":"perMarket","prices":[{"pricePerPaymentInUsd":1.2315135367772556,"billingTerm":{"type":"day","value":7.386281948385884},"paymentOption":{"type":"day","value":7.386281948385884},"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},{"pricePerPaymentInUsd":1.2315135367772556,"billingTerm":{"type":"day","value":7.386281948385884},"paymentOption":{"type":"day","value":7.386281948385884},"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]}]}}}
            )
        else:
            return AzureMarketplacePlanResource(
        )
        """

    def testAzureMarketplacePlanResource(self):
        """Test AzureMarketplacePlanResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
