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

from openapi_client.models.salesforce_crm_credential import SalesforceCrmCredential  # noqa: E501

class TestSalesforceCrmCredential(unittest.TestCase):
    """SalesforceCrmCredential unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SalesforceCrmCredential:
        """Test SalesforceCrmCredential
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SalesforceCrmCredential`
        """
        model = SalesforceCrmCredential()  # noqa: E501
        if include_optional:
            return SalesforceCrmCredential(
                access_token = '',
                client_id = '',
                client_secret = '',
                exp = 56,
                instance_url = '',
                refresh_token = ''
            )
        else:
            return SalesforceCrmCredential(
        )
        """

    def testSalesforceCrmCredential(self):
        """Test SalesforceCrmCredential"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
