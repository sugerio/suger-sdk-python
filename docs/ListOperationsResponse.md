# ListOperationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_token** | **str** |  | [optional] 
**operations** | [**List[Operation]**](Operation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.list_operations_response import ListOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOperationsResponse from a JSON string
list_operations_response_instance = ListOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListOperationsResponse.to_json())

# convert the object into a dict
list_operations_response_dict = list_operations_response_instance.to_dict()
# create an instance of ListOperationsResponse from a dict
list_operations_response_from_dict = ListOperationsResponse.from_dict(list_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


