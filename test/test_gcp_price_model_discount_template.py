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

from suger_sdk_python.models.gcp_price_model_discount_template import GcpPriceModelDiscountTemplate

class TestGcpPriceModelDiscountTemplate(unittest.TestCase):
    """GcpPriceModelDiscountTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpPriceModelDiscountTemplate:
        """Test GcpPriceModelDiscountTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpPriceModelDiscountTemplate`
        """
        model = GcpPriceModelDiscountTemplate()
        if include_optional:
            return GcpPriceModelDiscountTemplate(
                discount_economics = '',
                discount_percentage = {"minAmount":{"nanos":1,"units":"units"},"defaultAmount":{"nanos":1,"units":"units"},"maxAmount":{"nanos":1,"units":"units"}},
                discounted_price = {"nanos":1,"units":"units","currencyCode":"currencyCode"},
                hide_discount_percentage = True
            )
        else:
            return GcpPriceModelDiscountTemplate(
        )
        """

    def testGcpPriceModelDiscountTemplate(self):
        """Test GcpPriceModelDiscountTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
