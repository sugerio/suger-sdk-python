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


from openapi_client.models.azure_marketplace_reseller import (
    AzureMarketplaceReseller,
)  # noqa: E501


class TestAzureMarketplaceReseller(unittest.TestCase):
    """AzureMarketplaceReseller unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceReseller:
        """Test AzureMarketplaceReseller
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplaceReseller`
        """
        model = AzureMarketplaceReseller()  # noqa: E501
        if include_optional:
            return AzureMarketplaceReseller(
                var_schema = '',
                id = '',
                preview_audiences = [
                    openapi_client.models.azure_marketplace_preview_audience.AzureMarketplacePreviewAudience(
                        description = '', 
                        resource_id = '', 
                        type = 'subscription', )
                    ],
                product = '',
                reseller_channel_state = 'noSet',
                resource_name = '',
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
            return AzureMarketplaceReseller(
        )
        """

    def testAzureMarketplaceReseller(self):
        """Test AzureMarketplaceReseller"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
