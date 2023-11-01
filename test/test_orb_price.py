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

from openapi_client.models.orb_price import OrbPrice  # noqa: E501


class TestOrbPrice(unittest.TestCase):
    """OrbPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbPrice:
        """Test OrbPrice
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `OrbPrice`
        """
        model = OrbPrice()  # noqa: E501
        if include_optional:
            return OrbPrice(
                billable_metric = openapi_client.models.orb_billable_metric.OrbBillableMetric(
                    description = '', 
                    id = '', 
                    metadata = {
                        'key' : ''
                        }, 
                    name = '', 
                    status = 'active', ),
                bps_config = openapi_client.models.orb_price_model_config_bps.OrbPriceModelConfig_BPS(
                    bps = 1.337, 
                    per_unit_maximum = '', ),
                bulk_bps_config = openapi_client.models.orb_price_model_config_bulk_bps.OrbPriceModelConfig_BULK_BPS(
                    tiers = [
                        openapi_client.models.orb_price_tier.OrbPriceTier(
                            bps = 1.337, 
                            first_unit = '', 
                            last_unit = '', 
                            maximum_amount = '', 
                            maximum_units = 1.337, 
                            minimum_amount = '', 
                            per_unit_maximum = '', 
                            unit_amount = '', )
                        ], ),
                bulk_config = openapi_client.models.orb_price_model_config_bulk.OrbPriceModelConfig_BULK(
                    tiers = [
                        openapi_client.models.orb_price_tier.OrbPriceTier(
                            bps = 1.337, 
                            first_unit = '', 
                            last_unit = '', 
                            maximum_amount = '', 
                            maximum_units = 1.337, 
                            minimum_amount = '', 
                            per_unit_maximum = '', 
                            unit_amount = '', )
                        ], ),
                cadence = 'monthly',
                created_at = '',
                currency = '',
                discount = openapi_client.models.orb_price_discount.OrbPriceDiscount(
                    amount_discount = '', 
                    applies_to_price_ids = [
                        ''
                        ], 
                    discount_type = 'percentage', 
                    percentage_discount = 1.337, 
                    trial_amount_discount = '', 
                    usage_discount = '', ),
                fixed_price_quantity = 56,
                id = '',
                item = openapi_client.models.orb_item.OrbItem(
                    created_at = '', 
                    external_connections = [
                        openapi_client.models.orb_external_connection.OrbExternalConnection(
                            external_connection_name = 'stripe', 
                            external_entity_id = '', )
                        ], 
                    id = '', 
                    name = '', ),
                matrix_config = openapi_client.models.orb_price_model_config_matrix.OrbPriceModelConfig_MATRIX(
                    default_unit_amount = '', 
                    dimensions = [
                        ''
                        ], 
                    matrix_values = [
                        openapi_client.models.orb_matrix_price_value.OrbMatrixPriceValue(
                            dimension_values = [
                                ''
                                ], 
                            unit_amount = '', )
                        ], ),
                maximum = openapi_client.models.orb_price_maximum.OrbPriceMaximum(
                    applies_to_price_ids = [
                        ''
                        ], 
                    maximum_amount = '', ),
                minimum = openapi_client.models.orb_price_minimum.OrbPriceMinimum(
                    applies_to_price_ids = [
                        ''
                        ], 
                    minimum_amount = '', ),
                model_type = '',
                name = '',
                package_config = openapi_client.models.orb_price_model_config_package.OrbPriceModelConfig_PACKAGE(
                    package_amount = '', 
                    package_size = 1.337, ),
                plan_phase_order = 56,
                tiered_bps_config = openapi_client.models.orb_price_model_config_tiered_bps.OrbPriceModelConfig_TIERED_BPS(
                    tiers = [
                        openapi_client.models.orb_price_tier.OrbPriceTier(
                            bps = 1.337, 
                            first_unit = '', 
                            last_unit = '', 
                            maximum_amount = '', 
                            maximum_units = 1.337, 
                            minimum_amount = '', 
                            per_unit_maximum = '', 
                            unit_amount = '', )
                        ], ),
                tiered_config = openapi_client.models.orb_price_model_config_tiered.OrbPriceModelConfig_TIERED(
                    tiers = [
                        openapi_client.models.orb_price_tier.OrbPriceTier(
                            bps = 1.337, 
                            first_unit = '', 
                            last_unit = '', 
                            maximum_amount = '', 
                            maximum_units = 1.337, 
                            minimum_amount = '', 
                            per_unit_maximum = '', 
                            unit_amount = '', )
                        ], ),
                unit_config = openapi_client.models.orb_price_model_config_unit.OrbPriceModelConfig_UNIT(
                    unit_amount = '', )
            )
        else:
            return OrbPrice(
        )
        """

    def testOrbPrice(self):
        """Test OrbPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
