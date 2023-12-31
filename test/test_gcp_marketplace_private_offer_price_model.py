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

from openapi_client.models.gcp_marketplace_private_offer_price_model import GcpMarketplacePrivateOfferPriceModel  # noqa: E501

class TestGcpMarketplacePrivateOfferPriceModel(unittest.TestCase):
    """GcpMarketplacePrivateOfferPriceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplacePrivateOfferPriceModel:
        """Test GcpMarketplacePrivateOfferPriceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferPriceModel`
        """
        model = GcpMarketplacePrivateOfferPriceModel()  # noqa: E501
        if include_optional:
            return GcpMarketplacePrivateOfferPriceModel(
                base_offer = '',
                commitment = openapi_client.models.gcp_marketplace_private_offer_price_model_commitment.GcpMarketplacePrivateOfferPriceModelCommitment(
                    commitment_amount_per_period = openapi_client.models.gcp_price_value.GcpPriceValue(
                        currency_code = '', 
                        nanos = 56, 
                        units = '', ), 
                    discount = openapi_client.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = openapi_client.models.discount_percentage.discountPercentage(), 
                        discounted_price = openapi_client.models.discounted_price.discountedPrice(), ), 
                    period = openapi_client.models.gcp_period_duration.GcpPeriodDuration(
                        count = 56, 
                        unit = 'MONTHLY_PERIOD', ), ),
                fixed_price = openapi_client.models.gcp_marketplace_private_offer_price_model_fixed.GcpMarketplacePrivateOfferPriceModelFixed(
                    discount = openapi_client.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = openapi_client.models.discount_percentage.discountPercentage(), 
                        discounted_price = openapi_client.models.discounted_price.discountedPrice(), ), 
                    period = openapi_client.models.gcp_period_duration.GcpPeriodDuration(
                        count = 56, 
                        unit = 'MONTHLY_PERIOD', ), ),
                one_time_credit = openapi_client.models.gcp_price_value.GcpPriceValue(
                    currency_code = '', 
                    nanos = 56, 
                    units = '', ),
                overage = openapi_client.models.gcp_marketplace_private_offer_price_model_overage.GcpMarketplacePrivateOfferPriceModelOverage(
                    discount = openapi_client.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = openapi_client.models.discount_percentage.discountPercentage(), 
                        discounted_price = openapi_client.models.discounted_price.discountedPrice(), ), 
                    sku_discounts = [
                        None
                        ], ),
                payg = openapi_client.models.gcp_marketplace_private_offer_price_model_payg.GcpMarketplacePrivateOfferPriceModelPayg(
                    discount = openapi_client.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                        discount_percentage = openapi_client.models.discount_percentage.discountPercentage(), 
                        discounted_price = openapi_client.models.discounted_price.discountedPrice(), ), 
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
