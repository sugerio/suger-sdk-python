# OfferInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_eula_type** | [**EulaType**](EulaType.md) |  | [optional] 
**auto_renew** | **bool** | Is this offer Auto Renew enabled. | [optional] 
**aws_cppo_event_detail** | [**AwsMarketplaceEventBridgeEventDetail**](AwsMarketplaceEventBridgeEventDetail.md) |  | [optional] 
**aws_cppo_opportunity** | [**AwsMarketplaceCppoOpportunity**](AwsMarketplaceCppoOpportunity.md) |  | [optional] 
**azure_original_plan** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlan**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) |  | [optional] 
**azure_private_offer** | [**AzureMarketplacePrivateOffer**](AzureMarketplacePrivateOffer.md) |  | [optional] 
**azure_product_variant** | [**AzureProductVariant**](AzureProductVariant.md) |  | [optional] 
**buyer_aws_account_ids** | **List[str]** | The buyers&#39; AWS Account IDs of this offer. | [optional] 
**buyer_azure_tenants** | [**List[AzureAudience]**](AzureAudience.md) | The buyers&#39; Azure tenants of this offer. | [optional] 
**commit_amount** | **float** | The amount that the buyer has committed to pay, before discount if applicable. It can be monthly commitment or total commitment. | [optional] 
**commits** | [**List[CommitDimension]**](CommitDimension.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**dimensions** | [**List[MeteringDimension]**](MeteringDimension.md) |  | [optional] 
**discount_percentage** | **float** | The discount percentage off the original price. For example, 20 means 20% off. 0 means no discount. It can be discount off the commitment amount or discount off the usage price. | [optional] 
**eula_type** | [**EulaType**](EulaType.md) |  | [optional] 
**eula_url** | **str** |  | [optional] 
**gcp_customer_info** | [**GcpMarketplacePrivateOfferCustomerInfo**](GcpMarketplacePrivateOfferCustomerInfo.md) |  | [optional] 
**gcp_duration** | **int** | The duration of the offer in months. Only required when creating GCP Marketplace private offer. | [optional] 
**gcp_metrics** | [**List[GcpMarketplaceProductMeteringMetric]**](GcpMarketplaceProductMeteringMetric.md) | Only applicable for GCP Marketplace Offers (the default or private offer) | [optional] 
**gcp_payment_schedule** | [**GcpMarketplacePaymentScheduleType**](GcpMarketplacePaymentScheduleType.md) |  | [optional] 
**gcp_plans** | [**List[GcpMarketplaceProductPurchaseOptionSpec]**](GcpMarketplaceProductPurchaseOptionSpec.md) | Only applicable for GCP Marketplace | [optional] 
**gcp_private_offer** | [**GcpMarketplacePrivateOffer**](GcpMarketplacePrivateOffer.md) |  | [optional] 
**gcp_provider_info** | [**GcpMarketplacePrivateOfferProviderInfo**](GcpMarketplacePrivateOfferProviderInfo.md) |  | [optional] 
**gcp_provider_internal_note** | **str** | Optional when creating GCP Marketplace private offer. The internal note for the seller/ISV. It is only visible to the seller/ISV. | [optional] 
**gcp_provider_public_note** | **str** | Optional when creating GCP Marketplace private offer. The public note for the buyer. It is visible to the buyer. | [optional] 
**gcp_usage_plan_price_model** | [**GcpMarketplaceUsagePlanPriceModel**](GcpMarketplaceUsagePlanPriceModel.md) |  | [optional] 
**payment_installments** | [**List[PaymentInstallment]**](PaymentInstallment.md) | For flexible payment schedule. | [optional] 
**private_offer_url** | **str** | The URL of the private offer sent to buyers to accept. Only applicable for private offer. | [optional] 
**refund_cancelation_policy** | **str** |  | [optional] 
**seller_notes** | **str** |  | [optional] 
**visibility** | **str** | The default visibility of offer is PRIVATE. | [optional] 

## Example

```python
from openapi_client.models.offer_info import OfferInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInfo from a JSON string
offer_info_instance = OfferInfo.from_json(json)
# print the JSON string representation of the object
print OfferInfo.to_json()

# convert the object into a dict
offer_info_dict = offer_info_instance.to_dict()
# create an instance of OfferInfo from a dict
offer_info_form_dict = offer_info.from_dict(offer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


