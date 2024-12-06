# TrackEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TrackEventActionType**](TrackEventActionType.md) |  | [optional] 
**contact_id** | **str** | The ID of the contact who triggered the track event if applicable. | [optional] 
**timestamp** | **datetime** | timestamp of the track event happened. | [optional] 

## Example

```python
from suger_sdk_python.models.track_event import TrackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TrackEvent from a JSON string
track_event_instance = TrackEvent.from_json(json)
# print the JSON string representation of the object
print(TrackEvent.to_json())

# convert the object into a dict
track_event_dict = track_event_instance.to_dict()
# create an instance of TrackEvent from a dict
track_event_from_dict = TrackEvent.from_dict(track_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


