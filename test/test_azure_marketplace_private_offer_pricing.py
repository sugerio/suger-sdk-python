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


from openapi_client.models.azure_marketplace_private_offer_pricing import (
    AzureMarketplacePrivateOfferPricing,
)  # noqa: E501


class TestAzureMarketplacePrivateOfferPricing(unittest.TestCase):
    """AzureMarketplacePrivateOfferPricing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePrivateOfferPricing:
        """Test AzureMarketplacePrivateOfferPricing
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplacePrivateOfferPricing`
        """
        model = AzureMarketplacePrivateOfferPricing()  # noqa: E501
        if include_optional:
            return AzureMarketplacePrivateOfferPricing(
                discount_percentage = 1.337,
                discount_type = 'absolute',
                markup_percentage = 1.337,
                original_plan = openapi_client.models.azure_marketplace_price_and_availability_private_offer_plan.AzureMarketplacePriceAndAvailabilityPrivateOfferPlan(
                    __schema = '', 
                    id = '', 
                    plan = '', 
                    plan_name = '', 
                    pricing = openapi_client.models.azure_marketplace_price_and_availability_private_offer_price.AzureMarketplacePriceAndAvailabilityPrivateOfferPrice(
                        custom_meters = openapi_client.models.azure_marketplace_price_and_availability_private_offer_custom_meters.AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters(
                            meters = openapi_client.models.meters.meters(), 
                            price_input_option = 'perMarket', ), 
                        recurrent_price = openapi_client.models.azure_marketplace_price_and_availability_recurrent_price.AzureMarketplacePriceAndAvailabilityRecurrentPrice(
                            price_input_option = 'perMarket', 
                            prices = [
                                openapi_client.models.azure_marketplace_price_and_availability_recurrent_price_item.AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
                                    billing_term = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                        type = 'day', 
                                        value = 1.337, ), 
                                    payment_option = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                        type = 'day', 
                                        value = 1.337, ), 
                                    price_per_payment_in_usd = 1.337, )
                                ], ), ), 
                    product = '', 
                    resource_name = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                plan = '',
                plan_id = '',
                plan_name = '',
                plan_type = 'FLAT_RATE',
                price_details = '',
                private_offer_plan = openapi_client.models.azure_marketplace_price_and_availability_private_offer_plan.AzureMarketplacePriceAndAvailabilityPrivateOfferPlan(
                    __schema = '', 
                    id = '', 
                    plan = '', 
                    plan_name = '', 
                    pricing = openapi_client.models.azure_marketplace_price_and_availability_private_offer_price.AzureMarketplacePriceAndAvailabilityPrivateOfferPrice(
                        custom_meters = openapi_client.models.azure_marketplace_price_and_availability_private_offer_custom_meters.AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters(
                            meters = openapi_client.models.meters.meters(), 
                            price_input_option = 'perMarket', ), 
                        recurrent_price = openapi_client.models.azure_marketplace_price_and_availability_recurrent_price.AzureMarketplacePriceAndAvailabilityRecurrentPrice(
                            price_input_option = 'perMarket', 
                            prices = [
                                openapi_client.models.azure_marketplace_price_and_availability_recurrent_price_item.AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
                                    billing_term = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                        type = 'day', 
                                        value = 1.337, ), 
                                    payment_option = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                        type = 'day', 
                                        value = 1.337, ), 
                                    price_per_payment_in_usd = 1.337, )
                                ], ), ), 
                    product = '', 
                    resource_name = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                product = '',
                product_name = '',
                suger_offer_id = ''
            )
        else:
            return AzureMarketplacePrivateOfferPricing(
        )
        """

    def testAzureMarketplacePrivateOfferPricing(self):
        """Test AzureMarketplacePrivateOfferPricing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
