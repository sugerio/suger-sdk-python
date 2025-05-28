# WorkloadMetaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ace_apn_crm_unique_identifier** | **str** | The linked ACE ApnCrmUniqueIdentifier of the private offer if available. | [optional] 
**aws_saas_product_dimensions** | [**List[AwsProductDimension]**](AwsProductDimension.md) | The AWS SaaS product dimensions. Applicable for AWS SaaS products only. This is used to save price info when creating AWS SaaS product. | [optional] 
**base_agreement_id** | **str** | Applicable for AWS Marketplace only, when the IsAgreementBasedOffer is true. | [optional] 
**buyer_ids** | **List[str]** | The Suger buyer IDs of the private offer if available. | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The contacts of the offer to notify if any updates. | [optional] 
**cppo_in_offer_id** | **str** | The Suger CPPO_IN offer ID. | [optional] 
**cppo_offer_id** | **str** | The Suger CPPO offer ID. Reseller to end buyer | [optional] 
**cppo_out_offer_id** | **str** | The Suger CPPO_OUT offer ID. ISV to reseller | [optional] 
**custom_meta_info** | **Dict[str, str]** | The custom meta info of the offer can be updated by seller via API or console. | [optional] 
**enable_test_usage_metering** | **bool** | If enabled, Suger will test metering the usage for this entitlement hourly. | [optional] 
**entitlement_cancellation_schedule** | [**CancellationSchedule**](CancellationSchedule.md) | The cancellation schedule for the entitlement. It is nill if no cancellation schedule. | [optional] 
**error_messages** | **List[str]** | The error messages when the offer is invalid or offer related tasks failed. This is the raw error messages from the offer related tasks. | [optional] 
**hubspot_deal_id** | **str** | Hubsport deal ID of the private offer if available. | [optional] 
**internal_note** | **str** | The Internal note of the private offer. It is only visible to the seller/ISV, not visible to the buyer. Up to 1000 characters. | [optional] 
**is_agreement_based_offer** | **bool** | Applicable for AWS Marketplace only, If this offer is agreement based offer. | [optional] 
**is_gross_revenue_full_sync** | **bool** | Whether the gross revenue is fully synced for the entitlement. | [optional] 
**is_renewal_offer** | **bool** | Applicable for AWS Marketplace only. If this offer is renewal offer of existing agreement. The existing agreement can be within or outside AWS Marketplace. AWS may audit and verify your offer is a renewal. If AWS is unable to verify your offer, then AWS may revoke the offer and entitlements from your customer. | [optional] 
**is_replacement_offer** | **bool** | If this offer is a GCP replacement offer. Applicable for GCP Marketplace replacement offer only. | [optional] 
**last_modified_by** | [**LastModifiedBy**](LastModifiedBy.md) | The user who last modified the product/offer/buyer/contact. | [optional] 
**notifications** | [**List[NotificationEvent]**](NotificationEvent.md) | The notifications of the offer if any updates. In most cases, it is to notify contacts/buyers when the offer is pending acceptance. | [optional] 
**offer_accept_date** | **datetime** | The date when the offer is accepted by the buyer. Only available when the private offer has been accepted. | [optional] 
**prettified_error_messages** | **List[str]** | The prettified ErrorMessages. Using AI to make it more readable and understandable. The prettified error messages will be used for the offer related UI display. | [optional] 
**renewal_offer_type** | [**AwsRenewalOfferType**](AwsRenewalOfferType.md) | Applicable for AWS Marketplace only, required when the IsRenewalOffer is true. | [optional] 
**replaced_offer_end_time** | **datetime** | The end time of the replaced offer. Applicable for GCP Marketplace replacement offer only. | [optional] 
**replaced_offer_resource_name** | **str** | The resource name of the GCP Marketplace offer that this offer is replacing. In format of \&quot;projects/{gcpProjectNumber}/services/{productServiceName}/privateOffers/{privateOfferId}\&quot; Applicable for GCP Marketplace replacement offer only. | [optional] 
**salesforce_entitlement_url** | **str** | The Salesforce entitlement URL | [optional] 
**salesforce_opportunity_id** | **str** | The Salesforce opportunity ID of the private offer if available. | [optional] 
**test_usage_metering_end_time** | **datetime** | The test usage metering end time. It is used for test usage metering only. Required if EnableTestUsageMetering is true. | [optional] 
**update_message** | **str** | The message to notify when the offer is updated. | [optional] 

## Example

```python
from suger_sdk_python.models.workload_meta_info import WorkloadMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadMetaInfo from a JSON string
workload_meta_info_instance = WorkloadMetaInfo.from_json(json)
# print the JSON string representation of the object
print(WorkloadMetaInfo.to_json())

# convert the object into a dict
workload_meta_info_dict = workload_meta_info_instance.to_dict()
# create an instance of WorkloadMetaInfo from a dict
workload_meta_info_from_dict = WorkloadMetaInfo.from_dict(workload_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


