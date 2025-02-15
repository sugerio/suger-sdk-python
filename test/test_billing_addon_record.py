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

from suger_sdk_python.models.billing_addon_record import BillingAddonRecord

class TestBillingAddonRecord(unittest.TestCase):
    """BillingAddonRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingAddonRecord:
        """Test BillingAddonRecord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingAddonRecord`
        """
        model = BillingAddonRecord()
        if include_optional:
            return BillingAddonRecord(
                amount = 1.337,
                charge_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                id = '',
                name = ''
            )
        else:
            return BillingAddonRecord(
        )
        """

    def testBillingAddonRecord(self):
        """Test BillingAddonRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
