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

from suger_sdk_python.models.aws_marketplace_cppo_opportunity_offer_details import AwsMarketplaceCppoOpportunityOfferDetails

class TestAwsMarketplaceCppoOpportunityOfferDetails(unittest.TestCase):
    """AwsMarketplaceCppoOpportunityOfferDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceCppoOpportunityOfferDetails:
        """Test AwsMarketplaceCppoOpportunityOfferDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsMarketplaceCppoOpportunityOfferDetails`
        """
        model = AwsMarketplaceCppoOpportunityOfferDetails()
        if include_optional:
            return AwsMarketplaceCppoOpportunityOfferDetails(
                offer_created_count = 56,
                offer_extended_status = ''
            )
        else:
            return AwsMarketplaceCppoOpportunityOfferDetails(
        )
        """

    def testAwsMarketplaceCppoOpportunityOfferDetails(self):
        """Test AwsMarketplaceCppoOpportunityOfferDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
