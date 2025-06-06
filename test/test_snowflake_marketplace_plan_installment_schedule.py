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

from suger_sdk_python.models.snowflake_marketplace_plan_installment_schedule import SnowflakeMarketplacePlanInstallmentSchedule

class TestSnowflakeMarketplacePlanInstallmentSchedule(unittest.TestCase):
    """SnowflakeMarketplacePlanInstallmentSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnowflakeMarketplacePlanInstallmentSchedule:
        """Test SnowflakeMarketplacePlanInstallmentSchedule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnowflakeMarketplacePlanInstallmentSchedule`
        """
        model = SnowflakeMarketplacePlanInstallmentSchedule()
        if include_optional:
            return SnowflakeMarketplacePlanInstallmentSchedule(
                default_installment_amount = 1.337,
                installment_duration = 1.337,
                overridden_installments = [
                    {"installment_amount":4.652396432933246,"installment_number":8.969578798196912}
                    ]
            )
        else:
            return SnowflakeMarketplacePlanInstallmentSchedule(
        )
        """

    def testSnowflakeMarketplacePlanInstallmentSchedule(self):
        """Test SnowflakeMarketplacePlanInstallmentSchedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
