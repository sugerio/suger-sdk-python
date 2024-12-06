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

from suger_sdk_python.models.aws_marketplace_cppo_opportunity_term import AwsMarketplaceCppoOpportunityTerm

class TestAwsMarketplaceCppoOpportunityTerm(unittest.TestCase):
    """AwsMarketplaceCppoOpportunityTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceCppoOpportunityTerm:
        """Test AwsMarketplaceCppoOpportunityTerm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsMarketplaceCppoOpportunityTerm`
        """
        model = AwsMarketplaceCppoOpportunityTerm()
        if include_optional:
            return AwsMarketplaceCppoOpportunityTerm(
                currency_code = '',
                documents = [
                    suger_sdk_python.models.aws_marketplace_catalog_legal_term_document.AwsMarketplaceCatalogLegalTermDocument(
                        type = 'CustomEula', 
                        url = '', 
                        version = '', )
                    ],
                duration = '',
                grants = [
                    suger_sdk_python.models.aws_marketplace_cppo_opportunity_upfront_price_grant.AwsMarketplaceCppoOpportunityUpfrontPriceGrant(
                        dimension_key = '', 
                        max_quantity = 56, )
                    ],
                id = '',
                maximum_agreement_start_date = '',
                positive_targeting = suger_sdk_python.models.aws_marketplace_cppo_opportunity_positive_targeting.AwsMarketplaceCppoOpportunityPositiveTargeting(
                    buyer_accounts = [
                        suger_sdk_python.models.aws_marketplace_buyer_account.AwsMarketplaceBuyerAccount(
                            aws_account_id = '', )
                        ], 
                    country_codes = [
                        ''
                        ], ),
                price = '',
                rate_cards = [
                    suger_sdk_python.models.aws_marketplace_catalog_pricing_term_rate_card.AwsMarketplaceCatalogPricingTermRateCard(
                        constraints = suger_sdk_python.models.constraints.Constraints(), 
                        rate_card = [
                            suger_sdk_python.models.aws_marketplace_catalog_pricing_term_rate_card_item.AwsMarketplaceCatalogPricingTermRateCardItem(
                                description = '', 
                                dimension_key = '', 
                                display_name = '', 
                                price = '', 
                                quantity = '', 
                                unit = '', )
                            ], 
                        selector = suger_sdk_python.models.selector.Selector(), )
                    ],
                schedule = [
                    suger_sdk_python.models.aws_marketplace_cppo_opportunity_payment_schedule.AwsMarketplaceCppoOpportunityPaymentSchedule(
                        charge_amount = '', 
                        charge_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                type = 'BuyerTargetingTerm'
            )
        else:
            return AwsMarketplaceCppoOpportunityTerm(
        )
        """

    def testAwsMarketplaceCppoOpportunityTerm(self):
        """Test AwsMarketplaceCppoOpportunityTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
