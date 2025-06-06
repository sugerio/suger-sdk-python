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

from suger_sdk_python.models.gcp_marketplace_private_offer_installment_timeline import GcpMarketplacePrivateOfferInstallmentTimeline

class TestGcpMarketplacePrivateOfferInstallmentTimeline(unittest.TestCase):
    """GcpMarketplacePrivateOfferInstallmentTimeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplacePrivateOfferInstallmentTimeline:
        """Test GcpMarketplacePrivateOfferInstallmentTimeline
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferInstallmentTimeline`
        """
        model = GcpMarketplacePrivateOfferInstallmentTimeline()
        if include_optional:
            return GcpMarketplacePrivateOfferInstallmentTimeline(
                installments = [
                    suger_sdk_python.models.gcp_marketplace_private_offer_installment.GcpMarketplacePrivateOfferInstallment(
                        price_model = suger_sdk_python.models.gcp_marketplace_private_offer_price_model.GcpMarketplacePrivateOfferPriceModel(
                            base_offer = '', 
                            commitment = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_commitment.GcpMarketplacePrivateOfferPriceModelCommitment(
                                commitment_amount_per_period = {"nanos":1,"units":"units","currencyCode":"currencyCode"}, 
                                discount = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                                    discount_percentage = suger_sdk_python.models.discount_percentage.discountPercentage(), 
                                    discounted_price = suger_sdk_python.models.discounted_price.discountedPrice(), ), 
                                period = {"unit":"MONTHLY_PERIOD","count":5}, ), 
                            fixed_price = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_fixed.GcpMarketplacePrivateOfferPriceModelFixed(), 
                            one_time_credit = suger_sdk_python.models.one_time_credit.oneTimeCredit(), 
                            overage = suger_sdk_python.models.gcp_marketplace_private_offer_price_model_overage.GcpMarketplacePrivateOfferPriceModelOverage(
                                sku_discounts = [
                                    None
                                    ], ), 
                            payg = suger_sdk_python.models.payg.payg(), 
                            previous_credit_balance_policy = '', ), 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GcpMarketplacePrivateOfferInstallmentTimeline(
        )
        """

    def testGcpMarketplacePrivateOfferInstallmentTimeline(self):
        """Test GcpMarketplacePrivateOfferInstallmentTimeline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
