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

from suger_sdk_python.models.aws_marketplace_event_bridge_event_offer import AwsMarketplaceEventBridgeEventOffer

class TestAwsMarketplaceEventBridgeEventOffer(unittest.TestCase):
    """AwsMarketplaceEventBridgeEventOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceEventBridgeEventOffer:
        """Test AwsMarketplaceEventBridgeEventOffer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsMarketplaceEventBridgeEventOffer`
        """
        model = AwsMarketplaceEventBridgeEventOffer()
        if include_optional:
            return AwsMarketplaceEventBridgeEventOffer(
                arn = '',
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = ''
            )
        else:
            return AwsMarketplaceEventBridgeEventOffer(
        )
        """

    def testAwsMarketplaceEventBridgeEventOffer(self):
        """Test AwsMarketplaceEventBridgeEventOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
