# AzureListingUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_text** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_listing_uri import AzureListingUri

# TODO update the JSON string below
json = "{}"
# create an instance of AzureListingUri from a JSON string
azure_listing_uri_instance = AzureListingUri.from_json(json)
# print the JSON string representation of the object
print AzureListingUri.to_json()

# convert the object into a dict
azure_listing_uri_dict = azure_listing_uri_instance.to_dict()
# create an instance of AzureListingUri from a dict
azure_listing_uri_form_dict = azure_listing_uri.from_dict(azure_listing_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


