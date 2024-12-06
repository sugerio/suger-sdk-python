# SupportTicketUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **str** | The Suger user ID. | [optional] 
**is_suger_employee** | **bool** | Whether the user is a Suger employee. | [optional] 
**profile_picture** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.support_ticket_user import SupportTicketUser

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketUser from a JSON string
support_ticket_user_instance = SupportTicketUser.from_json(json)
# print the JSON string representation of the object
print(SupportTicketUser.to_json())

# convert the object into a dict
support_ticket_user_dict = support_ticket_user_instance.to_dict()
# create an instance of SupportTicketUser from a dict
support_ticket_user_from_dict = SupportTicketUser.from_dict(support_ticket_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


