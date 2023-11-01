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

from openapi_client.models.azure_marketplace_private_offer import (
    AzureMarketplacePrivateOffer,
)  # noqa: E501


class TestAzureMarketplacePrivateOffer(unittest.TestCase):
    """AzureMarketplacePrivateOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePrivateOffer:
        """Test AzureMarketplacePrivateOffer
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePrivateOffer`
        """
        model = AzureMarketplacePrivateOffer()  # noqa: E501
        if include_optional:
            return AzureMarketplacePrivateOffer(
                var_schema = '',
                accept_by = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                acceptance_links = [
                    openapi_client.models.azure_marketplace_private_offer_acceptance_link.AzureMarketplacePrivateOfferAcceptanceLink(
                        beneficiary_id = '', 
                        link = '', )
                    ],
                beneficiaries = [
                    openapi_client.models.azure_marketplace_private_offer_beneficiary.AzureMarketplacePrivateOfferBeneficiary(
                        beneficiary_recipients = [
                            openapi_client.models.azure_marketplace_private_offer_beneficiary_recipient.AzureMarketplacePrivateOfferBeneficiaryRecipient(
                                id = '', 
                                recipient_type = 'cspCustomer', )
                            ], 
                        description = '', 
                        id = '', )
                    ],
                e_tag = '',
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                notification_contacts = [
                    ''
                    ],
                offer_pricing_type = '',
                partners = [
                    openapi_client.models.azure_marketplace_private_offer_partner.AzureMarketplacePrivateOfferPartner(
                        id = '', 
                        location = '', 
                        partner_name = '', )
                    ],
                prepared_by = '',
                pricing = [
                    openapi_client.models.azure_marketplace_private_offer_pricing.AzureMarketplacePrivateOfferPricing(
                        discount_percentage = 1.337, 
                        discount_type = 'absolute', 
                        markup_percentage = 1.337, 
                        original_plan = openapi_client.models.original_plan.originalPlan(), 
                        plan = '', 
                        plan_id = '', 
                        plan_name = '', 
                        plan_type = 'FLAT_RATE', 
                        price_details = '', 
                        private_offer_plan = openapi_client.models.private_offer_plan.privateOfferPlan(), 
                        product = '', 
                        product_name = '', 
                        suger_offer_id = '', )
                    ],
                private_offer_type = '',
                resource_name = '',
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state = 'draft',
                sub_state = 'pendingAcceptance',
                terms_and_conditions_doc_sas_url = '',
                terms_and_conditions_docs = [
                    openapi_client.models.azure_marketplace_private_offer_terms_doc.AzureMarketplacePrivateOfferTermsDoc(
                        customer_facing_document_name = '', 
                        file_name = '', 
                        sas_url = '', )
                    ],
                upgraded_from = openapi_client.models.azure_marketplace_private_offer_promotion_reference.AzureMarketplacePrivateOfferPromotionReference(
                    id = '', 
                    name = '', ),
                validations = [
                    openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                        __schema = '', 
                        code = 'businessValidationError', 
                        level = 'informational', 
                        message = '', 
                        resource_id = '', )
                    ],
                variable_start_date = True
            )
        else:
            return AzureMarketplacePrivateOffer(
        )
        """

    def testAzureMarketplacePrivateOffer(self):
        """Test AzureMarketplacePrivateOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()