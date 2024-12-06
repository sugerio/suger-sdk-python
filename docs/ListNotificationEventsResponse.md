# ListNotificationEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** | If it is nil, it means there is no more records. | [optional] 
**notification_events** | [**List[NotificationEvent]**](NotificationEvent.md) |  | [optional] 
**total_count** | **int** | Only available when the request is made with offset&#x3D;0. | [optional] 

## Example

```python
from suger_sdk_python.models.list_notification_events_response import ListNotificationEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationEventsResponse from a JSON string
list_notification_events_response_instance = ListNotificationEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotificationEventsResponse.to_json())

# convert the object into a dict
list_notification_events_response_dict = list_notification_events_response_instance.to_dict()
# create an instance of ListNotificationEventsResponse from a dict
list_notification_events_response_from_dict = ListNotificationEventsResponse.from_dict(list_notification_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


