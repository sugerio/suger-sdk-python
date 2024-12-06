# NotificationMessageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**NotificationEventAction**](NotificationEventAction.md) | The action of this notification message. | [optional] 
**cc_recipients** | **List[str]** |  | [optional] 
**custom_fields** | **Dict[str, object]** | All other fields | [optional] 
**html_content** | **str** | The HTML content of the email. | [optional] 
**rcc_recipients** | **List[str]** |  | [optional] 
**standard_fields** | **Dict[str, object]** | The standard fields to render the email content. | [optional] 
**subject** | **str** |  | [optional] 
**text_content** | **str** | The text content of the email in case the recipient&#39;s email client does not support HTML. | [optional] 

## Example

```python
from suger_sdk_python.models.notification_message_info import NotificationMessageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationMessageInfo from a JSON string
notification_message_info_instance = NotificationMessageInfo.from_json(json)
# print the JSON string representation of the object
print(NotificationMessageInfo.to_json())

# convert the object into a dict
notification_message_info_dict = notification_message_info_instance.to_dict()
# create an instance of NotificationMessageInfo from a dict
notification_message_info_from_dict = NotificationMessageInfo.from_dict(notification_message_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


