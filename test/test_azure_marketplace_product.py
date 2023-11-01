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


from openapi_client.models.azure_marketplace_product import (
    AzureMarketplaceProduct,
)  # noqa: E501


class TestAzureMarketplaceProduct(unittest.TestCase):
    """AzureMarketplaceProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceProduct:
        """Test AzureMarketplaceProduct
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplaceProduct`
        """
        model = AzureMarketplaceProduct()  # noqa: E501
        if include_optional:
            return AzureMarketplaceProduct(
                var_schema = '',
                alias = '',
                id = '',
                identity = openapi_client.models.azure_marketplace_identity.AzureMarketplaceIdentity(
                    external_id = '', ),
                lifecycle_state = 'notAvailable',
                product_group = '',
                resource_name = '',
                type = 'azureApplication',
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
            return AzureMarketplaceProduct(
        )
        """

    def testAzureMarketplaceProduct(self):
        """Test AzureMarketplaceProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
