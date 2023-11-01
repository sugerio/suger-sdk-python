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


from openapi_client.models.gcp_price_tier import GcpPriceTier  # noqa: E501


class TestGcpPriceTier(unittest.TestCase):
    """GcpPriceTier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpPriceTier:
        """Test GcpPriceTier
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpPriceTier`
        """
        model = GcpPriceTier()  # noqa: E501
        if include_optional:
            return GcpPriceTier(
                from_amount = 1.337,
                price = openapi_client.models.gcp_price_value.GcpPriceValue(
                    currency_code = '', 
                    nanos = 56, 
                    units = '', ),
                starting_usage_amount = ''
            )
        else:
            return GcpPriceTier(
        )
        """

    def testGcpPriceTier(self):
        """Test GcpPriceTier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
