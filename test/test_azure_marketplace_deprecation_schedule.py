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

from openapi_client.models.azure_marketplace_deprecation_schedule import AzureMarketplaceDeprecationSchedule  # noqa: E501

class TestAzureMarketplaceDeprecationSchedule(unittest.TestCase):
    """AzureMarketplaceDeprecationSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceDeprecationSchedule:
        """Test AzureMarketplaceDeprecationSchedule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplaceDeprecationSchedule`
        """
        model = AzureMarketplaceDeprecationSchedule()  # noqa: E501
        if include_optional:
            return AzureMarketplaceDeprecationSchedule(
                var_schema = '',
                alternative = openapi_client.models.azure_marketplace_deprecation_schedule_alternative.AzureMarketplaceDeprecationScheduleAlternative(
                    plan = openapi_client.models.plan.plan(), 
                    product = openapi_client.models.product.product(), ),
                var_date = '',
                date_offset = '',
                reason = 'criticalSecurityIssue'
            )
        else:
            return AzureMarketplaceDeprecationSchedule(
        )
        """

    def testAzureMarketplaceDeprecationSchedule(self):
        """Test AzureMarketplaceDeprecationSchedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
