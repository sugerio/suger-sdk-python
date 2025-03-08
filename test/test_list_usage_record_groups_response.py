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

from suger_sdk_python.models.list_usage_record_groups_response import ListUsageRecordGroupsResponse

class TestListUsageRecordGroupsResponse(unittest.TestCase):
    """ListUsageRecordGroupsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListUsageRecordGroupsResponse:
        """Test ListUsageRecordGroupsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUsageRecordGroupsResponse`
        """
        model = ListUsageRecordGroupsResponse()
        if include_optional:
            return ListUsageRecordGroupsResponse(
                next_offset = 56,
                usage_record_groups = [
                    {"creationTime":"2000-01-23T04:56:07.000+00:00","records":{"key":9.301444243932576},"entitlementID":"entitlementID","buyerID":"buyerID","organizationID":"organizationID","metaInfo":{"lagoAmount":6.027456183070403,"stripePeriodStartTime":"2000-01-23T04:56:07.000+00:00","metronomeDailyCostAmount":1.4658129805029452,"SkipValidation":true,"billableRecords":[{"quantity":0.8008281904610115,"key":"key","properties":{"key":""}},{"quantity":0.8008281904610115,"key":"key","properties":{"key":""}}],"stripeInvoiceID":"stripeInvoiceID","originRecords":{"key":2.3021358869347655},"source":"{}","stripeSubscriptionItemID":"stripeSubscriptionItemID","lagoSubscriptionID":"lagoSubscriptionID","stripePeriodEndTime":"2000-01-23T04:56:07.000+00:00","stripeUsageRecordSummaryID":"stripeUsageRecordSummaryID","metronomeMonthlyInvoiceAmount":5.962133916683182,"metronomeMonthlyInvoiceAmountAdjusted":5.637376656633329,"lagoUsageStartTime":"2000-01-23T04:56:07.000+00:00","metronomeInvoiceID":"metronomeInvoiceID","stripeUsageRecordSummaryTotalUsage":7,"timestamp":"2000-01-23T04:56:07.000+00:00"},"partner":"AWS","serialID":3,"usageRecordReportID":"usageRecordReportID","id":"id","lastUpdateTime":"2000-01-23T04:56:07.000+00:00","reportedTime":"2000-01-23T04:56:07.000+00:00","status":"status"}
                    ]
            )
        else:
            return ListUsageRecordGroupsResponse(
        )
        """

    def testListUsageRecordGroupsResponse(self):
        """Test ListUsageRecordGroupsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
