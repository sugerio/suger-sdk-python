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

from openapi_client.models.usage_metering_config_info import UsageMeteringConfigInfo  # noqa: E501

class TestUsageMeteringConfigInfo(unittest.TestCase):
    """UsageMeteringConfigInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageMeteringConfigInfo:
        """Test UsageMeteringConfigInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsageMeteringConfigInfo`
        """
        model = UsageMeteringConfigInfo()  # noqa: E501
        if include_optional:
            return UsageMeteringConfigInfo(
                partner_usage_metering_configs = [
                    openapi_client.models.partner_usage_metering_config.PartnerUsageMeteringConfig(
                        dimension_mapping = {
                            'key' : openapi_client.models.usage_metering_dimension_mapping_value.UsageMeteringDimensionMappingValue(
                                convertion_multiplier = 1.337, 
                                dimension_key = '', )
                            }, 
                        enable_commit_with_additional_usage_at_list_price = True, 
                        enable_commit_with_additional_usage_metering = True, 
                        enable_dimension_mapping = True, 
                        partner = openapi_client.models.partner.partner(), )
                    ]
            )
        else:
            return UsageMeteringConfigInfo(
        )
        """

    def testUsageMeteringConfigInfo(self):
        """Test UsageMeteringConfigInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
