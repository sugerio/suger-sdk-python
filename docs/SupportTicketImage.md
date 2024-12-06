# SupportTicketImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**thumbnail_large** | **str** |  | [optional] 
**thumbnail_medium** | **str** |  | [optional] 
**thumbnail_small** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.support_ticket_image import SupportTicketImage

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketImage from a JSON string
support_ticket_image_instance = SupportTicketImage.from_json(json)
# print the JSON string representation of the object
print(SupportTicketImage.to_json())

# convert the object into a dict
support_ticket_image_dict = support_ticket_image_instance.to_dict()
# create an instance of SupportTicketImage from a dict
support_ticket_image_from_dict = SupportTicketImage.from_dict(support_ticket_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


