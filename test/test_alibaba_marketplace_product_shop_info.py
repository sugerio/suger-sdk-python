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

from suger_sdk_python.models.alibaba_marketplace_product_shop_info import AlibabaMarketplaceProductShopInfo

class TestAlibabaMarketplaceProductShopInfo(unittest.TestCase):
    """AlibabaMarketplaceProductShopInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlibabaMarketplaceProductShopInfo:
        """Test AlibabaMarketplaceProductShopInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlibabaMarketplaceProductShopInfo`
        """
        model = AlibabaMarketplaceProductShopInfo()
        if include_optional:
            return AlibabaMarketplaceProductShopInfo(
                emails = '',
                id = 56,
                name = '',
                telephones = {"Telephone":["Telephone","Telephone"]},
                wang_wangs = {"WangWang":[{"UserName":"UserName","Remark":"Remark"},{"UserName":"UserName","Remark":"Remark"}]}
            )
        else:
            return AlibabaMarketplaceProductShopInfo(
        )
        """

    def testAlibabaMarketplaceProductShopInfo(self):
        """Test AlibabaMarketplaceProductShopInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
