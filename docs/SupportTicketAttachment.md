# SupportTicketAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**thumbnail_large** | **str** |  | [optional] 
**thumbnail_medium** | **str** |  | [optional] 
**thumbnail_small** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.support_ticket_attachment import SupportTicketAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketAttachment from a JSON string
support_ticket_attachment_instance = SupportTicketAttachment.from_json(json)
# print the JSON string representation of the object
print(SupportTicketAttachment.to_json())

# convert the object into a dict
support_ticket_attachment_dict = support_ticket_attachment_instance.to_dict()
# create an instance of SupportTicketAttachment from a dict
support_ticket_attachment_from_dict = SupportTicketAttachment.from_dict(support_ticket_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


