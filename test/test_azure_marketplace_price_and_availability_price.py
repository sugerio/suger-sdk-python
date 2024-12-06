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

from suger_sdk_python.models.azure_marketplace_price_and_availability_price import AzureMarketplacePriceAndAvailabilityPrice

class TestAzureMarketplacePriceAndAvailabilityPrice(unittest.TestCase):
    """AzureMarketplacePriceAndAvailabilityPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePriceAndAvailabilityPrice:
        """Test AzureMarketplacePriceAndAvailabilityPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplacePriceAndAvailabilityPrice`
        """
        model = AzureMarketplacePriceAndAvailabilityPrice()
        if include_optional:
            return AzureMarketplacePriceAndAvailabilityPrice(
                core_pricing = {"price":6.965117697638846,"priceInputOption":"free","pricePerCoreSize":"{}","pricePerCore":1.284659006116532,"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},
                custom_meters = {"priceInputOption":"perMarket","meters":{"key":{"pricePerPaymentInUsd":6.778324963048013,"includedQuantities":[{"quantity":2.8841621266687802,"isInfinite":true,"billingTerm":{"type":"day","value":7.386281948385884}},{"quantity":2.8841621266687802,"isInfinite":true,"billingTerm":{"type":"day","value":7.386281948385884}}],"billingTerm":{"type":"day","value":7.386281948385884},"paymentOption":{"type":"day","value":7.386281948385884},"prices":[{"pricePerPaymentInUsd":6.878052220127876,"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},{"pricePerPaymentInUsd":6.878052220127876,"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]}]}}},
                license_model = 'byol',
                recurrent_price = {"recurrentPriceMode":"flatRate","userLimits":{"min":6.84685269835264,"max":1.4894159098541704},"priceInputOption":"perMarket","prices":[{"pricePerPaymentInUsd":1.2315135367772556,"billingTerm":{"type":"day","value":7.386281948385884},"paymentOption":{"type":"day","value":7.386281948385884},"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]},{"pricePerPaymentInUsd":1.2315135367772556,"billingTerm":{"type":"day","value":7.386281948385884},"paymentOption":{"type":"day","value":7.386281948385884},"prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]}]},
                system_meter_pricing = {"price":5.944895607614016,"priceInputOption":"perCore","prices":[{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"},{"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}]}
            )
        else:
            return AzureMarketplacePriceAndAvailabilityPrice(
        )
        """

    def testAzureMarketplacePriceAndAvailabilityPrice(self):
        """Test AzureMarketplacePriceAndAvailabilityPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
