# SupportTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[SupportTicketAttachment]**](SupportTicketAttachment.md) |  | [optional] 
**close_time** | **str** |  | [optional] 
**comments** | [**List[SupportTicketComment]**](SupportTicketComment.md) |  | [optional] 
**creation_time** | **str** |  | [optional] 
**creator** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**due_time** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**priority** | [**SupportTicketPriority**](SupportTicketPriority.md) |  | [optional] 
**status** | [**SupportTicketStatus**](SupportTicketStatus.md) |  | [optional] 
**task_type** | [**SupportTicketTaskType**](SupportTicketTaskType.md) |  | [optional] 
**watchers** | **List[str]** |  | [optional] 

## Example

```python
from suger_sdk_python.models.support_ticket import SupportTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicket from a JSON string
support_ticket_instance = SupportTicket.from_json(json)
# print the JSON string representation of the object
print(SupportTicket.to_json())

# convert the object into a dict
support_ticket_dict = support_ticket_instance.to_dict()
# create an instance of SupportTicket from a dict
support_ticket_from_dict = SupportTicket.from_dict(support_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


