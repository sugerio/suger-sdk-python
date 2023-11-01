# GcpMarketplacePrivateOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_entitlement** | [**GcpMarketplaceEntitlement**](GcpMarketplaceEntitlement.md) |  | [optional] 
**agency_enabled** | **bool** |  | [optional] 
**agreement** | **str** | The resource name of agreement(entitlement) In format of \&quot;projects/{projectNumber}/agreements/{agreementId}\&quot; | [optional] 
**cancel_time** | **datetime** |  | [optional] 
**custom_eula** | [**GcpMarketplaceDocument**](GcpMarketplaceDocument.md) |  | [optional] 
**customer_info** | [**GcpMarketplacePrivateOfferCustomerInfo**](GcpMarketplacePrivateOfferCustomerInfo.md) |  | [optional] 
**eula_agreement_document** | [**GcpMarketplaceDocument**](GcpMarketplaceDocument.md) |  | [optional] 
**existing_offer_data** | [**GcpMarketplaceExistingOfferData**](GcpMarketplaceExistingOfferData.md) |  | [optional] 
**expire_time** | **datetime** |  | [optional] 
**features** | [**List[GcpMarketplaceProductFeatureValue]**](GcpMarketplaceProductFeatureValue.md) |  | [optional] 
**installment_timeline** | [**GcpMarketplacePrivateOfferInstallmentTimeline**](GcpMarketplacePrivateOfferInstallmentTimeline.md) |  | [optional] 
**lifecycle_state** | **str** | such as \&quot;PUBLISHED\&quot; | [optional] 
**metric_information** | [**GcpMarketplacePrivateOfferMetricInformation**](GcpMarketplacePrivateOfferMetricInformation.md) |  | [optional] 
**migration_metadata** | [**GcpMarketplacePrivateOfferMigrationMetadata**](GcpMarketplacePrivateOfferMigrationMetadata.md) |  | [optional] 
**name** | **str** | In format of \&quot;projects/{projectNumber}/services/{serviceName, such as service-name.endpoints.gcp-project-id.cloud.goog}/privateOffers/{privateOfferId}\&quot; | [optional] 
**offer_id** | **str** | GCP private offer ID | [optional] 
**offer_source** | **str** | such as \&quot;OFFER\&quot; | [optional] 
**offer_state** | [**GcpMarketplacePrivateOfferState**](GcpMarketplacePrivateOfferState.md) |  | [optional] 
**offer_term** | [**GcpMarketplacePrivateOfferTerm**](GcpMarketplacePrivateOfferTerm.md) |  | [optional] 
**payment_schedule** | [**GcpMarketplacePaymentScheduleType**](GcpMarketplacePaymentScheduleType.md) |  | [optional] 
**policies** | **Dict[str, str]** |  | [optional] 
**price_model** | [**GcpMarketplacePrivateOfferPriceModel**](GcpMarketplacePrivateOfferPriceModel.md) |  | [optional] 
**price_model_type** | [**GcpMarketplacePrivateOfferPriceModelType**](GcpMarketplacePrivateOfferPriceModelType.md) |  | [optional] 
**provider_cancellation_internal_note** | **str** |  | [optional] 
**provider_info** | [**GcpMarketplacePrivateOfferProviderInfo**](GcpMarketplacePrivateOfferProviderInfo.md) |  | [optional] 
**provider_internal_note** | **str** |  | [optional] 
**provider_public_note** | **str** |  | [optional] 
**purchase_channel** | [**GcpMarketplacePurchaseChannel**](GcpMarketplacePurchaseChannel.md) |  | [optional] 
**purchase_time** | **datetime** |  | [optional] 
**replacement_metadata** | [**GcpMarketplacePrivateOfferReplacementMetadata**](GcpMarketplacePrivateOfferReplacementMetadata.md) |  | [optional] 
**service_level** | **str** | The Plan of the offer. | [optional] 
**update_time** | **datetime** |  | [optional] 
**use_legacy_partner_eula** | **bool** |  | [optional] 
**user_labels** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer import GcpMarketplacePrivateOffer

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOffer from a JSON string
gcp_marketplace_private_offer_instance = GcpMarketplacePrivateOffer.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOffer.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_dict = gcp_marketplace_private_offer_instance.to_dict()
# create an instance of GcpMarketplacePrivateOffer from a dict
gcp_marketplace_private_offer_form_dict = gcp_marketplace_private_offer.from_dict(gcp_marketplace_private_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


