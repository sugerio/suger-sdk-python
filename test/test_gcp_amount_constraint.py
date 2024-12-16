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

from suger_sdk_python.models.gcp_amount_constraint import GcpAmountConstraint

class TestGcpAmountConstraint(unittest.TestCase):
    """GcpAmountConstraint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpAmountConstraint:
        """Test GcpAmountConstraint
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpAmountConstraint`
        """
        model = GcpAmountConstraint()
        if include_optional:
            return GcpAmountConstraint(
                default_amount = {"nanos":1,"units":"units"},
                max_amount = {"nanos":1,"units":"units"},
                min_amount = {"nanos":1,"units":"units"}
            )
        else:
            return GcpAmountConstraint(
        )
        """

    def testGcpAmountConstraint(self):
        """Test GcpAmountConstraint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()