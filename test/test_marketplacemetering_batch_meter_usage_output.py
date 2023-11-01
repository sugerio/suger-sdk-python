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


from openapi_client.models.marketplacemetering_batch_meter_usage_output import (
    MarketplacemeteringBatchMeterUsageOutput,
)  # noqa: E501


class TestMarketplacemeteringBatchMeterUsageOutput(unittest.TestCase):
    """MarketplacemeteringBatchMeterUsageOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> MarketplacemeteringBatchMeterUsageOutput:
        """Test MarketplacemeteringBatchMeterUsageOutput
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MarketplacemeteringBatchMeterUsageOutput`
        """
        model = MarketplacemeteringBatchMeterUsageOutput()  # noqa: E501
        if include_optional:
            return MarketplacemeteringBatchMeterUsageOutput(
                result_metadata = None,
                results = [
                    openapi_client.models.types/usage_record_result.types.UsageRecordResult(
                        metering_record_id = '', 
                        status = openapi_client.models.status.status(), 
                        usage_record = openapi_client.models.usage_record.usageRecord(), )
                    ],
                unprocessed_records = [
                    openapi_client.models.types/usage_record.types.UsageRecord(
                        customer_identifier = '', 
                        dimension = '', 
                        quantity = 56, 
                        timestamp = '', 
                        usage_allocations = [
                            openapi_client.models.types/usage_allocation.types.UsageAllocation(
                                allocated_usage_quantity = 56, 
                                tags = [
                                    openapi_client.models.github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types/tag.github_com_aws_aws-sdk-go-v2_service_marketplacemetering_types.Tag(
                                        key = '', 
                                        value = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return MarketplacemeteringBatchMeterUsageOutput(
        )
        """

    def testMarketplacemeteringBatchMeterUsageOutput(self):
        """Test MarketplacemeteringBatchMeterUsageOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
