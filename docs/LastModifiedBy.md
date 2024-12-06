# LastModifiedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the creator. | [optional] 
**entity_id** | **str** | The ID of the creator. | [optional] 
**entity_type** | [**EntityType**](EntityType.md) | The Entity type of the creator, either USER or API_CLIENT. | [optional] 
**name** | **str** | The name of the creator. | [optional] 

## Example

```python
from suger_sdk_python.models.last_modified_by import LastModifiedBy

# TODO update the JSON string below
json = "{}"
# create an instance of LastModifiedBy from a JSON string
last_modified_by_instance = LastModifiedBy.from_json(json)
# print the JSON string representation of the object
print(LastModifiedBy.to_json())

# convert the object into a dict
last_modified_by_dict = last_modified_by_instance.to_dict()
# create an instance of LastModifiedBy from a dict
last_modified_by_from_dict = LastModifiedBy.from_dict(last_modified_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


