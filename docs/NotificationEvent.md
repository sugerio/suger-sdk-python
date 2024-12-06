# NotificationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**NotificationEventAction**](NotificationEventAction.md) |  | [optional] 
**cc_contact_ids** | **List[str]** | Cc contactIds that will receive this notification | [optional] 
**channels** | [**List[NotificationChannel]**](NotificationChannel.md) | The list of channels this event will be sent to, e.g., [\&quot;SLACK\&quot;, \&quot;EMAIL\&quot;] | [optional] 
**contact_emails** | **List[str]** | Contact emails that will receive this notification | [optional] 
**contact_ids** | **List[str]** | ContactIds that will receive this notification | [optional] 
**created_by** | [**LastModifiedBy**](LastModifiedBy.md) | Who originally created or triggered this notification event. It can be user or API client. | [optional] 
**custom_fields** | **Dict[str, object]** | Custom fields of the notification event. | [optional] 
**entity_id** | **str** |  | [optional] 
**entity_name** | **str** | The name of the entity. | [optional] 
**entity_status** | **str** |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 
**event_id** | **str** | notification event id. | [optional] 
**event_status** | [**NotificationEventStatus**](NotificationEventStatus.md) | notification event status. | [optional] 
**info** | **object** | Additional info of the notification event. | [optional] 
**is_action_item** | **bool** | If this notification event is an action item. | [optional] 
**last_update_time** | **datetime** | timestamp of the event when it is updated. | [optional] 
**message** | **str** | The message of the notification event such as email body, action item description. | [optional] 
**organization_id** | **str** | suger organization id. | [optional] 
**partner** | [**Partner**](Partner.md) | the partner of the entity. Optional. | [optional] 
**priority** | [**AuditingEventPriority**](AuditingEventPriority.md) | The priority of the notification event. | [optional] 
**require_audit** | **bool** | If this notification event is an auditing event and need to store in DB. | [optional] 
**timestamp** | **datetime** | timestamp of the event when it is scheduled or created. | [optional] 
**title** | **str** | The title of the notification event such as email subject, action item title. | [optional] 
**track_events** | [**List[TrackEvent]**](TrackEvent.md) | The track events of the notification event. | [optional] 

## Example

```python
from suger_sdk_python.models.notification_event import NotificationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEvent from a JSON string
notification_event_instance = NotificationEvent.from_json(json)
# print the JSON string representation of the object
print(NotificationEvent.to_json())

# convert the object into a dict
notification_event_dict = notification_event_instance.to_dict()
# create an instance of NotificationEvent from a dict
notification_event_from_dict = NotificationEvent.from_dict(notification_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


