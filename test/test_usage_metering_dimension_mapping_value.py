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

from openapi_client.models.usage_metering_dimension_mapping_value import UsageMeteringDimensionMappingValue  # noqa: E501

class TestUsageMeteringDimensionMappingValue(unittest.TestCase):
    """UsageMeteringDimensionMappingValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageMeteringDimensionMappingValue:
        """Test UsageMeteringDimensionMappingValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsageMeteringDimensionMappingValue`
        """
        model = UsageMeteringDimensionMappingValue()  # noqa: E501
        if include_optional:
            return UsageMeteringDimensionMappingValue(
                convertion_multiplier = 1.337,
                dimension_key = ''
            )
        else:
            return UsageMeteringDimensionMappingValue(
        )
        """

    def testUsageMeteringDimensionMappingValue(self):
        """Test UsageMeteringDimensionMappingValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
