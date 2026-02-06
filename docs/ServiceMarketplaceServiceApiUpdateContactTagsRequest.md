# ServiceMarketplaceServiceApiUpdateContactTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 

## Example

```python
from suger_sdk_python.models.service_marketplace_service_api_update_contact_tags_request import ServiceMarketplaceServiceApiUpdateContactTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMarketplaceServiceApiUpdateContactTagsRequest from a JSON string
service_marketplace_service_api_update_contact_tags_request_instance = ServiceMarketplaceServiceApiUpdateContactTagsRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceMarketplaceServiceApiUpdateContactTagsRequest.to_json())

# convert the object into a dict
service_marketplace_service_api_update_contact_tags_request_dict = service_marketplace_service_api_update_contact_tags_request_instance.to_dict()
# create an instance of ServiceMarketplaceServiceApiUpdateContactTagsRequest from a dict
service_marketplace_service_api_update_contact_tags_request_from_dict = ServiceMarketplaceServiceApiUpdateContactTagsRequest.from_dict(service_marketplace_service_api_update_contact_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


