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

from suger_sdk_python.models.stripe_refund import StripeRefund

class TestStripeRefund(unittest.TestCase):
    """StripeRefund unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripeRefund:
        """Test StripeRefund
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripeRefund`
        """
        model = StripeRefund()
        if include_optional:
            return StripeRefund(
                charge_id = '',
                estination_details = suger_sdk_python.models.stripe_refund_destination_details.StripeRefundDestinationDetails(
                    card = suger_sdk_python.models.stripe_refund_destination_details_card.StripeRefundDestinationDetailsCard(
                        reference = '', 
                        reference_status = '', 
                        reference_type = '', 
                        type = '', ), 
                    type = '', 
                    us_bank_transfer = suger_sdk_python.models.stripe_refund_destination_details_us_bank_transfer.StripeRefundDestinationDetailsUSBankTransfer(
                        reference = '', 
                        reference_status = '', ), ),
                failure_balance_transaction_id = '',
                failure_reason = '',
                id = '',
                payment_intent_id = '',
                status = 'pending'
            )
        else:
            return StripeRefund(
        )
        """

    def testStripeRefund(self):
        """Test StripeRefund"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
