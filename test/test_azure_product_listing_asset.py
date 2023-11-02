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

from openapi_client.models.azure_product_listing_asset import AzureProductListingAsset  # noqa: E501

class TestAzureProductListingAsset(unittest.TestCase):
    """AzureProductListingAsset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductListingAsset:
        """Test AzureProductListingAsset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureProductListingAsset`
        """
        model = AzureProductListingAsset()  # noqa: E501
        if include_optional:
            return AzureProductListingAsset(
                description = '',
                file_name = '',
                file_sas_uri = '',
                friendly_name = '',
                id = '',
                order = 56,
                publisher_defined_sas_uri = '',
                resource_type = 'ListingAsset',
                state = 'PendingUpload',
                type = ''
            )
        else:
            return AzureProductListingAsset(
        )
        """

    def testAzureProductListingAsset(self):
        """Test AzureProductListingAsset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
