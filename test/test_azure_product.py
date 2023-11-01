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

from openapi_client.models.azure_product import AzureProduct  # noqa: E501


class TestAzureProduct(unittest.TestCase):
    """AzureProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProduct:
        """Test AzureProduct
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AzureProduct`
        """
        model = AzureProduct()  # noqa: E501
        if include_optional:
            return AzureProduct(
                availabilities = [
                    openapi_client.models.azure_product_availability.AzureProductAvailability(
                        email_audiences = [
                            openapi_client.models.azure_audience.AzureAudience(
                                description = '', 
                                id = '', )
                            ], 
                        enterprise_licensing = '', 
                        id = '', 
                        resource_type = '', 
                        subscription_audiences = [
                            openapi_client.models.azure_audience.AzureAudience(
                                description = '', 
                                id = '', )
                            ], 
                        visibility = '', )
                    ],
                branches = [
                    openapi_client.models.azure_product_branch.AzureProductBranch(
                        current_draft_instance_id = '', 
                        friendly_name = '', 
                        id = '', 
                        module = '', 
                        resource_type = '', 
                        type = '', 
                        variant_id = '', )
                    ],
                external_ids = [
                    openapi_client.models.azure_type_value.AzureTypeValue(
                        type = '', 
                        value = '', )
                    ],
                id = '',
                is_modular_publishing = True,
                listings = [
                    openapi_client.models.azure_product_listing.AzureProductListing(
                        access_information = '', 
                        assets = [
                            openapi_client.models.azure_product_listing_asset.AzureProductListingAsset(
                                description = '', 
                                file_name = '', 
                                file_sas_uri = '', 
                                friendly_name = '', 
                                id = '', 
                                order = 56, 
                                publisher_defined_sas_uri = '', 
                                resource_type = 'ListingAsset', 
                                state = 'PendingUpload', 
                                type = '', )
                            ], 
                        compatible_products = [
                            ''
                            ], 
                        description = '', 
                        getting_started_instructions = '', 
                        id = '', 
                        keywords = [
                            ''
                            ], 
                        language_code = '', 
                        listing_contacts = [
                            openapi_client.models.azure_listing_contact.AzureListingContact(
                                email = '', 
                                name = '', 
                                phone = '', 
                                type = 'CustomerSupport', 
                                uri = '', )
                            ], 
                        listing_uris = [
                            openapi_client.models.azure_listing_uri.AzureListingUri(
                                display_text = '', 
                                subtype = '', 
                                type = '', 
                                uri = '', )
                            ], 
                        product_display_name = '', 
                        publisher_name = '', 
                        resource_type = 'AzureListing', 
                        short_description = '', 
                        summary = '', 
                        title = '', )
                    ],
                name = '',
                package_configurations = [
                    openapi_client.models.azure_product_package_configuration.AzureProductPackageConfiguration(
                        azure_active_directory_application_id = '', 
                        azure_active_directory_tenant_id = '', 
                        connection_webhook = '', 
                        id = '', 
                        landing_page_uri = '', 
                        resource_type = 'AzureSoftwareAsAServicePackageConfiguration', )
                    ],
                plans = [
                    openapi_client.models.azure_marketplace_price_and_availability_private_offer_plan.AzureMarketplacePriceAndAvailabilityPrivateOfferPlan(
                        __schema = '', 
                        id = '', 
                        plan = '', 
                        plan_name = '', 
                        pricing = openapi_client.models.azure_marketplace_price_and_availability_private_offer_price.AzureMarketplacePriceAndAvailabilityPrivateOfferPrice(
                            custom_meters = openapi_client.models.azure_marketplace_price_and_availability_private_offer_custom_meters.AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters(
                                meters = openapi_client.models.meters.meters(), 
                                price_input_option = 'perMarket', ), 
                            recurrent_price = openapi_client.models.azure_marketplace_price_and_availability_recurrent_price.AzureMarketplacePriceAndAvailabilityRecurrentPrice(
                                price_input_option = 'perMarket', 
                                prices = [
                                    openapi_client.models.azure_marketplace_price_and_availability_recurrent_price_item.AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(
                                        billing_term = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                            type = 'day', 
                                            value = 1.337, ), 
                                        payment_option = openapi_client.models.azure_marketplace_term.AzureMarketplaceTerm(
                                            type = 'day', 
                                            value = 1.337, ), 
                                        price_per_payment_in_usd = 1.337, )
                                    ], ), ), 
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
                    ],
                properties = [
                    openapi_client.models.azure_product_property.AzureProductProperty(
                        additional_categories = [
                            ''
                            ], 
                        app_version = '', 
                        applicable_products = [
                            ''
                            ], 
                        categories = [
                            ''
                            ], 
                        custom_amendments = [
                            ''
                            ], 
                        extended_properties = [
                            ''
                            ], 
                        global_amendment_terms = '', 
                        hide_keys = [
                            ''
                            ], 
                        id = '', 
                        industries = [
                            ''
                            ], 
                        leveled_categories = { }, 
                        leveled_industries = { }, 
                        marketing_only_change = True, 
                        product_tags = [
                            ''
                            ], 
                        resource_type = '', 
                        submission_version = '', 
                        terms_of_use = '', 
                        use_enterprise_contract = True, )
                    ],
                resource_type = '',
                setup = openapi_client.models.azure_product_setup.AzureProductSetup(
                    call_to_action = 'free', 
                    channel_states = [
                        openapi_client.models.azure_type_value.AzureTypeValue(
                            type = '', 
                            value = '', )
                        ], 
                    enable_test_drive = True, 
                    resource_type = 'AzureProductSetup', 
                    selling_option = 'ListingOnly', 
                    test_drive_type = '', 
                    trial_uri = '', ),
                submissions = [
                    openapi_client.models.azure_product_submission.AzureProductSubmission(
                        are_resources_ready = True, 
                        friendly_name = '', 
                        id = '', 
                        pending_update_info = openapi_client.models.azure_pending_update_info.AzurePendingUpdateInfo(
                            status = '', 
                            update_type = '', ), 
                        published_time_in_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        release_number = 56, 
                        resource_type = 'Submission', 
                        resources = [
                            openapi_client.models.azure_type_value.AzureTypeValue(
                                type = '', 
                                value = '', )
                            ], 
                        state = 'Inprogress', 
                        sub_state = 'InDraft', 
                        targets = [
                            openapi_client.models.azure_type_value.AzureTypeValue(
                                type = '', 
                                value = '', )
                            ], 
                        variant_resources = [
                            openapi_client.models.azure_variant_resource.AzureVariantResource(
                                variant_id = '', )
                            ], )
                    ],
                variants = [
                    openapi_client.models.azure_product_variant.AzureProductVariant(
                        azure_government_certifications = [
                            openapi_client.models.azure_government_certification.AzureGovernmentCertification(
                                title = '', 
                                uri = '', 
                                validation_results = [
                                    openapi_client.models.azure_validation_result.AzureValidationResult(
                                        error_message = '', 
                                        member_names = [
                                            ''
                                            ], )
                                    ], )
                            ], 
                        cloud_availabilities = [
                            ''
                            ], 
                        conversion_paths = '', 
                        extended_properties = [
                            openapi_client.models.azure_type_value.AzureTypeValue(
                                type = '', 
                                value = '', )
                            ], 
                        external_id = '', 
                        feature_availabilities = [
                            openapi_client.models.azure_product_feature_availability.AzureProductFeatureAvailability(
                                custom_meters = [
                                    openapi_client.models.azure_product_variant_custom_meter.AzureProductVariantCustomMeter(
                                        display_name = '', 
                                        id = '', 
                                        included_base_quantities = [
                                            openapi_client.models.azure_included_base_quantity.AzureIncludedBaseQuantity(
                                                is_infinite = True, 
                                                quantity = 1.337, 
                                                recurring_unit = 'Monthly', )
                                            ], 
                                        is_enabled = True, 
                                        price_in_usd = 1.337, 
                                        unique_id = '', 
                                        unit_of_measure = '', )
                                    ], 
                                id = '', 
                                is_hidden = True, 
                                market_states = [
                                    openapi_client.models.azure_market_state.AzureMarketState(
                                        market_code = '', 
                                        state = 'Disabled', )
                                    ], 
                                markets = [
                                    openapi_client.models.azure_market.AzureMarket(
                                        friendly_name = '', 
                                        market_code = '', )
                                    ], 
                                price_schedules = [
                                    openapi_client.models.azure_product_variant_price_schedule.AzureProductVariantPriceSchedule(
                                        date_time_range = openapi_client.models.azure_localized_time_range.AzureLocalizedTimeRange(
                                            end_at = openapi_client.models.azure_localized_date_time.AzureLocalizedDateTime(
                                                date_time_in_utc = '', 
                                                localize_per_market = True, ), 
                                            start_at = openapi_client.models.azure_localized_date_time.AzureLocalizedDateTime(
                                                date_time_in_utc = '', 
                                                localize_per_market = True, ), ), 
                                        friendly_name = '', 
                                        is_base_schedule = True, 
                                        market_codes = [
                                            ''
                                            ], 
                                        schedules = [
                                            openapi_client.models.azure_price_schedule.AzurePriceSchedule(
                                                price_cadence = openapi_client.models.azure_price_cadence.AzurePriceCadence(
                                                    type = 'Month', 
                                                    value = 56, ), 
                                                pricing_model = 'Flat', 
                                                pricing_units = [
                                                    openapi_client.models.azure_pricing_unit.AzurePricingUnit(
                                                        is_unlimited_unit = True, 
                                                        lower_unit = 56, 
                                                        name = 'sharedcore', 
                                                        unit_type = '', 
                                                        upper_unit = 56, )
                                                    ], 
                                                retail_price = openapi_client.models.azure_price.AzurePrice(
                                                    currency_code = '', 
                                                    open_price = 1.337, 
                                                    price_tier_id = '', ), )
                                            ], )
                                    ], 
                                properties = [
                                    openapi_client.models.azure_type_value.AzureTypeValue(
                                        type = '', 
                                        value = '', )
                                    ], 
                                resource_type = '', 
                                subscription_audiences = [
                                    openapi_client.models.azure_audience.AzureAudience(
                                        description = '', 
                                        id = '', )
                                    ], 
                                tenant_audiences = [
                                    openapi_client.models.azure_audience.AzureAudience(
                                        description = '', 
                                        id = '', )
                                    ], 
                                trial = openapi_client.models.azure_product_variant_trial.AzureProductVariantTrial(
                                    duration = 56, 
                                    duration_type = 'Minute', 
                                    type = 'NoTrial', ), 
                                visibility = 'Public', )
                            ], 
                        friendly_name = '', 
                        id = '', 
                        lead_gen_id = '', 
                        reference_variant_id = '', 
                        resource_type = 'AzureSkuVariant', 
                        state = 'InActive', )
                    ]
            )
        else:
            return AzureProduct(
        )
        """

    def testAzureProduct(self):
        """Test AzureProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
