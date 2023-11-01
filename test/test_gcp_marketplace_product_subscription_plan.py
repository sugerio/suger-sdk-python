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


from openapi_client.models.gcp_marketplace_product_subscription_plan import (
    GcpMarketplaceProductSubscriptionPlan,
)  # noqa: E501


class TestGcpMarketplaceProductSubscriptionPlan(unittest.TestCase):
    """GcpMarketplaceProductSubscriptionPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProductSubscriptionPlan:
        """Test GcpMarketplaceProductSubscriptionPlan
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplaceProductSubscriptionPlan`
        """
        model = GcpMarketplaceProductSubscriptionPlan()  # noqa: E501
        if include_optional:
            return GcpMarketplaceProductSubscriptionPlan(
                period = '',
                price = openapi_client.models.gcp_price_value.GcpPriceValue(
                    currency_code = '', 
                    nanos = 56, 
                    units = '', )
            )
        else:
            return GcpMarketplaceProductSubscriptionPlan(
        )
        """

    def testGcpMarketplaceProductSubscriptionPlan(self):
        """Test GcpMarketplaceProductSubscriptionPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
