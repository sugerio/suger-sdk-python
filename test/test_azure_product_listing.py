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

from openapi_client.models.azure_product_listing import \
    AzureProductListing  # noqa: E501


class TestAzureProductListing(unittest.TestCase):
    """AzureProductListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductListing:
        """Test AzureProductListing
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureProductListing`
        """
        model = AzureProductListing()  # noqa: E501
        if include_optional:
            return AzureProductListing(
                access_information = '',
                assets = [
                    openapi_client.models.azure_product_listing_asset.AzureProductListingAsset(
                        description = '', 
                        file_name = '', 
                        file_sas_uri = '', 
                        friendly_name = '', 
                        id = '', 
                        order = 56, 
                        publisher_defined_sas_uri = '', 
                        resource_type = 'ListingAsset', 
                        state = 'PendingUpload', 
                        type = '', )
                    ],
                compatible_products = [
                    ''
                    ],
                description = '',
                getting_started_instructions = '',
                id = '',
                keywords = [
                    ''
                    ],
                language_code = '',
                listing_contacts = [
                    openapi_client.models.azure_listing_contact.AzureListingContact(
                        email = '', 
                        name = '', 
                        phone = '', 
                        type = 'CustomerSupport', 
                        uri = '', )
                    ],
                listing_uris = [
                    openapi_client.models.azure_listing_uri.AzureListingUri(
                        display_text = '', 
                        subtype = '', 
                        type = '', 
                        uri = '', )
                    ],
                product_display_name = '',
                publisher_name = '',
                resource_type = 'AzureListing',
                short_description = '',
                summary = '',
                title = ''
            )
        else:
            return AzureProductListing(
        )
        """

    def testAzureProductListing(self):
        """Test AzureProductListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
