# WorkloadMetaInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_agreement_id** | **str** | Applicable for AWS Marketplace only, when the IsAgreementBasedOffer is true. | [optional] 
**buyer_ids** | **List[str]** | The Suger buyer IDs of the private offer if available. | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The contacts of the offer to notify if any updates. | [optional] 
**custom_meta_info** | **Dict[str, str]** | The custom meta info of the offer can be updated by seller via API or console. | [optional] 
**error_messages** | **List[str]** | The error messages when the offer is invalid or offer related tasks failed. Populated by Suger service. | [optional] 
**hubspot_deal_id** | **str** | Hubsport deal ID of the private offer if available. | [optional] 
**internal_note** | **str** | The Internal note of the private offer. It is only visible to the seller/ISV, not visible to the buyer. Up to 1000 characters. | [optional] 
**is_agreement_based_offer** | **bool** | Applicable for AWS Marketplace only, If this offer is agreement based offer. | [optional] 
**is_renewal_offer** | **bool** | Applicable for AWS Marketplace only. If this offer is renewal offer of existing agreement. The existing agreement can be within or outside AWS Marketplace. AWS may audit and verify your offer is a renewal. If AWS is unable to verify your offer, then AWS may revoke the offer and entitlements from your customer. | [optional] 
**notifications** | [**List[NotificationEvent]**](NotificationEvent.md) | The notifications of the offer if any updates. In most cases, it is to notify contacts/buyers when the offer is pending acceptance. | [optional] 
**renewal_offer_type** | [**AwsRenewalOfferType**](AwsRenewalOfferType.md) |  | [optional] 
**salesforce_opportunity_id** | **str** | The Salesforce opportunity ID of the private offer if available. | [optional] 

## Example

```python
from openapi_client.models.workload_meta_info import WorkloadMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadMetaInfo from a JSON string
workload_meta_info_instance = WorkloadMetaInfo.from_json(json)
# print the JSON string representation of the object
print WorkloadMetaInfo.to_json()

# convert the object into a dict
workload_meta_info_dict = workload_meta_info_instance.to_dict()
# create an instance of WorkloadMetaInfo from a dict
workload_meta_info_form_dict = workload_meta_info.from_dict(workload_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


