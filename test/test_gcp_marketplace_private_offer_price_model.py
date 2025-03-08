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

from suger_sdk_python.models.gcp_marketplace_private_offer_price_model import GcpMarketplacePrivateOfferPriceModel

class TestGcpMarketplacePrivateOfferPriceModel(unittest.TestCase):
    """GcpMarketplacePrivateOfferPriceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplacePrivateOfferPriceModel:
        """Test GcpMarketplacePrivateOfferPriceModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferPriceModel`
        """
        model = GcpMarketplacePrivateOfferPriceModel()
        if include_optional:
            return GcpMarketplacePrivateOfferPriceModel(
                base_offer = '',
                commitment = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_commitment.GcpMarketplacePrivateOfferPriceModelCommitment(
                    commitment_amount_per_period = {"nanos":1,"units":"units","currencyCode":"currencyCode"}, 
                    discount = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = suger_sdk_python.models.discount_percentage.discountPercentage(), 
                        discounted_price = suger_sdk_python.models.discounted_price.discountedPrice(), ), 
                    period = {"unit":"MONTHLY_PERIOD","count":5}, ),
                fixed_price = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_fixed.GcpMarketplacePrivateOfferPriceModelFixed(
                    discount = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = suger_sdk_python.models.discount_percentage.discountPercentage(), 
                        discounted_price = suger_sdk_python.models.discounted_price.discountedPrice(), ), 
                    period = {"unit":"MONTHLY_PERIOD","count":5}, ),
                one_time_credit = {"nanos":1,"units":"units","currencyCode":"currencyCode"},
                overage = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_overage.GcpMarketplacePrivateOfferPriceModelOverage(
                    discount = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = suger_sdk_python.models.discount_percentage.discountPercentage(), 
                        discounted_price = suger_sdk_python.models.discounted_price.discountedPrice(), ), 
                    sku_discounts = [
                        None
                        ], ),
                payg = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_payg.GcpMarketplacePrivateOfferPriceModelPayg(
                    discount = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = suger_sdk_python.models.discount_percentage.discountPercentage(), 
                        discounted_price = suger_sdk_python.models.discounted_price.discountedPrice(), ), 
                    sku_discounts = [
                        None
                        ], ),
                previous_credit_balance_policy = ''
            )
        else:
            return GcpMarketplacePrivateOfferPriceModel(
        )
        """

    def testGcpMarketplacePrivateOfferPriceModel(self):
        """Test GcpMarketplacePrivateOfferPriceModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
