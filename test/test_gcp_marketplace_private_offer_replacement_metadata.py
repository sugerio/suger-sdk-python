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

from openapi_client.models.gcp_marketplace_private_offer_replacement_metadata import (
    GcpMarketplacePrivateOfferReplacementMetadata,
)  # noqa: E501


class TestGcpMarketplacePrivateOfferReplacementMetadata(unittest.TestCase):
    """GcpMarketplacePrivateOfferReplacementMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GcpMarketplacePrivateOfferReplacementMetadata:
        """Test GcpMarketplacePrivateOfferReplacementMetadata
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferReplacementMetadata`
        """
        model = GcpMarketplacePrivateOfferReplacementMetadata()  # noqa: E501
        if include_optional:
            return GcpMarketplacePrivateOfferReplacementMetadata(
                coterm_alignment = '',
                replaced_offer = '',
                replaced_offer_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                replacement_policy = ''
            )
        else:
            return GcpMarketplacePrivateOfferReplacementMetadata(
        )
        """

    def testGcpMarketplacePrivateOfferReplacementMetadata(self):
        """Test GcpMarketplacePrivateOfferReplacementMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
