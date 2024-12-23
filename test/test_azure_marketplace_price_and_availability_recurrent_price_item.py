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

from suger_sdk_python.models.azure_marketplace_price_and_availability_recurrent_price_item import AzureMarketplacePriceAndAvailabilityRecurrentPriceItem

class TestAzureMarketplacePriceAndAvailabilityRecurrentPriceItem(unittest.TestCase):
    """AzureMarketplacePriceAndAvailabilityRecurrentPriceItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePriceAndAvailabilityRecurrentPriceItem:
        """Test AzureMarketplacePriceAndAvailabilityRecurrentPriceItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplacePriceAndAvailabilityRecurrentPriceItem`
        """
        model = AzureMarketplacePriceAndAvailabilityRecurrentPriceItem()
        if include_optional:
            return AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
                billing_term = {"type":"day","value":7.386281948385884},
                payment_option = {"type":"day","value":7.386281948385884},
                price_per_payment_in_usd = 1.337,
                prices = [
                    {"markets":["markets","markets"],"price":1.0246457001441578,"currency":"currency"}
                    ]
            )
        else:
            return AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
        )
        """

    def testAzureMarketplacePriceAndAvailabilityRecurrentPriceItem(self):
        """Test AzureMarketplacePriceAndAvailabilityRecurrentPriceItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
