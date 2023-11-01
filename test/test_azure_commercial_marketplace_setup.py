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

from openapi_client.models.azure_commercial_marketplace_setup import \
    AzureCommercialMarketplaceSetup  # noqa: E501


class TestAzureCommercialMarketplaceSetup(unittest.TestCase):
    """AzureCommercialMarketplaceSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureCommercialMarketplaceSetup:
        """Test AzureCommercialMarketplaceSetup
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureCommercialMarketplaceSetup`
        """
        model = AzureCommercialMarketplaceSetup()  # noqa: E501
        if include_optional:
            return AzureCommercialMarketplaceSetup(
                var_schema = '',
                access_url = '',
                call_to_action = 'free',
                id = '',
                product = '',
                require_license_for_install = True,
                resource_name = '',
                sell_through_microsoft = True,
                use_microsoft_license_management_service = True,
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
            return AzureCommercialMarketplaceSetup(
        )
        """

    def testAzureCommercialMarketplaceSetup(self):
        """Test AzureCommercialMarketplaceSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
