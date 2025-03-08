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

from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_price_model_template_payg import GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg

class TestGcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg(unittest.TestCase):
    """GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg:
        """Test GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg`
        """
        model = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg()
        if include_optional:
            return GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg(
                discount_template = {"discountPercentage":{"minAmount":{"nanos":4,"units":"units"},"defaultAmount":{"nanos":4,"units":"units"},"maxAmount":{"nanos":4,"units":"units"}},"discountEconomics":"discountEconomics","hideDiscountPercentage":true,"discountedPrice":{"nanos":1,"units":"units","currencyCode":"currencyCode"}},
                period = {"unit":"MONTHLY_PERIOD","count":5},
                sku_discount_templates = [
                    None
                    ],
                sku_representation = {"skuList":{"skus":["skus","skus"]},"skus":"skus","skuGroupList":"{}"}
            )
        else:
            return GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg(
        )
        """

    def testGcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg(self):
        """Test GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
