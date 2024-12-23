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

from suger_sdk_python.models.client_describe_instance_response_body_modules_module_properties_property_property_values import ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues

class TestClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(unittest.TestCase):
    """ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues:
        """Test ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues`
        """
        model = ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues()
        if include_optional:
            return ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(
                property_value = [
                    {"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}
                    ]
            )
        else:
            return ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(
        )
        """

    def testClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(self):
        """Test ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
