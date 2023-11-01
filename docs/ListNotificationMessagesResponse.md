# ListNotificationMessagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** | The next offset to use in the next request to get the next page of notification messages. If this field is null, there are no more notification messages to get. | [optional] 
**notification_messages** | [**List[NotificationMessage]**](NotificationMessage.md) |  | [optional] 
**total_count** | **int** | The total number of notification messages. Only available when the request is made with the first offset &#x3D; 0. | [optional] 

## Example

```python
from openapi_client.models.list_notification_messages_response import ListNotificationMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationMessagesResponse from a JSON string
list_notification_messages_response_instance = ListNotificationMessagesResponse.from_json(json)
# print the JSON string representation of the object
print ListNotificationMessagesResponse.to_json()

# convert the object into a dict
list_notification_messages_response_dict = list_notification_messages_response_instance.to_dict()
# create an instance of ListNotificationMessagesResponse from a dict
list_notification_messages_response_form_dict = list_notification_messages_response.from_dict(list_notification_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


