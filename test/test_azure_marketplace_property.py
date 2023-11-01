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

from openapi_client.models.azure_marketplace_property import \
    AzureMarketplaceProperty  # noqa: E501


class TestAzureMarketplaceProperty(unittest.TestCase):
    """AzureMarketplaceProperty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceProperty:
        """Test AzureMarketplaceProperty
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplaceProperty`
        """
        model = AzureMarketplaceProperty()  # noqa: E501
        if include_optional:
            return AzureMarketplaceProperty(
                var_schema = '',
                app_version = '',
                categories = {
                    'key' : [
                        ''
                        ]
                    },
                cloud_industries = {
                    'key' : [
                        ''
                        ]
                    },
                custom_amendments = [
                    openapi_client.models.azure_marketplace_custom_amendment.AzureMarketplaceCustomAmendment(
                        tenants = openapi_client.models.azure_marketplace_custom_amendment_tenant.AzureMarketplaceCustomAmendmentTenant(
                            manual_entries = [
                                openapi_client.models.azure_marketplace_custom_amendment_tenant_manual_entry.AzureMarketplaceCustomAmendmentTenantManualEntry(
                                    description = '', 
                                    id = '', )
                                ], ), 
                        terms = '', )
                    ],
                id = '',
                industries = {
                    'key' : [
                        ''
                        ]
                    },
                kind = 'azureSaaS',
                lifecycle_state = 'notAvailable',
                product = '',
                resource_name = '',
                standard_contract_amendment = '',
                terms_conditions = 'custom',
                terms_of_use = '',
                terms_of_use_url = '',
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
            return AzureMarketplaceProperty(
        )
        """

    def testAzureMarketplaceProperty(self):
        """Test AzureMarketplaceProperty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
