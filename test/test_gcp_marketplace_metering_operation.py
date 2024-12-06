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

from suger_sdk_python.models.gcp_marketplace_metering_operation import GcpMarketplaceMeteringOperation

class TestGcpMarketplaceMeteringOperation(unittest.TestCase):
    """GcpMarketplaceMeteringOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceMeteringOperation:
        """Test GcpMarketplaceMeteringOperation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceMeteringOperation`
        """
        model = GcpMarketplaceMeteringOperation()
        if include_optional:
            return GcpMarketplaceMeteringOperation(
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
                                labels = {
                                    'key' : ''
                                    }, 
                                money_value = suger_sdk_python.models.money_value.moneyValue(), 
                                start_time = '', 
                                string_value = '', )
                            ], )
                    ],
                operation_id = '',
                operation_name = '',
                start_time = ''
            )
        else:
            return GcpMarketplaceMeteringOperation(
        )
        """

    def testGcpMarketplaceMeteringOperation(self):
        """Test GcpMarketplaceMeteringOperation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
