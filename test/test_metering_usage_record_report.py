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

from openapi_client.models.metering_usage_record_report import (
    MeteringUsageRecordReport,
)  # noqa: E501


class TestMeteringUsageRecordReport(unittest.TestCase):
    """MeteringUsageRecordReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeteringUsageRecordReport:
        """Test MeteringUsageRecordReport
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MeteringUsageRecordReport`
        """
        model = MeteringUsageRecordReport()  # noqa: E501
        if include_optional:
            return MeteringUsageRecordReport(
                buyer_id = '',
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                entitlement_id = '',
                entitlement_term_id = '',
                id = '',
                info = openapi_client.models.metering_usage_record_report_info.MeteringUsageRecordReportInfo(
                    alibaba_metering_request = openapi_client.models.alibaba_metering_request.alibabaMeteringRequest(), 
                    alibaba_metering_response = openapi_client.models.alibaba_metering_response.alibabaMeteringResponse(), 
                    aws_metering_response = openapi_client.models.aws_metering_response.awsMeteringResponse(), 
                    azure_metering_response = openapi_client.models.azure_metering_response.azureMeteringResponse(), 
                    commit_amount = 1.337, 
                    credit_amount = 1.337, 
                    credit_records = {
                        'key' : 1.337
                        }, 
                    decimal_parts = {
                        'key' : 1.337
                        }, 
                    dimension_categories = {
                        'key' : ''
                        }, 
                    dimension_unit_list_price = {
                        'key' : 1.337
                        }, 
                    dimension_unit_price = {
                        'key' : 1.337
                        }, 
                    end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    gcp_metering_response = openapi_client.models.gcp_metering_response.gcpMeteringResponse(), 
                    included_records = {
                        'key' : 1.337
                        }, 
                    new_decimal_parts = {
                        'key' : 1.337
                        }, 
                    partner = '', 
                    records_to_report_before_adjustment_at_list_price = {
                        'key' : 1.337
                        }, 
                    reported_records = {
                        'key' : 1.337
                        }, 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    usage_record_group_ids = [
                        ''
                        ], 
                    used_commit_amount = 1.337, 
                    used_commit_amount_increment = 1.337, 
                    used_credit_amount = 1.337, 
                    used_credit_amount_increment = 1.337, ),
                organization_id = '',
                partner = 'AWS',
                product_id = ''
            )
        else:
            return MeteringUsageRecordReport(
        )
        """

    def testMeteringUsageRecordReport(self):
        """Test MeteringUsageRecordReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
