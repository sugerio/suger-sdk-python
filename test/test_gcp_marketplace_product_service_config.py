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

from openapi_client.models.gcp_marketplace_product_service_config import \
    GcpMarketplaceProductServiceConfig  # noqa: E501


class TestGcpMarketplaceProductServiceConfig(unittest.TestCase):
    """GcpMarketplaceProductServiceConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProductServiceConfig:
        """Test GcpMarketplaceProductServiceConfig
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplaceProductServiceConfig`
        """
        model = GcpMarketplaceProductServiceConfig()  # noqa: E501
        if include_optional:
            return GcpMarketplaceProductServiceConfig(
                billing = openapi_client.models.gcp_marketplace_product_service_config_billing.GcpMarketplaceProductServiceConfigBilling(
                    metrics = [
                        ''
                        ], ),
                metrics = [
                    openapi_client.models.gcp_marketplace_product_metering_metric.GcpMarketplaceProductMeteringMetric(
                        description = '', 
                        display_name = '', 
                        display_unit = '', 
                        display_unit_description = '', 
                        id = '', 
                        metric_kind = '', 
                        name = '', 
                        price_tiers = [
                            openapi_client.models.gcp_price_tier.GcpPriceTier(
                                from_amount = 1.337, 
                                price = openapi_client.models.gcp_price_value.GcpPriceValue(
                                    currency_code = '', 
                                    nanos = 56, 
                                    units = '', ), 
                                starting_usage_amount = '', )
                            ], 
                        reporting_unit = '', 
                        sku_id = '', 
                        unit = '', 
                        value_type = openapi_client.models.value_type.valueType(), )
                    ],
                name = '',
                producer_project_id = '',
                title = ''
            )
        else:
            return GcpMarketplaceProductServiceConfig(
        )
        """

    def testGcpMarketplaceProductServiceConfig(self):
        """Test GcpMarketplaceProductServiceConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
