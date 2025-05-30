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

from suger_sdk_python.models.metering_usage_record_report_info import MeteringUsageRecordReportInfo

class TestMeteringUsageRecordReportInfo(unittest.TestCase):
    """MeteringUsageRecordReportInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeteringUsageRecordReportInfo:
        """Test MeteringUsageRecordReportInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MeteringUsageRecordReportInfo`
        """
        model = MeteringUsageRecordReportInfo()
        if include_optional:
            return MeteringUsageRecordReportInfo(
                aggregated_billable_records = [
                    {"amount":6.027456183070403,"quantity":1.4658129805029452,"name":"name","billableMetricInfo":{"groupBys":["groupBys","groupBys"],"propertyUniqueOn":"propertyUniqueOn","filterGroups":[{"filters":[{"valueType":"STRING","name":"name","operation":"IS","value":"{}"},{"valueType":"STRING","name":"name","operation":"IS","value":"{}"}]},{"filters":[{"valueType":"STRING","name":"name","operation":"IS","value":"{}"},{"valueType":"STRING","name":"name","operation":"IS","value":"{}"}]}]},"groupBysExpression":"groupBysExpression","billableMetricAggregationType":"COUNT","key":"key","uniqueCountAggregationResult":"{}"}
                    ],
                alibaba_metering_request = suger_sdk_python.models.client/push_metering_data_request.client.PushMeteringDataRequest(
                    metering = '', ),
                alibaba_metering_response = suger_sdk_python.models.client/push_metering_data_response_body.client.PushMeteringDataResponseBody(
                    request_id = '', 
                    success = True, ),
                aws_metering_request = suger_sdk_python.models.aws_marketplace_metering_batch_meter_usage_input.AwsMarketplaceMeteringBatchMeterUsageInput(
                    product_code = '', 
                    usage_records = [
                        suger_sdk_python.models.aws_marketplace_metering_usage_record.AwsMarketplaceMeteringUsageRecord(
                            customer_identifier = '', 
                            dimension = '', 
                            quantity = 56, 
                            timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            usage_allocations = [
                                suger_sdk_python.models.aws_marketplace_metering_usage_allocation.AwsMarketplaceMeteringUsageAllocation(
                                    allocated_usage_quantity = 56, 
                                    tags = [
                                        suger_sdk_python.models.aws_marketplace_metering_tag.AwsMarketplaceMeteringTag(
                                            key = '', 
                                            value = '', )
                                        ], )
                                ], )
                        ], ),
                aws_metering_response = suger_sdk_python.models.marketplacemetering/batch_meter_usage_output.marketplacemetering.BatchMeterUsageOutput(
                    result_metadata = suger_sdk_python.models.result_metadata.resultMetadata(), 
                    results = [
                        suger_sdk_python.models.types/usage_record_result.types.UsageRecordResult(
                            metering_record_id = '', 
                            status = suger_sdk_python.models.status.status(), 
                            usage_record = suger_sdk_python.models.usage_record.usageRecord(), )
                        ], 
                    unprocessed_records = [
                        suger_sdk_python.models.types/usage_record.types.UsageRecord(
                            customer_identifier = '', 
                            dimension = '', 
                            quantity = 56, 
                            timestamp = '', 
                            usage_allocations = [
                                suger_sdk_python.models.types/usage_allocation.types.UsageAllocation(
                                    allocated_usage_quantity = 56, 
                                    tags = [
                                        suger_sdk_python.models.github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types/tag.github_com_aws_aws-sdk-go-v2_service_marketplacemetering_types.Tag(
                                            key = '', 
                                            value = '', )
                                        ], )
                                ], )
                        ], ),
                azure_metering_request = suger_sdk_python.models.azure_marketplace_metering_batch_usage_event.AzureMarketplaceMeteringBatchUsageEvent(
                    request = [
                        suger_sdk_python.models.azure_marketplace_metering_usage_event.AzureMarketplaceMeteringUsageEvent(
                            dimension = '', 
                            effective_start_time = '', 
                            plan_id = '', 
                            quantity = 1.337, 
                            resource_id = '', 
                            resource_uri = '', )
                        ], ),
                azure_metering_response = suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1/batch_usage_event_ok_response.github_com_sugerio_marketplace-service_third_party_azure_sdk_marketplacemeteringv1.BatchUsageEventOkResponse(
                    count = 56, 
                    result = [
                        suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1/usage_batch_event_ok_message.github_com_sugerio_marketplace-service_third_party_azure_sdk_marketplacemeteringv1.UsageBatchEventOkMessage(
                            dimension = '', 
                            effective_start_time = '', 
                            error = suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1/usage_event_conflict_response.github_com_sugerio_marketplace-service_third_party_azure_sdk_marketplacemeteringv1.UsageEventConflictResponse(
                                additional_info = suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1/usage_event_conflict_response_additional_info.github_com_sugerio_marketplace-service_third_party_azure_sdk_marketplacemeteringv1.UsageEventConflictResponseAdditionalInfo(
                                    accepted_message = suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1/usage_event_ok_response.github_com_sugerio_marketplace-service_third_party_azure_sdk_marketplacemeteringv1.UsageEventOkResponse(
                                        dimension = '', 
                                        effective_start_time = '', 
                                        message_time = '', 
                                        plan_id = '', 
                                        quantity = 1.337, 
                                        resource_id = '', 
                                        resource_uri = '', 
                                        status = suger_sdk_python.models.status.status(), 
                                        usage_event_id = '', ), ), 
                                code = '', 
                                message = '', ), 
                            message_time = '', 
                            plan_id = '', 
                            quantity = 1.337, 
                            resource_id = '', 
                            resource_uri = '', 
                            status = suger_sdk_python.models.status.status(), 
                            usage_event_id = '', )
                        ], ),
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
                gcp_metering_request = suger_sdk_python.models.gcp_marketplace_metering_operation.GcpMarketplaceMeteringOperation(
                    consumer_id = '', 
                    end_time = '', 
                    labels = {
                        'key' : ''
                        }, 
                    metric_value_sets = [
                        suger_sdk_python.models.gcp_marketplace_metering_metric_value_set.GcpMarketplaceMeteringMetricValueSet(
                            metric_name = '', 
                            metric_values = [
                                suger_sdk_python.models.gcp_marketplace_metering_metric_value.GcpMarketplaceMeteringMetricValue(
                                    bool_value = True, 
                                    double_value = 1.337, 
                                    end_time = '', 
                                    int64_value = '0', 
                                    money_value = suger_sdk_python.models.money_value.moneyValue(), 
                                    start_time = '', 
                                    string_value = '', )
                                ], )
                        ], 
                    operation_id = '', 
                    operation_name = '', 
                    start_time = '', ),
                gcp_metering_response = suger_sdk_python.models.servicecontrol/report_response.servicecontrol.ReportResponse(
                    report_errors = [
                        suger_sdk_python.models.servicecontrol/report_error.servicecontrol.ReportError(
                            operation_id = '', 
                            status = suger_sdk_python.models.status.status(), )
                        ], 
                    service_config_id = '', 
                    service_rollout_id = '', ),
                included_records = {
                    'key' : 1.337
                    },
                message = '',
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
                status = '',
                usage_record_group_ids = [
                    ''
                    ],
                used_commit_amount = 1.337,
                used_commit_amount_increment = 1.337,
                used_credit_amount = 1.337,
                used_credit_amount_increment = 1.337
            )
        else:
            return MeteringUsageRecordReportInfo(
        )
        """

    def testMeteringUsageRecordReportInfo(self):
        """Test MeteringUsageRecordReportInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
