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

from openapi_client.models.gcp_marketplace_product_purchase_spec import GcpMarketplaceProductPurchaseSpec  # noqa: E501

class TestGcpMarketplaceProductPurchaseSpec(unittest.TestCase):
    """GcpMarketplaceProductPurchaseSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProductPurchaseSpec:
        """Test GcpMarketplaceProductPurchaseSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceProductPurchaseSpec`
        """
        model = GcpMarketplaceProductPurchaseSpec()  # noqa: E501
        if include_optional:
            return GcpMarketplaceProductPurchaseSpec(
                features = [
                    openapi_client.models.gcp_marketplace_product_feature.GcpMarketplaceProductFeature(
                        description = '', 
                        name = '', 
                        title = '', )
                    ],
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
                purchase_option_specs = [
                    openapi_client.models.gcp_marketplace_product_purchase_option_spec.GcpMarketplaceProductPurchaseOptionSpec(
                        feature_values = [
                            openapi_client.models.gcp_marketplace_product_feature_value.GcpMarketplaceProductFeatureValue(
                                feature_description = '', 
                                feature_name = '', 
                                feature_title = '', 
                                feature_value = '', )
                            ], 
                        name = '', 
                        price_info = openapi_client.models.gcp_marketplace_product_price_info.GcpMarketplaceProductPriceInfo(
                            description = '', 
                            price_model = 'FREE', 
                            subscription_plans = [
                                openapi_client.models.gcp_marketplace_product_subscription_plan.GcpMarketplaceProductSubscriptionPlan(
                                    period = '', 
                                    price = openapi_client.models.gcp_price_value.GcpPriceValue(
                                        currency_code = '', 
                                        nanos = 56, 
                                        units = '', ), )
                                ], 
                            usage_fees = [
                                openapi_client.models.gcp_marketplace_product_usage_fee.GcpMarketplaceProductUsageFee(
                                    display_quantity = 56, 
                                    metric_id = '', 
                                    price_tiers = [
                                        openapi_client.models.gcp_price_tier.GcpPriceTier(
                                            from_amount = 1.337, 
                                            starting_usage_amount = '', )
                                        ], )
                                ], ), 
                        purchase_mode = 'PURCHASE_MODE_PRIVATE', 
                        title = '', )
                    ]
            )
        else:
            return GcpMarketplaceProductPurchaseSpec(
        )
        """

    def testGcpMarketplaceProductPurchaseSpec(self):
        """Test GcpMarketplaceProductPurchaseSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
