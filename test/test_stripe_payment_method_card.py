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

from suger_sdk_python.models.stripe_payment_method_card import StripePaymentMethodCard

class TestStripePaymentMethodCard(unittest.TestCase):
    """StripePaymentMethodCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripePaymentMethodCard:
        """Test StripePaymentMethodCard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripePaymentMethodCard`
        """
        model = StripePaymentMethodCard()
        if include_optional:
            return StripePaymentMethodCard(
                brand = '',
                country = '',
                display_brand = '',
                exp_month = 56,
                exp_year = 56,
                fingerprint = '',
                funding = '',
                last4 = ''
            )
        else:
            return StripePaymentMethodCard(
        )
        """

    def testStripePaymentMethodCard(self):
        """Test StripePaymentMethodCard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
