# AzureMarketplacePreviewAudience


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_preview_audience import AzureMarketplacePreviewAudience

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePreviewAudience from a JSON string
azure_marketplace_preview_audience_instance = AzureMarketplacePreviewAudience.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePreviewAudience.to_json()

# convert the object into a dict
azure_marketplace_preview_audience_dict = azure_marketplace_preview_audience_instance.to_dict()
# create an instance of AzureMarketplacePreviewAudience from a dict
azure_marketplace_preview_audience_form_dict = azure_marketplace_preview_audience.from_dict(azure_marketplace_preview_audience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


