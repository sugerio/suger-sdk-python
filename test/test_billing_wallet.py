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

from suger_sdk_python.models.billing_wallet import BillingWallet

class TestBillingWallet(unittest.TestCase):
    """BillingWallet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingWallet:
        """Test BillingWallet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingWallet`
        """
        model = BillingWallet()
        if include_optional:
            return BillingWallet(
                buyer_id = '',
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                currency = '',
                expire_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                external_id = '',
                id = '',
                info = {"closeDate":"2000-01-23T04:56:07.000+00:00","stripePaymentMethod":{"livemode":true,"bacs_debit":{"last4":"last4","fingerprint":"fingerprint","sort_code":"sort_code"},"created":1,"us_bank_account":{"last4":"last4","account_type":"account_type","account_holder_type":"account_holder_type","bank_name":"bank_name","fingerprint":"fingerprint","routing_number":"routing_number"},"sepa_debit":{"branch_code":"branch_code","bank_code":"bank_code","country":"country","last4":"last4","fingerprint":"fingerprint"},"id":"id","card":{"country":"country","last4":"last4","funding":"funding","display_brand":"display_brand","fingerprint":"fingerprint","exp_month":0,"exp_year":6,"brand":"brand"},"object":"object"},"stripeSetupIntentId":"stripeSetupIntentId"},
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                organization_id = '',
                partner = '',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'ACTIVE',
                total_amount = 1.337,
                type = 'ach_debit',
                used_amount = 1.337
            )
        else:
            return BillingWallet(
        )
        """

    def testBillingWallet(self):
        """Test BillingWallet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
