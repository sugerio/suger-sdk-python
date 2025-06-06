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

from suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_event_ok_response import GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse

class TestGithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse(unittest.TestCase):
    """GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse:
        """Test GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse`
        """
        model = GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse()
        if include_optional:
            return GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse(
                dimension = '',
                effective_start_time = '',
                message_time = '',
                plan_id = '',
                quantity = 1.337,
                resource_id = '',
                resource_uri = '',
                status = 'Accepted',
                usage_event_id = ''
            )
        else:
            return GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse(
        )
        """

    def testGithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse(self):
        """Test GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventOkResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
