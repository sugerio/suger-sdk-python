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


from openapi_client.models.azure_marketplace_private_offer_beneficiary import (
    AzureMarketplacePrivateOfferBeneficiary,
)  # noqa: E501


class TestAzureMarketplacePrivateOfferBeneficiary(unittest.TestCase):
    """AzureMarketplacePrivateOfferBeneficiary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AzureMarketplacePrivateOfferBeneficiary:
        """Test AzureMarketplacePrivateOfferBeneficiary
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePrivateOfferBeneficiary`
        """
        model = AzureMarketplacePrivateOfferBeneficiary()  # noqa: E501
        if include_optional:
            return AzureMarketplacePrivateOfferBeneficiary(
                beneficiary_recipients = [
                    openapi_client.models.azure_marketplace_private_offer_beneficiary_recipient.AzureMarketplacePrivateOfferBeneficiaryRecipient(
                        id = '', 
                        recipient_type = 'cspCustomer', )
                    ],
                description = '',
                id = ''
            )
        else:
            return AzureMarketplacePrivateOfferBeneficiary(
        )
        """

    def testAzureMarketplacePrivateOfferBeneficiary(self):
        """Test AzureMarketplacePrivateOfferBeneficiary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
