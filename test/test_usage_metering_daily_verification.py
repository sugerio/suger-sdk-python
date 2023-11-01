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
import datetime

from openapi_client.models.usage_metering_daily_verification import (
    UsageMeteringDailyVerification,
)  # noqa: E501


class TestUsageMeteringDailyVerification(unittest.TestCase):
    """UsageMeteringDailyVerification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageMeteringDailyVerification:
        """Test UsageMeteringDailyVerification
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UsageMeteringDailyVerification`
        """
        model = UsageMeteringDailyVerification()  # noqa: E501
        if include_optional:
            return UsageMeteringDailyVerification(
                billed_amount = 1.337,
                billed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                billed_quantity = 1.337,
                is_amount_matched = True,
                is_quantity_matched = True,
                key = '',
                partner = '',
                reported_amount = 1.337,
                reported_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reported_quantity = 1.337
            )
        else:
            return UsageMeteringDailyVerification(
        )
        """

    def testUsageMeteringDailyVerification(self):
        """Test UsageMeteringDailyVerification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
