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


from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_gcp_charge_usage import (
    GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage,
)  # noqa: E501


class TestGithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage(
    unittest.TestCase
):
    """GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage:
        """Test GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage`
        """
        model = GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage()  # noqa: E501
        if include_optional:
            return GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage(
                abandoned = 1.337,
                account_id = '',
                buyer_id = '',
                charges = 1.337,
                currency = '',
                due_vendor = 1.337,
                entitlement_id = '',
                google_entity = '',
                insight_account_id = '',
                offer_id = '',
                ordinal = 56,
                organization_id = '',
                payment_schedule = '',
                payment_type = '',
                prepay_credits = 1.337,
                product_id = '',
                refund_balance_deducted_this_month = 1.337,
                refund_balance_outstanding = 1.337,
                refund_reason = '',
                released = 1.337,
                report_date = '',
                resource = '',
                sku = '',
                trial_use = 1.337,
                unit = '',
                usage = 1.337,
                used_by = '',
                withheld = 1.337
            )
        else:
            return GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage(
        )
        """

    def testGithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage(self):
        """Test GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
