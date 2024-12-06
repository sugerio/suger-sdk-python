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

from suger_sdk_python.models.azure_marketplace_submission import AzureMarketplaceSubmission

class TestAzureMarketplaceSubmission(unittest.TestCase):
    """AzureMarketplaceSubmission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceSubmission:
        """Test AzureMarketplaceSubmission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplaceSubmission`
        """
        model = AzureMarketplaceSubmission()
        if include_optional:
            return AzureMarketplaceSubmission(
                var_schema = '',
                created = '',
                deprecation_schedule = {"date":"date","reason":"criticalSecurityIssue","$schema":"$schema","alternative":{"product":"{}","plan":"{}"},"dateOffset":"dateOffset"},
                id = '',
                lifecycle_state = 'notAvailable',
                product = '',
                resource_name = '',
                result = 'succeeded',
                status = 'notStarted',
                target = {"targetId":"targetId","targetType":"flight"},
                validations = [
                    {"resourceId":"resourceId","code":"businessValidationError","$schema":"$schema","level":"informational","message":"message"}
                    ]
            )
        else:
            return AzureMarketplaceSubmission(
        )
        """

    def testAzureMarketplaceSubmission(self):
        """Test AzureMarketplaceSubmission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
