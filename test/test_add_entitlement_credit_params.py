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

from openapi_client.models.add_entitlement_credit_params import \
    AddEntitlementCreditParams  # noqa: E501


class TestAddEntitlementCreditParams(unittest.TestCase):
    """AddEntitlementCreditParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddEntitlementCreditParams:
        """Test AddEntitlementCreditParams
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AddEntitlementCreditParams`
        """
        model = AddEntitlementCreditParams()  # noqa: E501
        if include_optional:
            return AddEntitlementCreditParams(
                credit_amount_increment = 1.337,
                entitlement_id = '',
                organization_id = ''
            )
        else:
            return AddEntitlementCreditParams(
                credit_amount_increment = 1.337,
                entitlement_id = '',
                organization_id = '',
        )
        """

    def testAddEntitlementCreditParams(self):
        """Test AddEntitlementCreditParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
