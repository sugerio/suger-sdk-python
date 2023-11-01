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


from openapi_client.models.client_describe_order_response_body import (
    ClientDescribeOrderResponseBody,
)  # noqa: E501


class TestClientDescribeOrderResponseBody(unittest.TestCase):
    """ClientDescribeOrderResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientDescribeOrderResponseBody:
        """Test ClientDescribeOrderResponseBody
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ClientDescribeOrderResponseBody`
        """
        model = ClientDescribeOrderResponseBody()  # noqa: E501
        if include_optional:
            return ClientDescribeOrderResponseBody(
                account_quantity = 56,
                ali_uid = 56,
                components = { },
                coupon_price = 1.337,
                created_on = 56,
                instance_ids = openapi_client.models.client/describe_order_response_body_instance_ids.client.DescribeOrderResponseBodyInstanceIds(
                    instance_id = [
                        ''
                        ], ),
                order_id = 56,
                order_status = '',
                order_type = '',
                original_price = 1.337,
                paid_on = 56,
                pay_status = '',
                payment_price = 1.337,
                period_type = '',
                product_code = '',
                product_name = '',
                product_sku_code = '',
                quantity = 56,
                request_id = '',
                supplier_company_name = '',
                supplier_telephones = openapi_client.models.client/describe_order_response_body_supplier_telephones.client.DescribeOrderResponseBodySupplierTelephones(
                    telephone = [
                        ''
                        ], ),
                total_price = 1.337
            )
        else:
            return ClientDescribeOrderResponseBody(
        )
        """

    def testClientDescribeOrderResponseBody(self):
        """Test ClientDescribeOrderResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
