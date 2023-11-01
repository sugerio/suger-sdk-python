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


from openapi_client.models.revenue_record import RevenueRecord  # noqa: E501


class TestRevenueRecord(unittest.TestCase):
    """RevenueRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RevenueRecord:
        """Test RevenueRecord
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RevenueRecord`
        """
        model = RevenueRecord()  # noqa: E501
        if include_optional:
            return RevenueRecord(
                amount = 1.337,
                buyer_id = '',
                collectable_amount = 1.337,
                currency = '',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                disburse_amount = 1.337,
                disburse_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                entitlement_id = '',
                id = '',
                info = openapi_client.models.revenue_record_info.RevenueRecordInfo(
                    aws_revenue_records = [
                        openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib/billing_aws_billing_event.github_com_sugerio_marketplace-service_rds-db_lib.BillingAwsBillingEvent(
                            action = '', 
                            agreement_id = '', 
                            amount = 1.337, 
                            balance_impacting = 56, 
                            bank_trace_id = '', 
                            billing_address_id = '', 
                            broker_id = '', 
                            buyer_id = '', 
                            currency = '', 
                            data_feed_product_id = '', 
                            disbursement_billing_event_id = '', 
                            end_user_account_id = '', 
                            entitlement_id = '', 
                            from_account_id = '', 
                            id = '', 
                            insert_date = openapi_client.models.sql/null_time.sql.NullTime(
                                time = '', 
                                valid = True, ), 
                            invoice_date = openapi_client.models.sql/null_time.sql.NullTime(
                                time = '', 
                                valid = True, ), 
                            invoice_id = '', 
                            offer_id = '', 
                            organization_id = '', 
                            parent_billing_event_id = '', 
                            payment_due_date = , 
                            product_id = '', 
                            to_account_id = '', 
                            transaction_reference_id = '', 
                            transaction_type = '', 
                            usage_period_end_date = , 
                            usage_period_start_date = , )
                        ], 
                    azure_revenue_records = [
                        openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib/billing_azure_cma_revenue.github_com_sugerio_marketplace-service_rds-db_lib.BillingAzureCmaRevenue(
                            azure_asset_id = '', 
                            azure_billing_account_id = '', 
                            azure_customer_id = '', 
                            azure_offer_id = '', 
                            azure_plan_id = '', 
                            billing_model = '', 
                            buyer_id = '', 
                            earning_usd = 1.337, 
                            entitlement_id = '', 
                            estimated_payout_month = , 
                            offer_id = '', 
                            organization_id = '', 
                            payment_sent_date = , 
                            payout_status = '', 
                            product_id = '', 
                            purchase_record_id = '', 
                            revenue_usd = 1.337, 
                            term_end_date = '', 
                            term_start_date = '', )
                        ], 
                    disbursement_notification_sent = True, 
                    gcp_revenue_records = [
                        openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib/billing_gcp_charge_usage.github_com_sugerio_marketplace-service_rds-db_lib.BillingGcpChargeUsage(
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
                            withheld = 1.337, )
                        ], 
                    resource = '', ),
                invoice_amount = 1.337,
                invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization_id = '',
                partner = '',
                payment_due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                product_id = '',
                refund_disburse_amount = 1.337,
                refund_disburse_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                refund_invoice_amount = 1.337,
                refund_invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tax_amount = 1.337
            )
        else:
            return RevenueRecord(
        )
        """

    def testRevenueRecord(self):
        """Test RevenueRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
