# OfferInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_eula_urls** | **List[str]** | The URL of the additional EULA files. Only applicable when EulaType &#x3D; CUSTOM. The additional EULA files will be attached to the EULA file in the EulaUrl, and form a single EULA file. | [optional] 
**additional_reseller_eula_urls** | **List[str]** | The URL of the additional reseller EULA files. Only applicable when ResellerEulaType &#x3D; CUSTOM. | [optional] 
**attach_eula_type** | [**EulaType**](EulaType.md) | Attach the standard EULA file to the CUSTOM EULA file. Only applicable when EulaType &#x3D; CUSTOM | [optional] 
**auto_renew** | **bool** | Is this offer Auto Renew enabled. | [optional] 
**aws_agreement_duration** | **str** | Aws private subscription offer Usage duration. ISO8601 format. P300D means the contract Usage start date At acceptance, and with duration 300 days. | [optional] 
**aws_channel_partner** | [**AwsChannelPartner**](AwsChannelPartner.md) | The AWS channel partner (reseller), only applicable for AWS Marketplace CPPO_OUT or CPPO offers. | [optional] 
**aws_cppo_event_detail** | [**AwsMarketplaceEventBridgeEventDetail**](AwsMarketplaceEventBridgeEventDetail.md) | AWS EventBridge Event, only applicable for AWS Marketplace CPPO offers. | [optional] 
**aws_cppo_opportunity** | [**AwsMarketplaceCppoOpportunity**](AwsMarketplaceCppoOpportunity.md) | AWS CPPO Opportunity, only applicable for AWS Marketplace CPPO_OUT or CPPO_IN offers. | [optional] 
**aws_markup_percentage** | **float** | AWS private reseller offer using markup percentage. 10.0 represent 10% partner margin. | [optional] 
**aws_resale_authorization_id** | **str** | AWS ResaleAuthorizationId(CPPO_IN offer id) for CPPO offers of the reseller. | [optional] 
**azure_original_plan** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlan**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) | The origin pricing of Azure plan. Only applicable for Azure Marketplace plans. | [optional] 
**azure_private_offer** | [**AzureMarketplacePrivateOffer**](AzureMarketplacePrivateOffer.md) | The private offer for Azure Marketplace. Only applicable for Azure Marketplace private offers. | [optional] 
**azure_product_variant** | [**AzureProductVariant**](AzureProductVariant.md) | For Azure marketplace only. | [optional] 
**billable_dimensions** | [**List[BillableDimension]**](BillableDimension.md) | Usage based metering dimensions based on Billable Metrics, managed by Suger only. | [optional] 
**billing_cycle** | [**BillingCycle**](BillingCycle.md) | Billing Cycle for the offer. | [optional] 
**billing_interval_in_months** | **int** | Billing interval in months for the offer. | [optional] 
**buyer_aws_account_ids** | **List[str]** | The buyers&#39; AWS Account IDs of this offer. | [optional] 
**buyer_azure_tenants** | [**List[AzureAudience]**](AzureAudience.md) | The buyers&#39; Azure tenants of this offer. | [optional] 
**commit_amount** | **float** | The amount that the buyer has committed to pay, before discount if applicable. It can be monthly commitment or total commitment. For frontend display or analysis purposes, not used for billing. | [optional] 
**commit_billing_interval_in_months** | **int** | Deprecated: Use BillingIntervalInMonths instead. | [optional] 
**commits** | [**List[CommitDimension]**](CommitDimension.md) | Recurring flat fee for the offer, managed by cloud marketplaces or Suger. | [optional] 
**currency** | **str** | The currency code of the offer. ISO 4217 format. | [optional] 
**dimensions** | [**List[MeteringDimension]**](MeteringDimension.md) | Usage based metering dimensions defined on cloud marketplaces, managed by Cloud marketplaces only. | [optional] 
**discount_percentage** | **float** | The discount percentage off the original price. For example, 20 means 20% off. 0 means no discount. It can be discount off the commitment amount or discount off the usage price. | [optional] 
**eula_type** | [**EulaType**](EulaType.md) |  | [optional] 
**eula_url** | **str** |  | [optional] 
**gcp_customer_info** | [**GcpMarketplacePrivateOfferCustomerInfo**](GcpMarketplacePrivateOfferCustomerInfo.md) | Only required when creating GCP Marketplace private offer. | [optional] 
**gcp_duration** | **int** | The duration of the offer in months. Only required when creating GCP Marketplace private offer. | [optional] 
**gcp_metrics** | [**List[GcpMarketplaceProductMeteringMetric]**](GcpMarketplaceProductMeteringMetric.md) | Only applicable for GCP Marketplace Offers (the default or private offer) | [optional] 
**gcp_payment_schedule** | [**PaymentScheduleType**](PaymentScheduleType.md) | Only required when creating GCP Marketplace private offer, to specify the payment schedule for the private offer. TODO: It will be deprecated in the future and replaced by PaymentSchedule. | [optional] 
**gcp_plans** | [**List[GcpMarketplaceProductPurchaseOptionSpec]**](GcpMarketplaceProductPurchaseOptionSpec.md) | Only applicable for GCP Marketplace | [optional] 
**gcp_private_offer** | [**GcpMarketplacePrivateOffer**](GcpMarketplacePrivateOffer.md) | The private offer for GCP Marketplace. Only applicable for GCP Marketplace private offers. | [optional] 
**gcp_provider_info** | [**GcpMarketplacePrivateOfferProviderInfo**](GcpMarketplacePrivateOfferProviderInfo.md) | Only required when creating GCP Marketplace private offer. | [optional] 
**gcp_provider_internal_note** | **str** | Optional when creating GCP Marketplace private offer. The internal note for the seller/ISV. It is only visible to the seller/ISV. | [optional] 
**gcp_provider_public_note** | **str** | Optional when creating GCP Marketplace private offer. By default, it is the same as offer name. The public note for the buyer. It is visible to the buyer. | [optional] 
**gcp_reseller_private_offer_plan** | [**GcpMarketplaceResellerPrivateOfferPlan**](GcpMarketplaceResellerPrivateOfferPlan.md) |  | [optional] 
**gcp_usage_plan_price_model** | [**GcpMarketplaceUsagePlanPriceModel**](GcpMarketplaceUsagePlanPriceModel.md) | Only applicable for GCP Marketplace with Usage plan. Not appliable for Subscription plan. | [optional] 
**grace_period_in_days** | **int** | The grace period in days for the offer. This is the number of days during which invoices remain in draft status, for reviewing. This filed can be overridden at the entitlement level. | [optional] 
**is_metering_overage_commit** | **bool** | Whether the usage metering will only be charged for the amount that exceeds the committed amount. e.g. the buyer has committed $100, and the usage is $120, - if true, the buyer will be charged for the usage at $20, and the commit at $100. - if false, the buyer will be charged for the usage at $120, and the commit at $100. | [optional] 
**net_terms_in_days** | **int** | The net terms in days for the offer. This is the number of days the buyer has to pay the invoice. This filed can be overridden at the entitlement level. | [optional] 
**payment_installments** | [**List[PaymentInstallment]**](PaymentInstallment.md) | For flexible payment schedule, managed by cloud marketplaces or Suger. | [optional] 
**payment_schedule** | [**PaymentScheduleType**](PaymentScheduleType.md) | The payment schedule for the offer. PREPAY means the buyer pays before the service is provided. POSTPAY means the buyer pays after the service is provided. | [optional] 
**private_offer_url** | **str** | The URL of the private offer sent to buyers to accept. Only applicable for private offer. | [optional] 
**prorated_billing** | **bool** | Prorated billing for the offer. If true, the billing is prorated based on the start date and end date. If false, the billing is not prorated. This filed can be overridden at the entitlement level. | [optional] 
**refund_cancellation_policy** | **str** |  | [optional] 
**reseller_attach_eula_type** | [**EulaType**](EulaType.md) | Attach the standard EULA file to the CUSTOM EULA file. Only applicable when EulaType &#x3D; CUSTOM | [optional] 
**reseller_eula_type** | [**EulaType**](EulaType.md) | The type of the reseller EULA. Only applicable for CPPO offers. | [optional] 
**reseller_eula_url** | **str** |  | [optional] 
**seller_notes** | **str** |  | [optional] 
**start_time** | **datetime** | Optional when creating AWS or GCP Marketplace private offer on the contract product. The future start time of the offer if it is not started on the acceptance. | [optional] 
**tax_ids** | **List[str]** | Tax ids for the offer, used to calculate the tax amount for the offer. This field can be overridden at the entitlement level. | [optional] 
**trial_config** | [**TrialConfig**](TrialConfig.md) | The offer for Direct. Only applicable for Direct offers. It is used in Stripe, Adyen, and other direct payment providers. The trial configuration for the offer. | [optional] 
**usage_billing_interval_in_months** | **int** | Deprecated: Use BillingIntervalInMonths instead. | [optional] 
**visibility** | **str** | The default visibility of offer is PRIVATE. | [optional] 

## Example

```python
from suger_sdk_python.models.offer_info import OfferInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInfo from a JSON string
offer_info_instance = OfferInfo.from_json(json)
# print the JSON string representation of the object
print(OfferInfo.to_json())

# convert the object into a dict
offer_info_dict = offer_info_instance.to_dict()
# create an instance of OfferInfo from a dict
offer_info_from_dict = OfferInfo.from_dict(offer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


