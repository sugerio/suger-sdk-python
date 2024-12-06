# SupportTicketCommentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | [**SupportTicketAttachment**](SupportTicketAttachment.md) |  | [optional] 
**frame** | [**SupportTicketFrame**](SupportTicketFrame.md) |  | [optional] 
**image** | [**SupportTicketImage**](SupportTicketImage.md) |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.support_ticket_comment_detail import SupportTicketCommentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketCommentDetail from a JSON string
support_ticket_comment_detail_instance = SupportTicketCommentDetail.from_json(json)
# print the JSON string representation of the object
print(SupportTicketCommentDetail.to_json())

# convert the object into a dict
support_ticket_comment_detail_dict = support_ticket_comment_detail_instance.to_dict()
# create an instance of SupportTicketCommentDetail from a dict
support_ticket_comment_detail_from_dict = SupportTicketCommentDetail.from_dict(support_ticket_comment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


