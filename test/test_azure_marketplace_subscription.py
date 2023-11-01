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

from openapi_client.models.azure_marketplace_subscription import \
    AzureMarketplaceSubscription  # noqa: E501


class TestAzureMarketplaceSubscription(unittest.TestCase):
    """AzureMarketplaceSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceSubscription:
        """Test AzureMarketplaceSubscription
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureMarketplaceSubscription`
        """
        model = AzureMarketplaceSubscription()  # noqa: E501
        if include_optional:
            return AzureMarketplaceSubscription(
                allowed_customer_operations = [
                    'Read'
                    ],
                auto_renew = True,
                beneficiary = openapi_client.models.azure_ad_identifier.AzureADIdentifier(
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
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fulfillment_id = '',
                id = '',
                is_free_trial = True,
                is_test = True,
                last_modified = '',
                name = '',
                offer_id = '',
                plan_id = '',
                publisher_id = '',
                purchaser = openapi_client.models.azure_ad_identifier.AzureADIdentifier(
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
                quantity = 56,
                saas_subscription_status = 'NotStarted',
                sandbox_type = 'None',
                session_id = '',
                session_mode = 'None',
                store_front = '',
                term = openapi_client.models.azure_term.AzureTerm(
                    charge_duration = '', 
                    end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    term_unit = '', )
            )
        else:
            return AzureMarketplaceSubscription(
        )
        """

    def testAzureMarketplaceSubscription(self):
        """Test AzureMarketplaceSubscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
