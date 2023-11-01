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

from openapi_client.models.azure_integration import AzureIntegration  # noqa: E501


class TestAzureIntegration(unittest.TestCase):
    """AzureIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureIntegration:
        """Test AzureIntegration
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureIntegration`
        """
        model = AzureIntegration()  # noqa: E501
        if include_optional:
            return AzureIntegration(
                cma_full_sync_done = True,
                credential = openapi_client.models.azure_integration_credential.AzureIntegrationCredential(
                    access_token = '', 
                    client_id = '', 
                    client_secret = '', 
                    expires_on = '', 
                    refresh_token = '', 
                    tenant_id = '', 
                    token_scope = '', 
                    token_type = '', ),
                partner_center_referral_sync_paused = True,
                revenue_record_full_sync_done = True,
                secret_key = ''
            )
        else:
            return AzureIntegration(
        )
        """

    def testAzureIntegration(self):
        """Test AzureIntegration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()