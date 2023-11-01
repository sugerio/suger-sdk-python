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


from openapi_client.models.gcp_marketplace_private_offer_price_model_commitment import (
    GcpMarketplacePrivateOfferPriceModelCommitment,
)  # noqa: E501


class TestGcpMarketplacePrivateOfferPriceModelCommitment(unittest.TestCase):
    """GcpMarketplacePrivateOfferPriceModelCommitment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GcpMarketplacePrivateOfferPriceModelCommitment:
        """Test GcpMarketplacePrivateOfferPriceModelCommitment
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferPriceModelCommitment`
        """
        model = GcpMarketplacePrivateOfferPriceModelCommitment()  # noqa: E501
        if include_optional:
            return GcpMarketplacePrivateOfferPriceModelCommitment(
                commitment_amount_per_period = openapi_client.models.gcp_price_value.GcpPriceValue(
                    currency_code = '', 
                    nanos = 56, 
                    units = '', ),
                discount = openapi_client.models.gcp_marketplace_private_offer_price_model_discount.GcpMarketplacePrivateOfferPriceModelDiscount(
                    discount_percentage = openapi_client.models.discount_percentage.discountPercentage(), 
                    discounted_price = openapi_client.models.discounted_price.discountedPrice(), ),
                period = openapi_client.models.gcp_period_duration.GcpPeriodDuration(
                    count = 56, 
                    unit = 'MONTHLY_PERIOD', )
            )
        else:
            return GcpMarketplacePrivateOfferPriceModelCommitment(
        )
        """

    def testGcpMarketplacePrivateOfferPriceModelCommitment(self):
        """Test GcpMarketplacePrivateOfferPriceModelCommitment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
