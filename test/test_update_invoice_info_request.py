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

from suger_sdk_python.models.update_invoice_info_request import UpdateInvoiceInfoRequest

class TestUpdateInvoiceInfoRequest(unittest.TestCase):
    """UpdateInvoiceInfoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateInvoiceInfoRequest:
        """Test UpdateInvoiceInfoRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateInvoiceInfoRequest`
        """
        model = UpdateInvoiceInfoRequest()
        if include_optional:
            return UpdateInvoiceInfoRequest(
                discount_amount = 1.337,
                discount_type = 'PERCENTAGE',
                due_date = '',
                memo = ''
            )
        else:
            return UpdateInvoiceInfoRequest(
        )
        """

    def testUpdateInvoiceInfoRequest(self):
        """Test UpdateInvoiceInfoRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
