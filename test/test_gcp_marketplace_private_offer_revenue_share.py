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

from suger_sdk_python.models.gcp_marketplace_private_offer_revenue_share import GcpMarketplacePrivateOfferRevenueShare

class TestGcpMarketplacePrivateOfferRevenueShare(unittest.TestCase):
    """GcpMarketplacePrivateOfferRevenueShare unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplacePrivateOfferRevenueShare:
        """Test GcpMarketplacePrivateOfferRevenueShare
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferRevenueShare`
        """
        model = GcpMarketplacePrivateOfferRevenueShare()
        if include_optional:
            return GcpMarketplacePrivateOfferRevenueShare(
                auto_renew_revenue_share = suger_sdk_python.models.gcp_marketplace_revenue_share_value.GcpMarketplaceRevenueShareValue(
                    value = '', ),
                revenue_share = suger_sdk_python.models.gcp_marketplace_revenue_share_value.GcpMarketplaceRevenueShareValue(
                    value = '', ),
                revenue_share_changes = [
                    suger_sdk_python.models.gcp_marketplace_revenue_share_change.GcpMarketplaceRevenueShareChange(
                        revenue_share = suger_sdk_python.models.gcp_marketplace_revenue_share_value.GcpMarketplaceRevenueShareValue(
                            value = '', ), 
                        revenue_share_type = 'AUTOMATIC', 
                        start_time = '', )
                    ]
            )
        else:
            return GcpMarketplacePrivateOfferRevenueShare(
        )
        """

    def testGcpMarketplacePrivateOfferRevenueShare(self):
        """Test GcpMarketplacePrivateOfferRevenueShare"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
