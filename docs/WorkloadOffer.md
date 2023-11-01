# WorkloadOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **List[str]** |  | [optional] 
**created_by** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**end_time** | **datetime** | nullable | [optional] 
**expire_time** | **datetime** | nullable | [optional] 
**external_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**OfferInfo**](OfferInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**last_updated_by** | **str** |  | [optional] 
**meta_info** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md) |  | [optional] 
**name** | **str** |  | [optional] 
**offer_type** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**product_id** | **str** |  | [optional] 
**service** | [**PartnerService**](PartnerService.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workload_offer import WorkloadOffer

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadOffer from a JSON string
workload_offer_instance = WorkloadOffer.from_json(json)
# print the JSON string representation of the object
print WorkloadOffer.to_json()

# convert the object into a dict
workload_offer_dict = workload_offer_instance.to_dict()
# create an instance of WorkloadOffer from a dict
workload_offer_form_dict = workload_offer.from_dict(workload_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


