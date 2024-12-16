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

from suger_sdk_python.models.aggregated_metering_usage_record import AggregatedMeteringUsageRecord

class TestAggregatedMeteringUsageRecord(unittest.TestCase):
    """AggregatedMeteringUsageRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregatedMeteringUsageRecord:
        """Test AggregatedMeteringUsageRecord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregatedMeteringUsageRecord`
        """
        model = AggregatedMeteringUsageRecord()
        if include_optional:
            return AggregatedMeteringUsageRecord(
                amount = 1.337,
                billable_metric_aggregation_type = 'COUNT',
                billable_metric_info = {"groupBys":["groupBys","groupBys"],"propertyUniqueOn":"propertyUniqueOn","filterGroups":[{"filters":[{"valueType":"STRING","name":"name","operation":"IS","value":"{}"},{"valueType":"STRING","name":"name","operation":"IS","value":"{}"}]},{"filters":[{"valueType":"STRING","name":"name","operation":"IS","value":"{}"},{"valueType":"STRING","name":"name","operation":"IS","value":"{}"}]}]},
                group_bys_expression = '',
                key = '',
                name = '',
                quantity = 1.337,
                unique_count_aggregation_result = suger_sdk_python.models.unique_count_aggregation_result.UniqueCountAggregationResult(
                    new_items = { }, )
            )
        else:
            return AggregatedMeteringUsageRecord(
        )
        """

    def testAggregatedMeteringUsageRecord(self):
        """Test AggregatedMeteringUsageRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()