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

from openapi_client.models.alibaba_marketplace_product_skus import \
    AlibabaMarketplaceProductSkus  # noqa: E501


class TestAlibabaMarketplaceProductSkus(unittest.TestCase):
    """AlibabaMarketplaceProductSkus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlibabaMarketplaceProductSkus:
        """Test AlibabaMarketplaceProductSkus
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AlibabaMarketplaceProductSkus`
        """
        model = AlibabaMarketplaceProductSkus()  # noqa: E501
        if include_optional:
            return AlibabaMarketplaceProductSkus(
                product_sku = [
                    openapi_client.models.alibaba_marketplace_product_sku.AlibabaMarketplaceProductSku(
                        charge_type = '', 
                        code = '', 
                        constraints = '', 
                        hidden = True, 
                        modules = openapi_client.models.alibaba_marketplace_product_sku_modules.AlibabaMarketplaceProductSkuModules(
                            module = [
                                openapi_client.models.alibaba_marketplace_product_sku_module.AlibabaMarketplaceProductSkuModule(
                                    code = '', 
                                    id = '', 
                                    name = '', 
                                    properties = openapi_client.models.alibaba_marketplace_product_sku_module_properties.AlibabaMarketplaceProductSkuModuleProperties(
                                        property = [
                                            openapi_client.models.alibaba_marketplace_product_sku_module_property.AlibabaMarketplaceProductSkuModuleProperty(
                                                display_unit = '', 
                                                key = '', 
                                                name = '', 
                                                property_values = openapi_client.models.alibaba_marketplace_product_sku_module_property_values.AlibabaMarketplaceProductSkuModulePropertyValues(
                                                    property_value = [
                                                        openapi_client.models.alibaba_marketplace_product_sku_module_property_value.AlibabaMarketplaceProductSkuModulePropertyValue(
                                                            display_name = '', 
                                                            max = '', 
                                                            min = '', 
                                                            remark = '', 
                                                            step = '', 
                                                            type = '', 
                                                            value = '', )
                                                        ], ), 
                                                show_type = '', )
                                            ], ), )
                                ], ), 
                        name = '', 
                        order_periods = openapi_client.models.alibaba_marketplace_product_sku_order_periods.AlibabaMarketplaceProductSkuOrderPeriods(
                            order_period = [
                                openapi_client.models.alibaba_marketplace_product_sku_order_period.AlibabaMarketplaceProductSkuOrderPeriod(
                                    name = '', 
                                    period_type = '', )
                                ], ), )
                    ]
            )
        else:
            return AlibabaMarketplaceProductSkus(
        )
        """

    def testAlibabaMarketplaceProductSkus(self):
        """Test AlibabaMarketplaceProductSkus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
