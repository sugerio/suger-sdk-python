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


from openapi_client.models.azure_marketplace_price_and_availability_recurrent_price_item import (
    AzureMarketplacePriceAndAvailabilityRecurrentPriceItem,
)  # noqa: E501


class TestAzureMarketplacePriceAndAvailabilityRecurrentPriceItem(unittest.TestCase):
    """AzureMarketplacePriceAndAvailabilityRecurrentPriceItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AzureMarketplacePriceAndAvailabilityRecurrentPriceItem:
        """Test AzureMarketplacePriceAndAvailabilityRecurrentPriceItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePriceAndAvailabilityRecurrentPriceItem`
        """
        model = AzureMarketplacePriceAndAvailabilityRecurrentPriceItem()  # noqa: E501
        if include_optional:
            return AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
                billing_term = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                    type = 'day', 
                    value = 1.337, ),
                payment_option = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                    type = 'day', 
                    value = 1.337, ),
                price_per_payment_in_usd = 1.337,
                prices = [
                    openapi_client.models.azure_marketplace_price.AzureMarketplacePrice(
                        currency = '', 
                        markets = [
                            ''
                            ], 
                        price = 1.337, )
                    ]
            )
        else:
            return AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
        )
        """

    def testAzureMarketplacePriceAndAvailabilityRecurrentPriceItem(self):
        """Test AzureMarketplacePriceAndAvailabilityRecurrentPriceItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
