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

from openapi_client.models.azure_marketplace_private_offer_promotion_reference import AzureMarketplacePrivateOfferPromotionReference  # noqa: E501

class TestAzureMarketplacePrivateOfferPromotionReference(unittest.TestCase):
    """AzureMarketplacePrivateOfferPromotionReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePrivateOfferPromotionReference:
        """Test AzureMarketplacePrivateOfferPromotionReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplacePrivateOfferPromotionReference`
        """
        model = AzureMarketplacePrivateOfferPromotionReference()  # noqa: E501
        if include_optional:
            return AzureMarketplacePrivateOfferPromotionReference(
                id = '',
                name = ''
            )
        else:
            return AzureMarketplacePrivateOfferPromotionReference(
        )
        """

    def testAzureMarketplacePrivateOfferPromotionReference(self):
        """Test AzureMarketplacePrivateOfferPromotionReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
