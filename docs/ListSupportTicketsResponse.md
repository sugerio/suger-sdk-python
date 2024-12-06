# ListSupportTicketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SupportTicket]**](SupportTicket.md) |  | [optional] 
**total_count** | **int** | Only available when the request is made with offset&#x3D;0. | [optional] 

## Example

```python
from suger_sdk_python.models.list_support_tickets_response import ListSupportTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportTicketsResponse from a JSON string
list_support_tickets_response_instance = ListSupportTicketsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSupportTicketsResponse.to_json())

# convert the object into a dict
list_support_tickets_response_dict = list_support_tickets_response_instance.to_dict()
# create an instance of ListSupportTicketsResponse from a dict
list_support_tickets_response_from_dict = ListSupportTicketsResponse.from_dict(list_support_tickets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


