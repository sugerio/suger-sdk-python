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

from suger_sdk_python.models.add_entitlement_credit_response import AddEntitlementCreditResponse

class TestAddEntitlementCreditResponse(unittest.TestCase):
    """AddEntitlementCreditResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddEntitlementCreditResponse:
        """Test AddEntitlementCreditResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddEntitlementCreditResponse`
        """
        model = AddEntitlementCreditResponse()
        if include_optional:
            return AddEntitlementCreditResponse(
                credit_amount_increment = 1.337,
                entitlement_id = '',
                entitlement_term_id = '',
                new_credit_amount = 1.337,
                organization_id = ''
            )
        else:
            return AddEntitlementCreditResponse(
        )
        """

    def testAddEntitlementCreditResponse(self):
        """Test AddEntitlementCreditResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
