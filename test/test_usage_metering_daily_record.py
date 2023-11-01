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

from openapi_client.models.usage_metering_daily_record import (
    UsageMeteringDailyRecord,
)  # noqa: E501


class TestUsageMeteringDailyRecord(unittest.TestCase):
    """UsageMeteringDailyRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageMeteringDailyRecord:
        """Test UsageMeteringDailyRecord
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UsageMeteringDailyRecord`
        """
        model = UsageMeteringDailyRecord()  # noqa: E501
        if include_optional:
            return UsageMeteringDailyRecord(
                amount = 1.337,
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key = '',
                partner = '',
                quantity = 1.337
            )
        else:
            return UsageMeteringDailyRecord(
        )
        """

    def testUsageMeteringDailyRecord(self):
        """Test UsageMeteringDailyRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()