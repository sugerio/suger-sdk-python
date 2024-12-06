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

from suger_sdk_python.models.billing_payment_transaction import BillingPaymentTransaction

class TestBillingPaymentTransaction(unittest.TestCase):
    """BillingPaymentTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingPaymentTransaction:
        """Test BillingPaymentTransaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingPaymentTransaction`
        """
        model = BillingPaymentTransaction()
        if include_optional:
            return BillingPaymentTransaction(
                amount = 1.337,
                buyer_id = '',
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                currency = '',
                entitlement_id = '',
                id = '',
                info = {"stripePaymentIntent":"{}","stripeBalanceTransaction":"{}","stripeError":"{}","stripeDisputes":[{"paymentIntentId":"paymentIntentId","reason":"reason","amount":6,"is_charge_refundable":true,"livemode":true,"chargeId":"chargeId","created":1,"id":"id","status":"status"},{"paymentIntentId":"paymentIntentId","reason":"reason","amount":6,"is_charge_refundable":true,"livemode":true,"chargeId":"chargeId","created":1,"id":"id","status":"status"}],"invoiceDate":"2000-01-23T04:56:07.000+00:00","stripeRefund":"{}","refundExists":true},
                invoice_id = '',
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization_id = '',
                parent_id = '',
                partner = '',
                status = 'PENDING',
                type = 'CHARGE',
                wallet_id = '',
                wallet_type = 'ach_debit'
            )
        else:
            return BillingPaymentTransaction(
        )
        """

    def testBillingPaymentTransaction(self):
        """Test BillingPaymentTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
