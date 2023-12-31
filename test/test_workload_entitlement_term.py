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

from openapi_client.models.workload_entitlement_term import WorkloadEntitlementTerm  # noqa: E501

class TestWorkloadEntitlementTerm(unittest.TestCase):
    """WorkloadEntitlementTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadEntitlementTerm:
        """Test WorkloadEntitlementTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadEntitlementTerm`
        """
        model = WorkloadEntitlementTerm()  # noqa: E501
        if include_optional:
            return WorkloadEntitlementTerm(
                buyer_id = '',
                commit_amount = 1.337,
                credit_amount = 1.337,
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                entitlement_id = '',
                entitlement_info = openapi_client.models.entitlement_info.EntitlementInfo(
                    alibaba_entitlements = [
                        openapi_client.models.client/describe_instance_response_body.client.DescribeInstanceResponseBody(
                            app_json = '', 
                            auto_renewal = '', 
                            began_on = 56, 
                            component_json = '', 
                            constraints = '', 
                            created_on = 56, 
                            end_on = 56, 
                            extend_json = '', 
                            host_json = '', 
                            instance_id = 56, 
                            is_trial = True, 
                            modules = openapi_client.models.client/describe_instance_response_body_modules.client.DescribeInstanceResponseBodyModules(
                                module = [
                                    openapi_client.models.client/describe_instance_response_body_modules_module.client.DescribeInstanceResponseBodyModulesModule(
                                        code = '', 
                                        id = '', 
                                        name = '', 
                                        properties = openapi_client.models.client/describe_instance_response_body_modules_module_properties.client.DescribeInstanceResponseBodyModulesModuleProperties(
                                            property = [
                                                openapi_client.models.client/describe_instance_response_body_modules_module_properties_property.client.DescribeInstanceResponseBodyModulesModulePropertiesProperty(
                                                    display_unit = '', 
                                                    key = '', 
                                                    name = '', 
                                                    property_values = openapi_client.models.client/describe_instance_response_body_modules_module_properties_property_property_values.client.DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(
                                                        property_value = [
                                                            openapi_client.models.client/describe_instance_response_body_modules_module_properties_property_property_values_property_value.client.DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue(
                                                                display_name = '', 
                                                                max = '', 
                                                                min = '', 
                                                                remark = '', 
                                                                step = '', 
                                                                type = '', 
                                                                value = '', )
                                                            ], ), 
                                                    show_type = '', )
                                                ], ), )
                                    ], ), 
                            order_id = 56, 
                            product_code = '', 
                            product_name = '', 
                            product_sku_code = '', 
                            product_type = '', 
                            relational_data = openapi_client.models.client/describe_instance_response_body_relational_data.client.DescribeInstanceResponseBodyRelationalData(
                                service_status = '', ), 
                            status = '', 
                            supplier_name = '', )
                        ], 
                    alibaba_orders = [
                        openapi_client.models.client/describe_order_response_body.client.DescribeOrderResponseBody(
                            account_quantity = 56, 
                            ali_uid = 56, 
                            components = { }, 
                            coupon_price = 1.337, 
                            created_on = 56, 
                            instance_ids = openapi_client.models.client/describe_order_response_body_instance_ids.client.DescribeOrderResponseBodyInstanceIds(
                                instance_id = [
                                    ''
                                    ], ), 
                            order_id = 56, 
                            order_status = '', 
                            order_type = '', 
                            original_price = 1.337, 
                            paid_on = 56, 
                            pay_status = '', 
                            payment_price = 1.337, 
                            period_type = '', 
                            product_code = '', 
                            product_name = '', 
                            product_sku_code = '', 
                            quantity = 56, 
                            request_id = '', 
                            supplier_company_name = '', 
                            supplier_telephones = openapi_client.models.client/describe_order_response_body_supplier_telephones.client.DescribeOrderResponseBodySupplierTelephones(
                                telephone = [
                                    ''
                                    ], ), 
                            total_price = 1.337, )
                        ], 
                    auto_renew = True, 
                    aws_entitlements = [
                        openapi_client.models.types/entitlement.types.Entitlement(
                            customer_identifier = '', 
                            dimension = '', 
                            expiration_date = '', 
                            product_code = '', 
                            value = openapi_client.models.value.value(), )
                        ], 
                    azure_subscriptions = [
                        openapi_client.models.azure_marketplace_subscription.AzureMarketplaceSubscription(
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
                                term_unit = '', ), )
                        ], 
                    collectable_amount = 1.337, 
                    commit_amount = 1.337, 
                    commits = [
                        openapi_client.models.commit_dimension.CommitDimension(
                            category = '', 
                            description = '', 
                            is_user_created = True, 
                            key = '', 
                            length = 56, 
                            maximum_users = 1, 
                            minimum_users = 1, 
                            name = '', 
                            quantity = 56, 
                            rate = 1.337, 
                            term_end_time = '', 
                            time_unit = openapi_client.models.time_unit.timeUnit(), 
                            type = openapi_client.models.type.type(), 
                            types = [
                                ''
                                ], )
                        ], 
                    currency = '', 
                    dimensions = [
                        openapi_client.models.metering_dimension.MeteringDimension(
                            category = '', 
                            description = '', 
                            included_base_quantities = [
                                openapi_client.models.azure_included_base_quantity.AzureIncludedBaseQuantity(
                                    is_infinite = True, 
                                    quantity = 1.337, 
                                    recurring_unit = 'Monthly', )
                                ], 
                            key = '', 
                            name = '', 
                            plan_id = '', 
                            plan_name = '', 
                            price_tiers = [
                                openapi_client.models.gcp_price_tier.GcpPriceTier(
                                    from_amount = 1.337, 
                                    price = openapi_client.models.gcp_price_value.GcpPriceValue(
                                        currency_code = '', 
                                        nanos = 56, 
                                        units = '', ), 
                                    starting_usage_amount = '', )
                                ], 
                            rate = 1.337, 
                            sku_id = '', 
                            usage_count = openapi_client.models.usage_count.usageCount(), 
                            value_type = openapi_client.models.value_type.valueType(), )
                        ], 
                    disbursed_amount = 1.337, 
                    eula_type = '', 
                    eula_url = '', 
                    gcp_entitlements = [
                        openapi_client.models.gcp_marketplace_entitlement.GcpMarketplaceEntitlement(
                            account = '', 
                            consumers = [
                                openapi_client.models.gcp_marketplace_consumer.GcpMarketplaceConsumer(
                                    project = '', )
                                ], 
                            create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            input_properties = [
                                56
                                ], 
                            message_to_user = '', 
                            name = '', 
                            new_offer_duration = '', 
                            new_offer_end_time = '', 
                            new_offer_start_time = '', 
                            new_pending_offer = '', 
                            new_pending_offer_duration = '', 
                            new_pending_plan = '', 
                            new_plan = '', 
                            offer = '', 
                            offer_duration = '', 
                            offer_effective_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            offer_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            plan = '', 
                            product = '', 
                            product_external_name = '', 
                            provider = '', 
                            quote_external_name = '', 
                            state = openapi_client.models.state.state(), 
                            subscription_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            usage_reporting_id = '', )
                        ], 
                    gcp_plans = [
                        openapi_client.models.gcp_marketplace_product_purchase_option_spec.GcpMarketplaceProductPurchaseOptionSpec(
                            feature_values = [
                                openapi_client.models.gcp_marketplace_product_feature_value.GcpMarketplaceProductFeatureValue(
                                    feature_description = '', 
                                    feature_name = '', 
                                    feature_title = '', 
                                    feature_value = '', )
                                ], 
                            name = '', 
                            price_info = openapi_client.models.gcp_marketplace_product_price_info.GcpMarketplaceProductPriceInfo(
                                description = '', 
                                price_model = 'FREE', 
                                subscription_plans = [
                                    openapi_client.models.gcp_marketplace_product_subscription_plan.GcpMarketplaceProductSubscriptionPlan(
                                        period = '', )
                                    ], 
                                usage_fees = [
                                    openapi_client.models.gcp_marketplace_product_usage_fee.GcpMarketplaceProductUsageFee(
                                        display_quantity = 56, 
                                        metric_id = '', )
                                    ], ), 
                            purchase_mode = 'PURCHASE_MODE_PRIVATE', 
                            title = '', )
                        ], 
                    invoiced_amount = 1.337, 
                    payment_installments = [
                        openapi_client.models.payment_installment.PaymentInstallment(
                            amount = 1.337, 
                            charge_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            charge_on_str = '', 
                            credit = 1.337, 
                            discount_percentage = 1.337, 
                            original_amount = 1.337, )
                        ], 
                    refund_cancelation_policy = '', 
                    seller_notes = '', ),
                external_entitlement_id = '',
                id = '',
                info = openapi_client.models.entitlement_term_info.EntitlementTermInfo(
                    dimension_quantity_decimal_parts = {
                        'key' : 1.337
                        }, 
                    is_commit_divided = True, 
                    parent_entitlement_term_id = '', 
                    sub_entitlement_term_ids = [
                        ''
                        ], 
                    type = '', ),
                offer_id = '',
                organization_id = '',
                partner = '',
                product_id = '',
                service = 'DEFAULT',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                used_commit_amount = 1.337,
                used_credit_amount = 1.337
            )
        else:
            return WorkloadEntitlementTerm(
        )
        """

    def testWorkloadEntitlementTerm(self):
        """Test WorkloadEntitlementTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
