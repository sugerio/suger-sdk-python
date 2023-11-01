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

from openapi_client.models.list_usage_metering_daily_verifications_response import ListUsageMeteringDailyVerificationsResponse  # noqa: E501

class TestListUsageMeteringDailyVerificationsResponse(unittest.TestCase):
    """ListUsageMeteringDailyVerificationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListUsageMeteringDailyVerificationsResponse:
        """Test ListUsageMeteringDailyVerificationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUsageMeteringDailyVerificationsResponse`
        """
        model = ListUsageMeteringDailyVerificationsResponse()  # noqa: E501
        if include_optional:
            return ListUsageMeteringDailyVerificationsResponse(
                next_offset = 56,
                usage_metering_daily_verifications = [
                    openapi_client.models.usage_metering_daily_verification.UsageMeteringDailyVerification(
                        billed_amount = 1.337, 
                        billed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        billed_quantity = 1.337, 
                        is_amount_matched = True, 
                        is_quantity_matched = True, 
                        key = '', 
                        partner = openapi_client.models.partner.partner(), 
                        reported_amount = 1.337, 
                        reported_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        reported_quantity = 1.337, )
                    ]
            )
        else:
            return ListUsageMeteringDailyVerificationsResponse(
        )
        """

    def testListUsageMeteringDailyVerificationsResponse(self):
        """Test ListUsageMeteringDailyVerificationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
