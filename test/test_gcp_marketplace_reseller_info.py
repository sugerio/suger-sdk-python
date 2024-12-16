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

from suger_sdk_python.models.gcp_marketplace_reseller_info import GcpMarketplaceResellerInfo

class TestGcpMarketplaceResellerInfo(unittest.TestCase):
    """GcpMarketplaceResellerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceResellerInfo:
        """Test GcpMarketplaceResellerInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceResellerInfo`
        """
        model = GcpMarketplaceResellerInfo()
        if include_optional:
            return GcpMarketplaceResellerInfo(
                billing_account_id = '',
                billing_account_nickname = '',
                billing_account_org_display_name = '',
                billing_account_type = '',
                notes_to_reseller = ''
            )
        else:
            return GcpMarketplaceResellerInfo(
        )
        """

    def testGcpMarketplaceResellerInfo(self):
        """Test GcpMarketplaceResellerInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()