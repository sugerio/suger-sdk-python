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

from suger_sdk_python.models.client_describe_instance_response_body import ClientDescribeInstanceResponseBody

class TestClientDescribeInstanceResponseBody(unittest.TestCase):
    """ClientDescribeInstanceResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientDescribeInstanceResponseBody:
        """Test ClientDescribeInstanceResponseBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientDescribeInstanceResponseBody`
        """
        model = ClientDescribeInstanceResponseBody()
        if include_optional:
            return ClientDescribeInstanceResponseBody(
                app_json = '',
                auto_renewal = '',
                began_on = 56,
                component_json = '',
                constraints = '',
                created_on = 56,
                end_on = 56,
                extend_json = '',
                host_json = '',
                instance_id = 56,
                is_trial = True,
                modules = {"Module":[{"Id":"Id","Properties":{"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]},"Code":"Code","Name":"Name"},{"Id":"Id","Properties":{"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]},"Code":"Code","Name":"Name"}]},
                order_id = 56,
                product_code = '',
                product_name = '',
                product_sku_code = '',
                product_type = '',
                relational_data = {"ServiceStatus":"ServiceStatus"},
                status = '',
                supplier_name = ''
            )
        else:
            return ClientDescribeInstanceResponseBody(
        )
        """

    def testClientDescribeInstanceResponseBody(self):
        """Test ClientDescribeInstanceResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
