# WorkloadEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**end_time** | **datetime** | nullable | [optional] 
**entitlement_term_id** | **str** |  | [optional] 
**external_buyer_id** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**external_product_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**EntitlementInfo**](EntitlementInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**meta_info** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md) |  | [optional] 
**name** | **str** |  | [optional] 
**offer_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**partner_id** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**service** | [**PartnerService**](PartnerService.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | [**EntitlementStatus**](EntitlementStatus.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadEntitlement from a JSON string
workload_entitlement_instance = WorkloadEntitlement.from_json(json)
# print the JSON string representation of the object
print(WorkloadEntitlement.to_json())

# convert the object into a dict
workload_entitlement_dict = workload_entitlement_instance.to_dict()
# create an instance of WorkloadEntitlement from a dict
workload_entitlement_from_dict = WorkloadEntitlement.from_dict(workload_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


