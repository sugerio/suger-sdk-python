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

from openapi_client.models.gcp_marketplace_private_offer_migration_metadata import (
    GcpMarketplacePrivateOfferMigrationMetadata,
)  # noqa: E501


class TestGcpMarketplacePrivateOfferMigrationMetadata(unittest.TestCase):
    """GcpMarketplacePrivateOfferMigrationMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GcpMarketplacePrivateOfferMigrationMetadata:
        """Test GcpMarketplacePrivateOfferMigrationMetadata
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferMigrationMetadata`
        """
        model = GcpMarketplacePrivateOfferMigrationMetadata()  # noqa: E501
        if include_optional:
            return GcpMarketplacePrivateOfferMigrationMetadata(
                inventory_flavor_external_name = '',
                product_external_name = '',
                provider_id = ''
            )
        else:
            return GcpMarketplacePrivateOfferMigrationMetadata(
        )
        """

    def testGcpMarketplacePrivateOfferMigrationMetadata(self):
        """Test GcpMarketplacePrivateOfferMigrationMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
