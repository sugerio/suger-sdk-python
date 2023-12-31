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

from openapi_client.models.workload_offer import WorkloadOffer  # noqa: E501

class TestWorkloadOffer(unittest.TestCase):
    """WorkloadOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadOffer:
        """Test WorkloadOffer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadOffer`
        """
        model = WorkloadOffer()  # noqa: E501
        if include_optional:
            return WorkloadOffer(
                contact_ids = [
                    ''
                    ],
                created_by = '',
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expire_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                external_id = '',
                id = '',
                info = openapi_client.models.offer_info.OfferInfo(
                    attach_eula_type = openapi_client.models.attach_eula_type.attachEulaType(), 
                    auto_renew = True, 
                    aws_cppo_event_detail = openapi_client.models.aws_cppo_event_detail.awsCppoEventDetail(), 
                    aws_cppo_opportunity = openapi_client.models.aws_cppo_opportunity.awsCppoOpportunity(), 
                    azure_original_plan = openapi_client.models.azure_original_plan.azureOriginalPlan(), 
                    azure_private_offer = openapi_client.models.azure_private_offer.azurePrivateOffer(), 
                    azure_product_variant = openapi_client.models.azure_product_variant.azureProductVariant(), 
                    buyer_aws_account_ids = [
                        ''
                        ], 
                    buyer_azure_tenants = [
                        openapi_client.models.azure_audience.AzureAudience(
                            description = '', 
                            id = '', )
                        ], 
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
                            term = '', 
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
                    discount_percentage = 1.337, 
                    eula_type = '', 
                    eula_url = '', 
                    gcp_customer_info = openapi_client.models.gcp_customer_info.gcpCustomerInfo(), 
                    gcp_duration = 56, 
                    gcp_metrics = [
                        openapi_client.models.gcp_marketplace_product_metering_metric.GcpMarketplaceProductMeteringMetric(
                            description = '', 
                            display_name = '', 
                            display_unit = '', 
                            display_unit_description = '', 
                            id = '', 
                            metric_kind = '', 
                            name = '', 
                            reporting_unit = '', 
                            sku_id = '', 
                            unit = '', 
                            value_type = openapi_client.models.value_type.valueType(), )
                        ], 
                    gcp_payment_schedule = openapi_client.models.gcp_payment_schedule.gcpPaymentSchedule(), 
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
                    gcp_private_offer = openapi_client.models.gcp_private_offer.gcpPrivateOffer(), 
                    gcp_provider_info = openapi_client.models.gcp_provider_info.gcpProviderInfo(), 
                    gcp_provider_internal_note = '', 
                    gcp_provider_public_note = '', 
                    gcp_usage_plan_price_model = openapi_client.models.gcp_usage_plan_price_model.gcpUsagePlanPriceModel(), 
                    payment_installments = [
                        openapi_client.models.payment_installment.PaymentInstallment(
                            amount = 1.337, 
                            charge_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            charge_on_str = '', 
                            credit = 1.337, 
                            discount_percentage = 1.337, 
                            original_amount = 1.337, )
                        ], 
                    private_offer_url = '', 
                    refund_cancelation_policy = '', 
                    seller_notes = '', 
                    visibility = 'PRIVATE', ),
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_by = '',
                meta_info = openapi_client.models.workload_meta_info.WorkloadMetaInfo(
                    base_agreement_id = '', 
                    buyer_ids = [
                        ''
                        ], 
                    contacts = [
                        openapi_client.models.contact.Contact(
                            company = '', 
                            email = '', 
                            name = '', )
                        ], 
                    custom_meta_info = {
                        'key' : ''
                        }, 
                    error_messages = [
                        ''
                        ], 
                    hubspot_deal_id = '', 
                    internal_note = '', 
                    is_agreement_based_offer = True, 
                    is_renewal_offer = True, 
                    notifications = [
                        openapi_client.models.notification_event.NotificationEvent(
                            action = 'ACCEPT', 
                            cc_contact_ids = [
                                ''
                                ], 
                            contact_ids = [
                                ''
                                ], 
                            entity_id = '', 
                            entity_status = '', 
                            entity_type = 'ORGANIZATION', 
                            event_id = '', 
                            event_status = openapi_client.models.event_status.eventStatus(), 
                            last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '', 
                            organization_id = '', 
                            partner = openapi_client.models.partner.partner(), 
                            timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            title = '', 
                            track_events = [
                                openapi_client.models.track_event.TrackEvent(
                                    contact_id = '', 
                                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], )
                        ], 
                    renewal_offer_type = openapi_client.models.renewal_offer_type.renewalOfferType(), 
                    salesforce_opportunity_id = '', ),
                name = '',
                offer_type = 'DEFAULT',
                organization_id = '',
                partner = '',
                product_id = '',
                service = 'DEFAULT',
                status = 'ACCEPTED'
            )
        else:
            return WorkloadOffer(
        )
        """

    def testWorkloadOffer(self):
        """Test WorkloadOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
