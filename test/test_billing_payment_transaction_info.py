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

from suger_sdk_python.models.billing_payment_transaction_info import BillingPaymentTransactionInfo

class TestBillingPaymentTransactionInfo(unittest.TestCase):
    """BillingPaymentTransactionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingPaymentTransactionInfo:
        """Test BillingPaymentTransactionInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingPaymentTransactionInfo`
        """
        model = BillingPaymentTransactionInfo()
        if include_optional:
            return BillingPaymentTransactionInfo(
                invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                refund_exists = True,
                stripe_balance_transaction = suger_sdk_python.models.stripe_balance_transaction.StripeBalanceTransaction(
                    amount = 56, 
                    available_on = 56, 
                    charge_id = '', 
                    created = 56, 
                    description = '', 
                    exchange_rate = 1.337, 
                    fee = 56, 
                    fee_details = [
                        suger_sdk_python.models.stripe_balance_transaction_fee_detail.StripeBalanceTransactionFeeDetail(
                            amount = 56, 
                            application = '', 
                            description = '', 
                            type = '', )
                        ], 
                    id = '', 
                    net = 56, 
                    status = '', 
                    type = '', ),
                stripe_disputes = [
                    {"paymentIntentId":"paymentIntentId","reason":"reason","amount":6,"is_charge_refundable":true,"livemode":true,"chargeId":"chargeId","created":1,"id":"id","status":"status"}
                    ],
                stripe_error = suger_sdk_python.models.stripe_error.StripeError(
                    code = '', 
                    message = '', 
                    param = '', 
                    status = 56, 
                    type = '', ),
                stripe_payment_intent = suger_sdk_python.models.stripe_payment_intent.StripePaymentIntent(
                    id = '', 
                    last_payment_error = suger_sdk_python.models.last_payment_error.last_payment_error(), 
                    livemode = True, 
                    status = suger_sdk_python.models.status.status(), ),
                stripe_refund = suger_sdk_python.models.stripe_refund.StripeRefund(
                    charge_id = '', 
                    estination_details = suger_sdk_python.models.estination_details.estinationDetails(), 
                    failure_balance_transaction_id = '', 
                    failure_reason = '', 
                    id = '', 
                    payment_intent_id = '', 
                    status = suger_sdk_python.models.status.status(), )
            )
        else:
            return BillingPaymentTransactionInfo(
        )
        """

    def testBillingPaymentTransactionInfo(self):
        """Test BillingPaymentTransactionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()