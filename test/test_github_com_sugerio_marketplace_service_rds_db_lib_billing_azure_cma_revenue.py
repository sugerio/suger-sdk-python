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


from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue import (
    GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue,
)  # noqa: E501


class TestGithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue(
    unittest.TestCase
):
    """GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue:
        """Test GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue`
        """
        model = GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue()  # noqa: E501
        if include_optional:
            return GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue(
                azure_asset_id = '',
                azure_billing_account_id = '',
                azure_customer_id = '',
                azure_offer_id = '',
                azure_plan_id = '',
                billing_model = '',
                buyer_id = '',
                earning_usd = 1.337,
                entitlement_id = '',
                estimated_payout_month = openapi_client.models.sql/null_time.sql.NullTime(
                    time = '', 
                    valid = True, ),
                offer_id = '',
                organization_id = '',
                payment_sent_date = openapi_client.models.sql/null_time.sql.NullTime(
                    time = '', 
                    valid = True, ),
                payout_status = '',
                product_id = '',
                purchase_record_id = '',
                revenue_usd = 1.337,
                term_end_date = '',
                term_start_date = ''
            )
        else:
            return GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue(
        )
        """

    def testGithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue(self):
        """Test GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
