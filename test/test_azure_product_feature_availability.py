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

from openapi_client.models.azure_product_feature_availability import AzureProductFeatureAvailability  # noqa: E501

class TestAzureProductFeatureAvailability(unittest.TestCase):
    """AzureProductFeatureAvailability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductFeatureAvailability:
        """Test AzureProductFeatureAvailability
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureProductFeatureAvailability`
        """
        model = AzureProductFeatureAvailability()  # noqa: E501
        if include_optional:
            return AzureProductFeatureAvailability(
                custom_meters = [
                    openapi_client.models.azure_product_variant_custom_meter.AzureProductVariantCustomMeter(
                        display_name = '', 
                        id = '', 
                        included_base_quantities = [
                            openapi_client.models.azure_included_base_quantity.AzureIncludedBaseQuantity(
                                is_infinite = True, 
                                quantity = 1.337, 
                                recurring_unit = 'Monthly', )
                            ], 
                        is_enabled = True, 
                        price_in_usd = 1.337, 
                        unique_id = '', 
                        unit_of_measure = '', )
                    ],
                id = '',
                is_hidden = True,
                market_states = [
                    openapi_client.models.azure_market_state.AzureMarketState(
                        market_code = '', 
                        state = 'Disabled', )
                    ],
                markets = [
                    openapi_client.models.azure_market.AzureMarket(
                        friendly_name = '', 
                        market_code = '', )
                    ],
                price_schedules = [
                    openapi_client.models.azure_product_variant_price_schedule.AzureProductVariantPriceSchedule(
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
                            ], )
                    ],
                properties = [
                    openapi_client.models.azure_type_value.AzureTypeValue(
                        type = '', 
                        value = '', )
                    ],
                resource_type = '',
                subscription_audiences = [
                    openapi_client.models.azure_audience.AzureAudience(
                        description = '', 
                        id = '', )
                    ],
                tenant_audiences = [
                    openapi_client.models.azure_audience.AzureAudience(
                        description = '', 
                        id = '', )
                    ],
                trial = openapi_client.models.azure_product_variant_trial.AzureProductVariantTrial(
                    date_time_range = openapi_client.models.azure_localized_time_range.AzureLocalizedTimeRange(
                        end_at = openapi_client.models.azure_localized_date_time.AzureLocalizedDateTime(
                            date_time_in_utc = '', 
                            localize_per_market = True, ), 
                        start_at = openapi_client.models.azure_localized_date_time.AzureLocalizedDateTime(
                            date_time_in_utc = '', 
                            localize_per_market = True, ), ), 
                    duration = 56, 
                    duration_type = 'Minute', 
                    type = 'NoTrial', ),
                visibility = 'Public'
            )
        else:
            return AzureProductFeatureAvailability(
        )
        """

    def testAzureProductFeatureAvailability(self):
        """Test AzureProductFeatureAvailability"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
