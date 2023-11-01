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

from openapi_client.models.gcp_marketplace_document import (
    GcpMarketplaceDocument,
)  # noqa: E501


class TestGcpMarketplaceDocument(unittest.TestCase):
    """GcpMarketplaceDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceDocument:
        """Test GcpMarketplaceDocument
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplaceDocument`
        """
        model = GcpMarketplaceDocument()  # noqa: E501
        if include_optional:
            return GcpMarketplaceDocument(
                description = '',
                document_type = '',
                external_google_link = openapi_client.models.gcp_marketplace_external_google_link.GcpMarketplaceExternalGoogleLink(
                    uri = '', ),
                name = '',
                unstructured_document = openapi_client.models.gcp_marketplace_unstructured_document.GcpMarketplaceUnstructuredDocument(
                    content = '', ),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GcpMarketplaceDocument(
        )
        """

    def testGcpMarketplaceDocument(self):
        """Test GcpMarketplaceDocument"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
