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

from openapi_client.models.create_usage_record_group_params import (
    CreateUsageRecordGroupParams,
)  # noqa: E501


class TestCreateUsageRecordGroupParams(unittest.TestCase):
    """CreateUsageRecordGroupParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUsageRecordGroupParams:
        """Test CreateUsageRecordGroupParams
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateUsageRecordGroupParams`
        """
        model = CreateUsageRecordGroupParams()  # noqa: E501
        if include_optional:
            return CreateUsageRecordGroupParams(
                entitlement_id = '',
                id = '',
                meta_info = openapi_client.models.metering_usage_record_group_meta_info.MeteringUsageRecordGroupMetaInfo(
                    origin_records = {
                        'key' : 1.337
                        }, 
                    source = openapi_client.models.source.source(), 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                organization_id = '',
                records = {
                    'key' : 1.337
                    },
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CreateUsageRecordGroupParams(
                entitlement_id = '',
                organization_id = '',
                records = {
                    'key' : 1.337
                    },
        )
        """

    def testCreateUsageRecordGroupParams(self):
        """Test CreateUsageRecordGroupParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
