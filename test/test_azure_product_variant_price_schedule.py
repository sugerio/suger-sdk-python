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

from openapi_client.models.azure_product_variant_price_schedule import (
    AzureProductVariantPriceSchedule,
)  # noqa: E501


class TestAzureProductVariantPriceSchedule(unittest.TestCase):
    """AzureProductVariantPriceSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductVariantPriceSchedule:
        """Test AzureProductVariantPriceSchedule
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureProductVariantPriceSchedule`
        """
        model = AzureProductVariantPriceSchedule()  # noqa: E501
        if include_optional:
            return AzureProductVariantPriceSchedule(
                date_time_range = openapi_client.models.azure_localized_time_range.AzureLocalizedTimeRange(
                    end_at = openapi_client.models.azure_localized_date_time.AzureLocalizedDateTime(
                        date_time_in_utc = '', 
                        localize_per_market = True, ), 
                    start_at = openapi_client.models.azure_localized_date_time.AzureLocalizedDateTime(
                        date_time_in_utc = '', 
                        localize_per_market = True, ), ),
                friendly_name = '',
                is_base_schedule = True,
                market_codes = [
                    ''
                    ],
                schedules = [
                    openapi_client.models.azure_price_schedule.AzurePriceSchedule(
                        price_cadence = openapi_client.models.azure_price_cadence.AzurePriceCadence(
                            type = 'Month', 
                            value = 56, ), 
                        pricing_model = 'Flat', 
                        pricing_units = [
                            openapi_client.models.azure_pricing_unit.AzurePricingUnit(
                                is_unlimited_unit = True, 
                                lower_unit = 56, 
                                name = 'sharedcore', 
                                unit_type = '', 
                                upper_unit = 56, )
                            ], 
                        retail_price = openapi_client.models.azure_price.AzurePrice(
                            currency_code = '', 
                            open_price = 1.337, 
                            price_tier_id = '', ), )
                    ]
            )
        else:
            return AzureProductVariantPriceSchedule(
        )
        """

    def testAzureProductVariantPriceSchedule(self):
        """Test AzureProductVariantPriceSchedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
