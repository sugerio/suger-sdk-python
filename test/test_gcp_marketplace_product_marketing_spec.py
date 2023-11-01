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

from openapi_client.models.gcp_marketplace_product_marketing_spec import (
    GcpMarketplaceProductMarketingSpec,
)  # noqa: E501


class TestGcpMarketplaceProductMarketingSpec(unittest.TestCase):
    """GcpMarketplaceProductMarketingSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProductMarketingSpec:
        """Test GcpMarketplaceProductMarketingSpec
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplaceProductMarketingSpec`
        """
        model = GcpMarketplaceProductMarketingSpec()  # noqa: E501
        if include_optional:
            return GcpMarketplaceProductMarketingSpec(
                description = '',
                display_names = [
                    ''
                    ],
                documentation_specs = [
                    openapi_client.models.gcp_marketplace_product_documentation_spec.GcpMarketplaceProductDocumentationSpec(
                        description = '', 
                        title = '', 
                        uri = '', )
                    ],
                eula_url = '',
                external_license_specs = [
                    openapi_client.models.gcp_marketplace_product_license_spec.GcpMarketplaceProductLicenseSpec(
                        description = '', 
                        uri = '', )
                    ],
                external_marketing_url = '',
                icon = '',
                search_categories = [
                    ''
                    ],
                search_description = '',
                search_keywords = [
                    ''
                    ],
                signup_uri = '',
                support_spec = openapi_client.models.gcp_marketplace_product_support_spec.GcpMarketplaceProductSupportSpec(
                    description = '', 
                    email = '', 
                    uri = '', ),
                tag_line = '',
                title = ''
            )
        else:
            return GcpMarketplaceProductMarketingSpec(
        )
        """

    def testGcpMarketplaceProductMarketingSpec(self):
        """Test GcpMarketplaceProductMarketingSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
