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

from suger_sdk_python.models.gcp_marketplace_private_offer_metric_detail import GcpMarketplacePrivateOfferMetricDetail

class TestGcpMarketplacePrivateOfferMetricDetail(unittest.TestCase):
    """GcpMarketplacePrivateOfferMetricDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplacePrivateOfferMetricDetail:
        """Test GcpMarketplacePrivateOfferMetricDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferMetricDetail`
        """
        model = GcpMarketplacePrivateOfferMetricDetail()
        if include_optional:
            return GcpMarketplacePrivateOfferMetricDetail(
                display_name = '',
                parent_commerce_service = '',
                sku_id = '',
                tiers = [
                    {"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":1.2315135367772556}
                    ],
                unit_description = ''
            )
        else:
            return GcpMarketplacePrivateOfferMetricDetail(
        )
        """

    def testGcpMarketplacePrivateOfferMetricDetail(self):
        """Test GcpMarketplacePrivateOfferMetricDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
