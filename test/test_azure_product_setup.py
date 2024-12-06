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

from suger_sdk_python.models.azure_product_setup import AzureProductSetup

class TestAzureProductSetup(unittest.TestCase):
    """AzureProductSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductSetup:
        """Test AzureProductSetup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureProductSetup`
        """
        model = AzureProductSetup()
        if include_optional:
            return AzureProductSetup(
                call_to_action = 'free',
                channel_states = [
                    {"type":"type","value":"value"}
                    ],
                enable_test_drive = True,
                resource_type = 'AzureProductSetup',
                selling_option = 'ListingOnly',
                test_drive_type = '',
                trial_uri = ''
            )
        else:
            return AzureProductSetup(
        )
        """

    def testAzureProductSetup(self):
        """Test AzureProductSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
