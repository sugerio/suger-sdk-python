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

from openapi_client.models.microsoft_partner_referral_requirements import MicrosoftPartnerReferralRequirements  # noqa: E501

class TestMicrosoftPartnerReferralRequirements(unittest.TestCase):
    """MicrosoftPartnerReferralRequirements unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftPartnerReferralRequirements:
        """Test MicrosoftPartnerReferralRequirements
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrosoftPartnerReferralRequirements`
        """
        model = MicrosoftPartnerReferralRequirements()  # noqa: E501
        if include_optional:
            return MicrosoftPartnerReferralRequirements(
                additional_requirements = openapi_client.models.microsoft_partner_referral_additional_requirements.MicrosoftPartnerReferralAdditionalRequirements(
                    attributes = [
                        openapi_client.models.microsoft_partner_referral_requirement_attribute.MicrosoftPartnerReferralRequirementAttribute(
                            id = '', 
                            type = '', )
                        ], 
                    iot = openapi_client.models.microsoft_partner_referral_iot.MicrosoftPartnerReferralIot(
                        attach_services = True, 
                        azure_certified_device = True, 
                        customer_license_agreement_number = openapi_client.models.customer_license_agreement_number.customerLicenseAgreementNumber(), 
                        device_category = openapi_client.models.device_category.deviceCategory(), 
                        silicon_type = openapi_client.models.silicon_type.siliconType(), ), ),
                industries = [
                    openapi_client.models.microsoft_partner_referral_tag.MicrosoftPartnerReferralTag(
                        id = '', )
                    ],
                offers = [
                    openapi_client.models.microsoft_partner_referral_tag.MicrosoftPartnerReferralTag(
                        id = '', )
                    ],
                products = [
                    openapi_client.models.microsoft_partner_referral_tag.MicrosoftPartnerReferralTag(
                        id = '', )
                    ],
                sales_plays = [
                    openapi_client.models.microsoft_partner_referral_tag.MicrosoftPartnerReferralTag(
                        id = '', )
                    ],
                services = [
                    openapi_client.models.microsoft_partner_referral_tag.MicrosoftPartnerReferralTag(
                        id = '', )
                    ],
                solutions = [
                    openapi_client.models.microsoft_partner_referral_solution.MicrosoftPartnerReferralSolution(
                        closing_date_time = openapi_client.models.closing_date_time.closingDateTime(), 
                        currency = openapi_client.models.currency.currency(), 
                        id = '', 
                        name = '', 
                        price = openapi_client.models.price.price(), 
                        publisher_name = '', 
                        quantity = openapi_client.models.quantity.quantity(), 
                        solution_type = '', 
                        type = '', )
                    ]
            )
        else:
            return MicrosoftPartnerReferralRequirements(
        )
        """

    def testMicrosoftPartnerReferralRequirements(self):
        """Test MicrosoftPartnerReferralRequirements"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
