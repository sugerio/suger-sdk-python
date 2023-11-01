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

from openapi_client.models.azure_marketplace_private_offer_terms_doc import \
    AzureMarketplacePrivateOfferTermsDoc  # noqa: E501


class TestAzureMarketplacePrivateOfferTermsDoc(unittest.TestCase):
    """AzureMarketplacePrivateOfferTermsDoc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePrivateOfferTermsDoc:
        """Test AzureMarketplacePrivateOfferTermsDoc
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePrivateOfferTermsDoc`
        """
        model = AzureMarketplacePrivateOfferTermsDoc()  # noqa: E501
        if include_optional:
            return AzureMarketplacePrivateOfferTermsDoc(
                customer_facing_document_name = '',
                file_name = '',
                sas_url = ''
            )
        else:
            return AzureMarketplacePrivateOfferTermsDoc(
        )
        """

    def testAzureMarketplacePrivateOfferTermsDoc(self):
        """Test AzureMarketplacePrivateOfferTermsDoc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
