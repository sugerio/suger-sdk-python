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

from suger_sdk_python.models.invoice_adjust_discount_by_dimension import InvoiceAdjustDiscountByDimension

class TestInvoiceAdjustDiscountByDimension(unittest.TestCase):
    """InvoiceAdjustDiscountByDimension unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceAdjustDiscountByDimension:
        """Test InvoiceAdjustDiscountByDimension
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceAdjustDiscountByDimension`
        """
        model = InvoiceAdjustDiscountByDimension()
        if include_optional:
            return InvoiceAdjustDiscountByDimension(
                dimension_key = '',
                discount = {"discountType":"PERCENTAGE","value":1.4658129805029452},
                reason = ''
            )
        else:
            return InvoiceAdjustDiscountByDimension(
        )
        """

    def testInvoiceAdjustDiscountByDimension(self):
        """Test InvoiceAdjustDiscountByDimension"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
