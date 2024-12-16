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

from suger_sdk_python.models.stripe_dispute import StripeDispute

class TestStripeDispute(unittest.TestCase):
    """StripeDispute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripeDispute:
        """Test StripeDispute
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripeDispute`
        """
        model = StripeDispute()
        if include_optional:
            return StripeDispute(
                amount = 56,
                charge_id = '',
                created = 56,
                id = '',
                is_charge_refundable = True,
                livemode = True,
                payment_intent_id = '',
                reason = '',
                status = ''
            )
        else:
            return StripeDispute(
        )
        """

    def testStripeDispute(self):
        """Test StripeDispute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()