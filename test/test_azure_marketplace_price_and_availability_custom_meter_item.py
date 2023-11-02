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
import datetime

from openapi_client.models.azure_marketplace_price_and_availability_custom_meter_item import AzureMarketplacePriceAndAvailabilityCustomMeterItem  # noqa: E501

class TestAzureMarketplacePriceAndAvailabilityCustomMeterItem(unittest.TestCase):
    """AzureMarketplacePriceAndAvailabilityCustomMeterItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePriceAndAvailabilityCustomMeterItem:
        """Test AzureMarketplacePriceAndAvailabilityCustomMeterItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplacePriceAndAvailabilityCustomMeterItem`
        """
        model = AzureMarketplacePriceAndAvailabilityCustomMeterItem()  # noqa: E501
        if include_optional:
            return AzureMarketplacePriceAndAvailabilityCustomMeterItem(
                display_name = '',
                unit_of_measure = ''
            )
        else:
            return AzureMarketplacePriceAndAvailabilityCustomMeterItem(
        )
        """

    def testAzureMarketplacePriceAndAvailabilityCustomMeterItem(self):
        """Test AzureMarketplacePriceAndAvailabilityCustomMeterItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
