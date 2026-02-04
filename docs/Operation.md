# Operation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_workflow_operations** | [**List[Operation]**](Operation.md) | Only populated if it has child workflows. Otherwise it is nil. | [optional] 
**end_time** | **datetime** |  | [optional] 
**id** | **str** | Operation ID. | [optional] 
**memo** | **Dict[str, object]** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**run_id** | **str** | Run ID. | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | [**OperationType**](OperationType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


