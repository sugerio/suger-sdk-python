# NotificationEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**NotificationEventAction**](NotificationEventAction.md) |  | [optional] 
**cc_contact_ids** | **List[str]** | Cc contactIds that will receive this notification | [optional] 
**contact_ids** | **List[str]** | ContactIds that will receive this notification | [optional] 
**entity_id** | **str** |  | [optional] 
**entity_status** | **str** |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 
**event_id** | **str** | notification event id. | [optional] 
**event_status** | [**NotificationEventStatus**](NotificationEventStatus.md) |  | [optional] 
**last_update_time** | **datetime** | timestamp of the event when it is updated. | [optional] 
**message** | **str** |  | [optional] 
**organization_id** | **str** | suger organization id. | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**timestamp** | **datetime** | timestamp of the event when it is scheduled or created. | [optional] 
**title** | **str** | The title of the notification event such as email subject. | [optional] 
**track_events** | [**List[TrackEvent]**](TrackEvent.md) | The track events of the notification event. | [optional] 

## Example

```python
from openapi_client.models.notification_event import NotificationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEvent from a JSON string
notification_event_instance = NotificationEvent.from_json(json)
# print the JSON string representation of the object
print NotificationEvent.to_json()

# convert the object into a dict
notification_event_dict = notification_event_instance.to_dict()
# create an instance of NotificationEvent from a dict
notification_event_form_dict = notification_event.from_dict(notification_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


