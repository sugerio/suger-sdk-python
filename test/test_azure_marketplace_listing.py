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

from openapi_client.models.azure_marketplace_listing import \
    AzureMarketplaceListing  # noqa: E501


class TestAzureMarketplaceListing(unittest.TestCase):
    """AzureMarketplaceListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceListing:
        """Test AzureMarketplaceListing
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplaceListing`
        """
        model = AzureMarketplaceListing()  # noqa: E501
        if include_optional:
            return AzureMarketplaceListing(
                var_schema = '',
                cloud_solution_provider_contact = openapi_client.models.azure_marketplace_contact.AzureMarketplaceContact(
                    email = '', 
                    name = '', 
                    phone = '', 
                    url = '', ),
                cloud_solution_provider_marketing_materials = '',
                description = '',
                engineering_contact = openapi_client.models.azure_marketplace_contact.AzureMarketplaceContact(
                    email = '', 
                    name = '', 
                    phone = '', 
                    url = '', ),
                general_links = [
                    openapi_client.models.azure_marketplace_general_link.AzureMarketplaceGeneralLink(
                        display_text = '', 
                        link = '', )
                    ],
                getting_started_instructions = '',
                gloabal_support_website = '',
                government_support_website = '',
                id = '',
                kind = 'azureSaaS',
                language_id = '',
                lifecycle_state = 'notAvailable',
                privacy_policy_link = '',
                product = '',
                resource_name = '',
                search_keywords = [
                    ''
                    ],
                search_result_summary = '',
                short_description = '',
                support_contact = openapi_client.models.azure_marketplace_contact.AzureMarketplaceContact(
                    email = '', 
                    name = '', 
                    phone = '', 
                    url = '', ),
                title = '',
                validations = [
                    openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                        __schema = '', 
                        code = 'businessValidationError', 
                        level = 'informational', 
                        message = '', 
                        resource_id = '', )
                    ]
            )
        else:
            return AzureMarketplaceListing(
        )
        """

    def testAzureMarketplaceListing(self):
        """Test AzureMarketplaceListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
