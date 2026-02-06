# OperationHistoryEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**event_id** | **int** |  | [optional] 
**event_time** | **datetime** |  | [optional] 
**event_type** | **str** |  | [optional] 
**task_id** | **int** |  | [optional] 
**version** | **int** |  | [optional] 
**worker_may_ignore** | **bool** |  | [optional] 

## Example

```python
from suger_sdk_python.models.operation_history_event import OperationHistoryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OperationHistoryEvent from a JSON string
operation_history_event_instance = OperationHistoryEvent.from_json(json)
# print the JSON string representation of the object
print(OperationHistoryEvent.to_json())

# convert the object into a dict
operation_history_event_dict = operation_history_event_instance.to_dict()
# create an instance of OperationHistoryEvent from a dict
operation_history_event_from_dict = OperationHistoryEvent.from_dict(operation_history_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


