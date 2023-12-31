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

from openapi_client.models.azure_marketplace_product_resource import AzureMarketplaceProductResource  # noqa: E501

class TestAzureMarketplaceProductResource(unittest.TestCase):
    """AzureMarketplaceProductResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureMarketplaceProductResource:
        """Test AzureMarketplaceProductResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureMarketplaceProductResource`
        """
        model = AzureMarketplaceProductResource()  # noqa: E501
        if include_optional:
            return AzureMarketplaceProductResource(
                customer_leads = openapi_client.models.azure_marketplace_customer_leads.AzureMarketplaceCustomerLeads(
                    __schema = '', 
                    blob_lead_configuration = openapi_client.models.blob_lead_configuration.blobLeadConfiguration(), 
                    dynamics_lead_configuration = openapi_client.models.dynamics_lead_configuration.dynamicsLeadConfiguration(), 
                    email_lead_configuration = openapi_client.models.email_lead_configuration.emailLeadConfiguration(), 
                    https_endpoint_lead_configuration = openapi_client.models.https_endpoint_lead_configuration.httpsEndpointLeadConfiguration(), 
                    id = '', 
                    lead_destination = 'none', 
                    marketo_lead_configuration = openapi_client.models.marketo_lead_configuration.marketoLeadConfiguration(), 
                    product = '', 
                    resource_name = '', 
                    salesforce_lead_configuration = openapi_client.models.salesforce_lead_configuration.salesforceLeadConfiguration(), 
                    table_lead_configuration = openapi_client.models.table_lead_configuration.tableLeadConfiguration(), 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                listing = openapi_client.models.azure_marketplace_listing.AzureMarketplaceListing(
                    __schema = '', 
                    cloud_solution_provider_contact = openapi_client.models.azure_marketplace_contact.AzureMarketplaceContact(
                        email = '', 
                        name = '', 
                        phone = '', 
                        url = '', ), 
                    cloud_solution_provider_marketing_materials = '', 
                    description = '', 
                    engineering_contact = openapi_client.models.azure_marketplace_contact.AzureMarketplaceContact(
                        email = '', 
                        name = '', 
                        phone = '', 
                        url = '', ), 
                    general_links = [
                        openapi_client.models.azure_marketplace_general_link.AzureMarketplaceGeneralLink(
                            display_text = '', 
                            link = '', )
                        ], 
                    getting_started_instructions = '', 
                    gloabal_support_website = '', 
                    government_support_website = '', 
                    id = '', 
                    kind = 'azureSaaS', 
                    language_id = '', 
                    lifecycle_state = openapi_client.models.lifecycle_state.lifecycleState(), 
                    privacy_policy_link = '', 
                    product = '', 
                    resource_name = '', 
                    search_keywords = [
                        ''
                        ], 
                    search_result_summary = '', 
                    short_description = '', 
                    support_contact = , 
                    title = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                listing_assets = [
                    openapi_client.models.azure_marketplace_listing_asset.AzureMarketplaceListingAsset(
                        __schema = '', 
                        description = '', 
                        display_order = 56, 
                        file_name = '', 
                        friendly_name = '', 
                        id = '', 
                        kind = 'azure', 
                        language_id = '', 
                        lifecycle_state = openapi_client.models.lifecycle_state.lifecycleState(), 
                        listing = '', 
                        product = '', 
                        resource_name = '', 
                        type = 'azureLogoSmall', 
                        url = '', 
                        validations = [
                            openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                                __schema = '', 
                                code = 'businessValidationError', 
                                level = 'informational', 
                                message = '', 
                                resource_id = '', )
                            ], )
                    ],
                plans = [
                    openapi_client.models.azure_marketplace_plan_resource.AzureMarketplacePlanResource(
                        plan = openapi_client.models.azure_marketplace_plan.AzureMarketplacePlan(
                            __schema = '', 
                            alias = '', 
                            azure_government_certifications = [
                                openapi_client.models.azure_marketplace_government_certification.AzureMarketplaceGovernmentCertification(
                                    link = '', 
                                    name = '', )
                                ], 
                            azure_regions = [
                                ''
                                ], 
                            deprecation_schedule = openapi_client.models.azure_marketplace_deprecation_schedule.AzureMarketplaceDeprecationSchedule(
                                __schema = '', 
                                alternative = openapi_client.models.azure_marketplace_deprecation_schedule_alternative.AzureMarketplaceDeprecationScheduleAlternative(
                                    product = openapi_client.models.product.product(), ), 
                                date = '', 
                                date_offset = '', 
                                reason = 'criticalSecurityIssue', ), 
                            display_rank = 56, 
                            id = '', 
                            identity = openapi_client.models.azure_marketplace_identity.AzureMarketplaceIdentity(
                                external_id = '', ), 
                            lifecycle_state = 'notAvailable', 
                            product = '', 
                            resource_name = '', 
                            subtype = 'managedApplication', 
                            validations = [
                                openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                                    __schema = '', 
                                    code = 'businessValidationError', 
                                    level = 'informational', 
                                    message = '', 
                                    resource_id = '', )
                                ], ), 
                        plan_listing = openapi_client.models.azure_marketplace_plan_listing.AzureMarketplacePlanListing(
                            __schema = '', 
                            description = '', 
                            id = '', 
                            kind = 'azureVM-plan', 
                            language_id = '', 
                            name = '', 
                            product = '', 
                            resource_name = '', 
                            summary = '', ), 
                        price_and_availability_plan = openapi_client.models.azure_marketplace_price_and_availability_plan.AzureMarketplacePriceAndAvailabilityPlan(
                            __schema = '', 
                            audience = 'public', 
                            billing_tag = '', 
                            id = '', 
                            markets = [
                                ''
                                ], 
                            meter_define = '', 
                            pricing = openapi_client.models.azure_marketplace_price_and_availability_price.AzureMarketplacePriceAndAvailabilityPrice(
                                core_pricing = openapi_client.models.azure_marketplace_price_and_availability_core_price.AzureMarketplacePriceAndAvailabilityCorePrice(
                                    price = 1.337, 
                                    price_input_option = 'free', 
                                    price_per_core = 1.337, 
                                    price_per_core_size = openapi_client.models.price_per_core_size.pricePerCoreSize(), 
                                    prices = [
                                        openapi_client.models.azure_marketplace_price.AzureMarketplacePrice(
                                            currency = '', 
                                            price = 1.337, )
                                        ], ), 
                                custom_meters = openapi_client.models.azure_marketplace_price_and_availability_custom_meter_price.AzureMarketplacePriceAndAvailabilityCustomMeterPrice(
                                    meters = {
                                        'key' : openapi_client.models.azure_marketplace_price_and_availability_custom_meter_price_meter_item.AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem(
                                            billing_term = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                                type = 'day', 
                                                value = 1.337, ), 
                                            included_quantities = [
                                                openapi_client.models.azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item.AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem(
                                                    is_infinite = True, 
                                                    quantity = 1.337, )
                                                ], 
                                            payment_option = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                                type = 'day', 
                                                value = 1.337, ), 
                                            price_per_payment_in_usd = 1.337, )
                                        }, 
                                    price_input_option = 'perMarket', ), 
                                license_model = 'byol', 
                                recurrent_price = openapi_client.models.azure_marketplace_price_and_availability_recurrent_price.AzureMarketplacePriceAndAvailabilityRecurrentPrice(
                                    price_input_option = 'perMarket', 
                                    recurrent_price_mode = 'flatRate', 
                                    user_limits = openapi_client.models.azure_marketplace_price_and_availability_recurrent_price_user_limit.AzureMarketplacePriceAndAvailabilityRecurrentPriceUserLimit(
                                        max = 1.337, 
                                        min = 1.337, ), ), 
                                system_meter_pricing = openapi_client.models.azure_marketplace_price_and_availability_system_meter_price.AzureMarketplacePriceAndAvailabilitySystemMeterPrice(
                                    price = 1.337, 
                                    price_input_option = 'perCore', ), ), 
                            private_audiences = [
                                openapi_client.models.azure_marketplace_price_and_availability_audience.AzureMarketplacePriceAndAvailabilityAudience(
                                    id = '', 
                                    label = '', 
                                    type = 'none', )
                                ], 
                            product = '', 
                            resource_name = '', 
                            software_reservation = [
                                openapi_client.models.azure_marketplace_price_and_availability_software_reservation.AzureMarketplacePriceAndAvailabilitySoftwareReservation(
                                    percentage_save = 1.337, 
                                    term = 1.337, 
                                    type = 'month', )
                                ], 
                            trial = , 
                            visibility = 'visible', ), )
                    ],
                price_and_availability_custom_meter = openapi_client.models.azure_marketplace_price_and_availability_custom_meter.AzureMarketplacePriceAndAvailabilityCustomMeter(
                    __schema = '', 
                    custom_meters = {
                        'key' : openapi_client.models.azure_marketplace_price_and_availability_custom_meter_item.AzureMarketplacePriceAndAvailabilityCustomMeterItem(
                            display_name = '', 
                            unit_of_measure = '', )
                        }, 
                    id = '', 
                    product = '', 
                    resource_name = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                price_and_availability_offer = openapi_client.models.azure_marketplace_price_and_availability_offer.AzureMarketplacePriceAndAvailabilityOffer(
                    __schema = '', 
                    id = '', 
                    preview_audiences = [
                        openapi_client.models.azure_marketplace_price_and_availability_audience.AzureMarketplacePriceAndAvailabilityAudience(
                            id = '', 
                            label = '', 
                            type = 'none', )
                        ], 
                    product = '', 
                    resource_name = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                product = openapi_client.models.azure_marketplace_product.AzureMarketplaceProduct(
                    __schema = '', 
                    alias = '', 
                    id = '', 
                    identity = openapi_client.models.azure_marketplace_identity.AzureMarketplaceIdentity(
                        external_id = '', ), 
                    lifecycle_state = 'notAvailable', 
                    product_group = '', 
                    resource_name = '', 
                    type = 'azureApplication', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                var_property = openapi_client.models.azure_marketplace_property.AzureMarketplaceProperty(
                    __schema = '', 
                    app_version = '', 
                    categories = {
                        'key' : [
                            ''
                            ]
                        }, 
                    cloud_industries = {
                        'key' : [
                            ''
                            ]
                        }, 
                    custom_amendments = [
                        openapi_client.models.azure_marketplace_custom_amendment.AzureMarketplaceCustomAmendment(
                            tenants = openapi_client.models.azure_marketplace_custom_amendment_tenant.AzureMarketplaceCustomAmendmentTenant(
                                manual_entries = [
                                    openapi_client.models.azure_marketplace_custom_amendment_tenant_manual_entry.AzureMarketplaceCustomAmendmentTenantManualEntry(
                                        description = '', 
                                        id = '', )
                                    ], ), 
                            terms = '', )
                        ], 
                    id = '', 
                    industries = {
                        'key' : [
                            ''
                            ]
                        }, 
                    kind = 'azureSaaS', 
                    lifecycle_state = 'notAvailable', 
                    product = '', 
                    resource_name = '', 
                    standard_contract_amendment = '', 
                    terms_conditions = 'custom', 
                    terms_of_use = '', 
                    terms_of_use_url = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                reseller = openapi_client.models.azure_marketplace_reseller.AzureMarketplaceReseller(
                    __schema = '', 
                    audiences = [
                        openapi_client.models.azure_marketplace_preview_audience.AzureMarketplacePreviewAudience(
                            description = '', 
                            resource_id = '', 
                            type = 'subscription', )
                        ], 
                    id = '', 
                    product = '', 
                    reseller_channel_state = '', 
                    resource_name = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                setup = openapi_client.models.azure_commercial_marketplace_setup.AzureCommercialMarketplaceSetup(
                    __schema = '', 
                    access_url = '', 
                    call_to_action = 'free', 
                    id = '', 
                    product = '', 
                    require_license_for_install = True, 
                    resource_name = '', 
                    sell_through_microsoft = True, 
                    use_microsoft_license_management_service = True, 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], ),
                technical_configuration = openapi_client.models.azure_marketplace_saas_technical_configuration.AzureMarketplaceSaasTechnicalConfiguration(
                    __schema = '', 
                    azure_ad_app_id = '', 
                    azure_ad_tenant_id = '', 
                    connection_webhook = '', 
                    id = '', 
                    landing_page_url = '', 
                    product = '', 
                    resource_name = '', 
                    validations = [
                        openapi_client.models.azure_marketplace_validation.AzureMarketplaceValidation(
                            __schema = '', 
                            code = 'businessValidationError', 
                            level = 'informational', 
                            message = '', 
                            resource_id = '', )
                        ], )
            )
        else:
            return AzureMarketplaceProductResource(
        )
        """

    def testAzureMarketplaceProductResource(self):
        """Test AzureMarketplaceProductResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
