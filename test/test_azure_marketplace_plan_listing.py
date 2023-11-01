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

from openapi_client.models.azure_marketplace_plan_listing import (
    AzureMarketplacePlanListing,
)  # noqa: E501


class TestAzureMarketplacePlanListing(unittest.TestCase):
    """AzureMarketplacePlanListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePlanListing:
        """Test AzureMarketplacePlanListing
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePlanListing`
        """
        model = AzureMarketplacePlanListing()  # noqa: E501
        if include_optional:
            return AzureMarketplacePlanListing(
                var_schema = '',
                description = '',
                id = '',
                kind = 'azureVM-plan',
                language_id = '',
                lifecycle_state = 'notAvailable',
                name = '',
                plan = '',
                product = '',
                resource_name = '',
                summary = '',
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
            return AzureMarketplacePlanListing(
        )
        """

    def testAzureMarketplacePlanListing(self):
        """Test AzureMarketplacePlanListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()