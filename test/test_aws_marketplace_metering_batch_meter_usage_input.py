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

from suger_sdk_python.models.aws_marketplace_metering_batch_meter_usage_input import AwsMarketplaceMeteringBatchMeterUsageInput

class TestAwsMarketplaceMeteringBatchMeterUsageInput(unittest.TestCase):
    """AwsMarketplaceMeteringBatchMeterUsageInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceMeteringBatchMeterUsageInput:
        """Test AwsMarketplaceMeteringBatchMeterUsageInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsMarketplaceMeteringBatchMeterUsageInput`
        """
        model = AwsMarketplaceMeteringBatchMeterUsageInput()
        if include_optional:
            return AwsMarketplaceMeteringBatchMeterUsageInput(
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
                    ]
            )
        else:
            return AwsMarketplaceMeteringBatchMeterUsageInput(
        )
        """

    def testAwsMarketplaceMeteringBatchMeterUsageInput(self):
        """Test AwsMarketplaceMeteringBatchMeterUsageInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()