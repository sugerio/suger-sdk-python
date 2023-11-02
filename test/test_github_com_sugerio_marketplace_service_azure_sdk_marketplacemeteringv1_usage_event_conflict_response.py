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

from openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_conflict_response import GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse  # noqa: E501

class TestGithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse(unittest.TestCase):
    """GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse:
        """Test GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse`
        """
        model = GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse()  # noqa: E501
        if include_optional:
            return GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse(
                additional_info = openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1/usage_event_conflict_response_additional_info.github_com_sugerio_marketplace-service_azure_sdk_marketplacemeteringv1.UsageEventConflictResponseAdditionalInfo(
                    accepted_message = openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1/usage_event_ok_response.github_com_sugerio_marketplace-service_azure_sdk_marketplacemeteringv1.UsageEventOkResponse(
                        dimension = '', 
                        effective_start_time = '', 
                        message_time = '', 
                        plan_id = '', 
                        quantity = 1.337, 
                        resource_id = '', 
                        resource_uri = '', 
                        status = openapi_client.models.status.status(), 
                        usage_event_id = '', ), ),
                code = '',
                message = ''
            )
        else:
            return GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse(
        )
        """

    def testGithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse(self):
        """Test GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
