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

from openapi_client.models.cosell_opp_meta import CosellOppMeta  # noqa: E501

class TestCosellOppMeta(unittest.TestCase):
    """CosellOppMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CosellOppMeta:
        """Test CosellOppMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CosellOppMeta`
        """
        model = CosellOppMeta()  # noqa: E501
        if include_optional:
            return CosellOppMeta(
                is_archived = True,
                is_draft = True,
                salesforce_referral_id = '',
                status = 'Pending',
                sync_record = openapi_client.models.cosell_sync_record.CosellSyncRecord(
                    message = '', 
                    ok = True, )
            )
        else:
            return CosellOppMeta(
        )
        """

    def testCosellOppMeta(self):
        """Test CosellOppMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
