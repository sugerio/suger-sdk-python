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

from suger_sdk_python.models.azure_marketplace_price_and_availability_private_offer_plan_software_reservation import AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation

class TestAzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation(unittest.TestCase):
    """AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation:
        """Test AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation`
        """
        model = AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation()
        if include_optional:
            return AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation(
                payment_schedule = {"type":"day","value":7.386281948385884},
                reservation_duration = {"type":"day","value":7.386281948385884},
                vm_prices = {"patternProperties":{"key":{"quantity":7.457744773683766,"unitPricePerPaymentPeriodInUsd":1.1730742509559433}}}
            )
        else:
            return AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation(
        )
        """

    def testAzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation(self):
        """Test AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
