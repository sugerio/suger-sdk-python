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

from suger_sdk_python.models.stripe_customer import StripeCustomer

class TestStripeCustomer(unittest.TestCase):
    """StripeCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripeCustomer:
        """Test StripeCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripeCustomer`
        """
        model = StripeCustomer()
        if include_optional:
            return StripeCustomer(
                address = suger_sdk_python.models.stripe_customer_address.StripeCustomerAddress(
                    city = '', 
                    country = '', 
                    line1 = '', 
                    line2 = '', 
                    postal_code = '', 
                    state = '', ),
                description = '',
                email = '',
                id = '',
                metadata = {
                    'key' : ''
                    },
                name = '',
                phone = ''
            )
        else:
            return StripeCustomer(
        )
        """

    def testStripeCustomer(self):
        """Test StripeCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()