# UsageAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** |  | [optional] 
**tags** | [**List[UsageAllocationTag]**](UsageAllocationTag.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.usage_allocation import UsageAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAllocation from a JSON string
usage_allocation_instance = UsageAllocation.from_json(json)
# print the JSON string representation of the object
print(UsageAllocation.to_json())

# convert the object into a dict
usage_allocation_dict = usage_allocation_instance.to_dict()
# create an instance of UsageAllocation from a dict
usage_allocation_from_dict = UsageAllocation.from_dict(usage_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


