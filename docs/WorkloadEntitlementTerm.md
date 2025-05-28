# WorkloadEntitlementTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**commit_amount** | **float** |  | [optional] 
**creation_time** | **str** |  | [optional] 
**credit_amount** | **float** |  | [optional] 
**end_time** | **datetime** | nullable | [optional] 
**entitlement_id** | **str** |  | [optional] 
**entitlement_info** | [**EntitlementInfo**](EntitlementInfo.md) |  | [optional] 
**external_entitlement_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**EntitlementTermInfo**](EntitlementTermInfo.md) |  | [optional] 
**last_update_time** | **str** |  | [optional] 
**offer_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**product_id** | **str** |  | [optional] 
**reported_amount** | **float** |  | [optional] 
**service** | [**PartnerService**](PartnerService.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**used_commit_amount** | **float** |  | [optional] 
**used_credit_amount** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.workload_entitlement_term import WorkloadEntitlementTerm

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadEntitlementTerm from a JSON string
workload_entitlement_term_instance = WorkloadEntitlementTerm.from_json(json)
# print the JSON string representation of the object
print(WorkloadEntitlementTerm.to_json())

# convert the object into a dict
workload_entitlement_term_dict = workload_entitlement_term_instance.to_dict()
# create an instance of WorkloadEntitlementTerm from a dict
workload_entitlement_term_from_dict = WorkloadEntitlementTerm.from_dict(workload_entitlement_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


