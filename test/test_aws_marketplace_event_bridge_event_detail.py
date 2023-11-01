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
import datetime

from openapi_client.models.aws_marketplace_event_bridge_event_detail import AwsMarketplaceEventBridgeEventDetail  # noqa: E501

class TestAwsMarketplaceEventBridgeEventDetail(unittest.TestCase):
    """AwsMarketplaceEventBridgeEventDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceEventBridgeEventDetail:
        """Test AwsMarketplaceEventBridgeEventDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsMarketplaceEventBridgeEventDetail`
        """
        model = AwsMarketplaceEventBridgeEventDetail()  # noqa: E501
        if include_optional:
            return AwsMarketplaceEventBridgeEventDetail(
                catalog = '',
                event_category = '',
                event_id = '',
                event_name = '',
                event_source = '',
                event_type = '',
                event_version = '',
                management_event = True,
                manufacturer = openapi_client.models.aws_marketplace_event_bridge_event_account.AwsMarketplaceEventBridgeEventAccount(
                    account_id = '', 
                    name = '', ),
                offer = openapi_client.models.aws_marketplace_event_bridge_event_offer.AwsMarketplaceEventBridgeEventOffer(
                    arn = '', 
                    expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', ),
                product = openapi_client.models.aws_marketplace_event_bridge_event_product.AwsMarketplaceEventBridgeEventProduct(
                    arn = '', 
                    id = '', 
                    title = '', ),
                request_id = '',
                request_parameters = None,
                response_elements = None,
                seller_of_record = openapi_client.models.aws_marketplace_event_bridge_event_account.AwsMarketplaceEventBridgeEventAccount(
                    account_id = '', 
                    name = '', ),
                targeted_buyer_account_ids = [
                    ''
                    ]
            )
        else:
            return AwsMarketplaceEventBridgeEventDetail(
        )
        """

    def testAwsMarketplaceEventBridgeEventDetail(self):
        """Test AwsMarketplaceEventBridgeEventDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
