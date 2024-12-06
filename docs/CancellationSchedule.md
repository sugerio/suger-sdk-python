# CancellationSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_date** | **str** | The cancellation date of the entitlement. It is required when the type is SpecificDate. | [optional] 
**creation_date** | **str** | When this cancellation schedule is created. | [optional] 
**note** | **str** | The cancellation note. Max 500 characters. | [optional] 
**type** | [**CancellationScheduleType**](CancellationScheduleType.md) | Cancellation type | [optional] 

## Example

```python
from suger_sdk_python.models.cancellation_schedule import CancellationSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationSchedule from a JSON string
cancellation_schedule_instance = CancellationSchedule.from_json(json)
# print the JSON string representation of the object
print(CancellationSchedule.to_json())

# convert the object into a dict
cancellation_schedule_dict = cancellation_schedule_instance.to_dict()
# create an instance of CancellationSchedule from a dict
cancellation_schedule_from_dict = CancellationSchedule.from_dict(cancellation_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


