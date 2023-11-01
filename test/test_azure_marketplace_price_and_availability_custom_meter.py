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

from openapi_client.models.azure_marketplace_price_and_availability_custom_meter import (
    AzureMarketplacePriceAndAvailabilityCustomMeter,
)  # noqa: E501


class TestAzureMarketplacePriceAndAvailabilityCustomMeter(unittest.TestCase):
    """AzureMarketplacePriceAndAvailabilityCustomMeter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AzureMarketplacePriceAndAvailabilityCustomMeter:
        """Test AzureMarketplacePriceAndAvailabilityCustomMeter
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePriceAndAvailabilityCustomMeter`
        """
        model = AzureMarketplacePriceAndAvailabilityCustomMeter()  # noqa: E501
        if include_optional:
            return AzureMarketplacePriceAndAvailabilityCustomMeter(
                var_schema = '',
                custom_meters = {
                    'key' : openapi_client.models.azure_marketplace_price_and_availability_custom_meter_item.AzureMarketplacePriceAndAvailabilityCustomMeterItem(
                        display_name = '', 
                        unit_of_measure = '', )
                    },
                id = '',
                product = '',
                resource_name = '',
                validations = [
                    openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                        __schema = '', 
                        code = 'businessValidationError', 
                        level = 'informational', 
                        message = '', 
                        resource_id = '', )
                    ]
            )
        else:
            return AzureMarketplacePriceAndAvailabilityCustomMeter(
        )
        """

    def testAzureMarketplacePriceAndAvailabilityCustomMeter(self):
        """Test AzureMarketplacePriceAndAvailabilityCustomMeter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
