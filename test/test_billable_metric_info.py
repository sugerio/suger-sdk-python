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

from suger_sdk_python.models.billable_metric_info import BillableMetricInfo

class TestBillableMetricInfo(unittest.TestCase):
    """BillableMetricInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillableMetricInfo:
        """Test BillableMetricInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillableMetricInfo`
        """
        model = BillableMetricInfo()
        if include_optional:
            return BillableMetricInfo(
                filter_groups = [
                    {"filters":[{"valueType":"STRING","name":"name","operation":"IS","value":"{}"},{"valueType":"STRING","name":"name","operation":"IS","value":"{}"}]}
                    ],
                group_bys = [
                    ''
                    ],
                property_unique_on = ''
            )
        else:
            return BillableMetricInfo(
        )
        """

    def testBillableMetricInfo(self):
        """Test BillableMetricInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
