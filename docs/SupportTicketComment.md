# SupportTicketComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**List[SupportTicketCommentDetail]**](SupportTicketCommentDetail.md) |  | [optional] 
**comment_text** | **str** | When creating a new comment, only CommentText is required. | [optional] 
**creator** | [**SupportTicketUser**](SupportTicketUser.md) | who created the comment | [optional] 
**var_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.support_ticket_comment import SupportTicketComment

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketComment from a JSON string
support_ticket_comment_instance = SupportTicketComment.from_json(json)
# print the JSON string representation of the object
print(SupportTicketComment.to_json())

# convert the object into a dict
support_ticket_comment_dict = support_ticket_comment_instance.to_dict()
# create an instance of SupportTicketComment from a dict
support_ticket_comment_from_dict = SupportTicketComment.from_dict(support_ticket_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


