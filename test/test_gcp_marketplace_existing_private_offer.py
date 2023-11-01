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

from openapi_client.models.gcp_marketplace_existing_private_offer import (
    GcpMarketplaceExistingPrivateOffer,
)  # noqa: E501


class TestGcpMarketplaceExistingPrivateOffer(unittest.TestCase):
    """GcpMarketplaceExistingPrivateOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceExistingPrivateOffer:
        """Test GcpMarketplaceExistingPrivateOffer
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplaceExistingPrivateOffer`
        """
        model = GcpMarketplaceExistingPrivateOffer()  # noqa: E501
        if include_optional:
            return GcpMarketplaceExistingPrivateOffer(
                agreement = '',
                custom_eula = openapi_client.models.gcp_marketplace_document.GcpMarketplaceDocument(
                    description = '', 
                    document_type = '', 
                    external_google_link = openapi_client.models.external_google_link.externalGoogleLink(), 
                    name = '', 
                    unstructured_document = openapi_client.models.gcp_marketplace_unstructured_document.GcpMarketplaceUnstructuredDocument(
                        content = '', ), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                installment_timeline = openapi_client.models.gcp_marketplace_private_offer_installment_timeline.GcpMarketplacePrivateOfferInstallmentTimeline(
                    installments = [
                        openapi_client.models.gcp_marketplace_private_offer_installment.GcpMarketplacePrivateOfferInstallment(
                            price_model = openapi_client.models.gcp_marketplace_private_offer_price_model.GcpMarketplacePrivateOfferPriceModel(
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
                                fixed_price = openapi_client.models.gcp_marketplace_private_offer_price_model_fixed.GcpMarketplacePrivateOfferPriceModelFixed(), 
                                one_time_credit = openapi_client.models.one_time_credit.oneTimeCredit(), 
                                overage = openapi_client.models.gcp_marketplace_private_offer_price_model_overage.GcpMarketplacePrivateOfferPriceModelOverage(
                                    sku_discounts = [
                                        None
                                        ], ), 
                                payg = openapi_client.models.payg.payg(), 
                                previous_credit_balance_policy = '', ), 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                name = '',
                offer_term = openapi_client.models.gcp_marketplace_private_offer_term.GcpMarketplacePrivateOfferTerm(
                    enable_scheduled_start_times = True, 
                    end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_policy = '', 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    term_duration = openapi_client.models.gcp_period_duration.GcpPeriodDuration(
                        count = 56, 
                        unit = 'MONTHLY_PERIOD', ), ),
                payment_schedule = '',
                price_model = openapi_client.models.gcp_marketplace_private_offer_price_model.GcpMarketplacePrivateOfferPriceModel(
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
                    fixed_price = openapi_client.models.gcp_marketplace_private_offer_price_model_fixed.GcpMarketplacePrivateOfferPriceModelFixed(), 
                    one_time_credit = openapi_client.models.one_time_credit.oneTimeCredit(), 
                    overage = openapi_client.models.gcp_marketplace_private_offer_price_model_overage.GcpMarketplacePrivateOfferPriceModelOverage(
                        sku_discounts = [
                            None
                            ], ), 
                    payg = openapi_client.models.payg.payg(), 
                    previous_credit_balance_policy = '', ),
                service_level = ''
            )
        else:
            return GcpMarketplaceExistingPrivateOffer(
        )
        """

    def testGcpMarketplaceExistingPrivateOffer(self):
        """Test GcpMarketplaceExistingPrivateOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()