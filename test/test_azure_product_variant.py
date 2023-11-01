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


from openapi_client.models.azure_product_variant import (
    AzureProductVariant,
)  # noqa: E501


class TestAzureProductVariant(unittest.TestCase):
    """AzureProductVariant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductVariant:
        """Test AzureProductVariant
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureProductVariant`
        """
        model = AzureProductVariant()  # noqa: E501
        if include_optional:
            return AzureProductVariant(
                azure_government_certifications = [
                    openapi_client.models.azure_government_certification.AzureGovernmentCertification(
                        title = '', 
                        uri = '', 
                        validation_results = [
                            openapi_client.models.azure_validation_result.AzureValidationResult(
                                error_message = '', 
                                member_names = [
                                    ''
                                    ], )
                            ], )
                    ],
                cloud_availabilities = [
                    ''
                    ],
                conversion_paths = '',
                extended_properties = [
                    openapi_client.models.azure_type_value.AzureTypeValue(
                        type = '', 
                        value = '', )
                    ],
                external_id = '',
                feature_availabilities = [
                    openapi_client.models.azure_product_feature_availability.AzureProductFeatureAvailability(
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
                            duration = 56, 
                            duration_type = 'Minute', 
                            type = 'NoTrial', ), 
                        visibility = 'Public', )
                    ],
                friendly_name = '',
                id = '',
                lead_gen_id = '',
                reference_variant_id = '',
                resource_type = 'AzureSkuVariant',
                state = 'InActive'
            )
        else:
            return AzureProductVariant(
        )
        """

    def testAzureProductVariant(self):
        """Test AzureProductVariant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
