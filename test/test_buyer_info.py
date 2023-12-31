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

from openapi_client.models.buyer_info import BuyerInfo  # noqa: E501

class TestBuyerInfo(unittest.TestCase):
    """BuyerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuyerInfo:
        """Test BuyerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuyerInfo`
        """
        model = BuyerInfo()  # noqa: E501
        if include_optional:
            return BuyerInfo(
                aws_buyer = openapi_client.models.aws_account_identifier.AwsAccountIdentifier(
                    aws_account_id = '', 
                    aws_customer_id = '', 
                    company_info = openapi_client.models.company_info.CompanyInfo(
                        address_line1 = '', 
                        address_line2 = '', 
                        city = '', 
                        country = '', 
                        email_domain = '', 
                        name = '', 
                        postal_code = '', 
                        state = '', ), 
                    data_feed_account_id = '', ),
                azure_buyer = openapi_client.models.azure_ad_identifier.AzureADIdentifier(
                    billing_account_id = '', 
                    company_info = openapi_client.models.company_info.CompanyInfo(
                        address_line1 = '', 
                        address_line2 = '', 
                        city = '', 
                        country = '', 
                        email_domain = '', 
                        name = '', 
                        postal_code = '', 
                        state = '', ), 
                    customer_id = '', 
                    email_id = '', 
                    first_name = '', 
                    last_name = '', 
                    license_type = '', 
                    object_id = '', 
                    puid = '', 
                    tenant_id = '', ),
                collectable_amount = 1.337,
                customer_id = '',
                disbursed_amount = 1.337,
                gcp_buyer = openapi_client.models.gcp_marketplace_user_account.GcpMarketplaceUserAccount(
                    approvals = [
                        openapi_client.models.gcp_marketplace_user_account_approval.GcpMarketplaceUserAccountApproval(
                            name = '', 
                            reason = '', 
                            state = 'STATE_UNSPECIFIED', 
                            update_time = '', )
                        ], 
                    billing_account_id = '', 
                    company_info = openapi_client.models.company_info.CompanyInfo(
                        address_line1 = '', 
                        address_line2 = '', 
                        city = '', 
                        country = '', 
                        email_domain = '', 
                        name = '', 
                        postal_code = '', ), 
                    create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    input_properties = [
                        56
                        ], 
                    name = '', 
                    provider = '', 
                    state = openapi_client.models.state.state(), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_info = openapi_client.models.gcp_user_info.GcpUserInfo(
                        roles = [
                            ''
                            ], 
                        user_identity = '', ), ),
                invoiced_amount = 1.337,
                metronome_customer_id = '',
                orb_customer_id = ''
            )
        else:
            return BuyerInfo(
        )
        """

    def testBuyerInfo(self):
        """Test BuyerInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
