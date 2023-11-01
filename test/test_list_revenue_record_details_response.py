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

from openapi_client.models.list_revenue_record_details_response import (
    ListRevenueRecordDetailsResponse,
)  # noqa: E501


class TestListRevenueRecordDetailsResponse(unittest.TestCase):
    """ListRevenueRecordDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListRevenueRecordDetailsResponse:
        """Test ListRevenueRecordDetailsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListRevenueRecordDetailsResponse`
        """
        model = ListRevenueRecordDetailsResponse()  # noqa: E501
        if include_optional:
            return ListRevenueRecordDetailsResponse(
                next_offset = 56,
                revenue_record_details = [
                    openapi_client.models.revenue_record_detail.RevenueRecordDetail(
                        aws_revenue_record_detail = openapi_client.models.aws_revenue_record_detail.awsRevenueRecordDetail(), 
                        azure_revenue_record_detail = openapi_client.models.azure_revenue_record_detail.azureRevenueRecordDetail(), 
                        gcp_revenue_record_detail = openapi_client.models.gcp_revenue_record_detail.gcpRevenueRecordDetail(), )
                    ]
            )
        else:
            return ListRevenueRecordDetailsResponse(
        )
        """

    def testListRevenueRecordDetailsResponse(self):
        """Test ListRevenueRecordDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()