# UsageAllocationTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.usage_allocation_tag import UsageAllocationTag

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAllocationTag from a JSON string
usage_allocation_tag_instance = UsageAllocationTag.from_json(json)
# print the JSON string representation of the object
print(UsageAllocationTag.to_json())

# convert the object into a dict
usage_allocation_tag_dict = usage_allocation_tag_instance.to_dict()
# create an instance of UsageAllocationTag from a dict
usage_allocation_tag_from_dict = UsageAllocationTag.from_dict(usage_allocation_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


