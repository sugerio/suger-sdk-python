# OperationEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_history_event** | [**List[OperationHistoryEvent]**](OperationHistoryEvent.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.operation_events_response import OperationEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OperationEventsResponse from a JSON string
operation_events_response_instance = OperationEventsResponse.from_json(json)
# print the JSON string representation of the object
print(OperationEventsResponse.to_json())

# convert the object into a dict
operation_events_response_dict = operation_events_response_instance.to_dict()
# create an instance of OperationEventsResponse from a dict
operation_events_response_from_dict = OperationEventsResponse.from_dict(operation_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


