# UpdateSupportTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**SupportTicketPriority**](SupportTicketPriority.md) |  | 
**watchers** | **List[str]** |  | 

## Example

```python
from suger_sdk_python.models.update_support_ticket_request import UpdateSupportTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSupportTicketRequest from a JSON string
update_support_ticket_request_instance = UpdateSupportTicketRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSupportTicketRequest.to_json())

# convert the object into a dict
update_support_ticket_request_dict = update_support_ticket_request_instance.to_dict()
# create an instance of UpdateSupportTicketRequest from a dict
update_support_ticket_request_from_dict = UpdateSupportTicketRequest.from_dict(update_support_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


