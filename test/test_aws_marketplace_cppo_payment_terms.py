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

from openapi_client.models.aws_marketplace_cppo_payment_terms import (
    AwsMarketplaceCppoPaymentTerms,
)  # noqa: E501


class TestAwsMarketplaceCppoPaymentTerms(unittest.TestCase):
    """AwsMarketplaceCppoPaymentTerms unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceCppoPaymentTerms:
        """Test AwsMarketplaceCppoPaymentTerms
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AwsMarketplaceCppoPaymentTerms`
        """
        model = AwsMarketplaceCppoPaymentTerms()  # noqa: E501
        if include_optional:
            return AwsMarketplaceCppoPaymentTerms(
                currency_code = '',
                entitlement = [
                    openapi_client.models.aws_marketplace_cppo_payment_terms_entitlement.AwsMarketplaceCppoPaymentTermsEntitlement(
                        name = '', 
                        quantity = 56, )
                    ],
                schedule = [
                    openapi_client.models.aws_marketplace_cppo_payment_schedule.AwsMarketplaceCppoPaymentSchedule(
                        amount = 1.337, 
                        charge_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                schedule_type = '',
                selected_duration = ''
            )
        else:
            return AwsMarketplaceCppoPaymentTerms(
        )
        """

    def testAwsMarketplaceCppoPaymentTerms(self):
        """Test AwsMarketplaceCppoPaymentTerms"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
