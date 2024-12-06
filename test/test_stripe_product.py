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

from suger_sdk_python.models.stripe_product import StripeProduct

class TestStripeProduct(unittest.TestCase):
    """StripeProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripeProduct:
        """Test StripeProduct
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripeProduct`
        """
        model = StripeProduct()
        if include_optional:
            return StripeProduct(
                active = True,
                created = 56,
                description = '',
                id = '',
                images = [
                    ''
                    ],
                livemode = True,
                marketing_features = [
                    {"name":"name"}
                    ],
                metadata = {
                    'key' : ''
                    },
                name = '',
                object = '',
                package_dimensions = suger_sdk_python.models.stripe_product_package_dimensions.StripeProductPackageDimensions(
                    height = 1.337, 
                    length = 1.337, 
                    weight = 1.337, 
                    width = 1.337, ),
                shippable = True,
                statement_descriptor = '',
                tax_code = None,
                unit_label = '',
                updated = 56,
                url = ''
            )
        else:
            return StripeProduct(
        )
        """

    def testStripeProduct(self):
        """Test StripeProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
