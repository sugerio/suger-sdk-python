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

from openapi_client.models.metering_dimension import \
    MeteringDimension  # noqa: E501


class TestMeteringDimension(unittest.TestCase):
    """MeteringDimension unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeteringDimension:
        """Test MeteringDimension
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MeteringDimension`
        """
        model = MeteringDimension()  # noqa: E501
        if include_optional:
            return MeteringDimension(
                category = '',
                description = '',
                included_base_quantities = [
                    openapi_client.models.azure_included_base_quantity.AzureIncludedBaseQuantity(
                        is_infinite = True, 
                        quantity = 1.337, 
                        recurring_unit = 'Monthly', )
                    ],
                key = '',
                name = '',
                plan_id = '',
                plan_name = '',
                price_tiers = [
                    openapi_client.models.gcp_price_tier.GcpPriceTier(
                        from_amount = 1.337, 
                        price = openapi_client.models.gcp_price_value.GcpPriceValue(
                            currency_code = '', 
                            nanos = 56, 
                            units = '', ), 
                        starting_usage_amount = '', )
                    ],
                rate = 1.337,
                sku_id = '',
                types = [
                    ''
                    ],
                usage_count = openapi_client.models.usage_count.UsageCount(
                    credit_count = 1.337, 
                    included_count = 1.337, 
                    reported_count = 1.337, ),
                value_type = 'VALUE_TYPE_UNSPECIFIED'
            )
        else:
            return MeteringDimension(
        )
        """

    def testMeteringDimension(self):
        """Test MeteringDimension"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
