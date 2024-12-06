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

from suger_sdk_python.models.client_describe_instance_response_body_modules_module import ClientDescribeInstanceResponseBodyModulesModule

class TestClientDescribeInstanceResponseBodyModulesModule(unittest.TestCase):
    """ClientDescribeInstanceResponseBodyModulesModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientDescribeInstanceResponseBodyModulesModule:
        """Test ClientDescribeInstanceResponseBodyModulesModule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientDescribeInstanceResponseBodyModulesModule`
        """
        model = ClientDescribeInstanceResponseBodyModulesModule()
        if include_optional:
            return ClientDescribeInstanceResponseBodyModulesModule(
                code = '',
                id = '',
                name = '',
                properties = {"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]}
            )
        else:
            return ClientDescribeInstanceResponseBodyModulesModule(
        )
        """

    def testClientDescribeInstanceResponseBodyModulesModule(self):
        """Test ClientDescribeInstanceResponseBodyModulesModule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
