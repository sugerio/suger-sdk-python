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

from openapi_client.models.identity_buyer import IdentityBuyer  # noqa: E501

class TestIdentityBuyer(unittest.TestCase):
    """IdentityBuyer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityBuyer:
        """Test IdentityBuyer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityBuyer`
        """
        model = IdentityBuyer()  # noqa: E501
        if include_optional:
            return IdentityBuyer(
                contact_ids = [
                    ''
                    ],
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                external_id = '',
                id = '',
                info = openapi_client.models.buyer_info.BuyerInfo(
                    aws_buyer = openapi_client.models.aws_buyer.awsBuyer(), 
                    azure_buyer = openapi_client.models.azure_buyer.azureBuyer(), 
                    collectable_amount = 1.337, 
                    customer_id = '', 
                    disbursed_amount = 1.337, 
                    gcp_buyer = openapi_client.models.gcp_buyer.gcpBuyer(), 
                    invoiced_amount = 1.337, 
                    metronome_customer_id = '', 
                    orb_customer_id = '', ),
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                organization_id = '',
                partner = 'AWS'
            )
        else:
            return IdentityBuyer(
        )
        """

    def testIdentityBuyer(self):
        """Test IdentityBuyer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
