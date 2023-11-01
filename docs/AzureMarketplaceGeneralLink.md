# AzureMarketplaceGeneralLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_text** | **str** |  | [optional] 
**link** | **str** | in patern of \&quot;^(http|https)://\&quot; | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_general_link import AzureMarketplaceGeneralLink

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceGeneralLink from a JSON string
azure_marketplace_general_link_instance = AzureMarketplaceGeneralLink.from_json(json)
# print the JSON string representation of the object
print AzureMarketplaceGeneralLink.to_json()

# convert the object into a dict
azure_marketplace_general_link_dict = azure_marketplace_general_link_instance.to_dict()
# create an instance of AzureMarketplaceGeneralLink from a dict
azure_marketplace_general_link_form_dict = azure_marketplace_general_link.from_dict(azure_marketplace_general_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


