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


from openapi_client.models.gcp_marketplace_private_offer_term import (
    GcpMarketplacePrivateOfferTerm,
)  # noqa: E501


class TestGcpMarketplacePrivateOfferTerm(unittest.TestCase):
    """GcpMarketplacePrivateOfferTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplacePrivateOfferTerm:
        """Test GcpMarketplacePrivateOfferTerm
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GcpMarketplacePrivateOfferTerm`
        """
        model = GcpMarketplacePrivateOfferTerm()  # noqa: E501
        if include_optional:
            return GcpMarketplacePrivateOfferTerm(
                enable_scheduled_start_times = True,
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_policy = '',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                term_duration = openapi_client.models.gcp_period_duration.GcpPeriodDuration(
                    count = 56, 
                    unit = 'MONTHLY_PERIOD', )
            )
        else:
            return GcpMarketplacePrivateOfferTerm(
        )
        """

    def testGcpMarketplacePrivateOfferTerm(self):
        """Test GcpMarketplacePrivateOfferTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
