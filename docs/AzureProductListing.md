# AzureProductListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_information** | **str** |  | [optional] 
**assets** | [**List[AzureProductListingAsset]**](AzureProductListingAsset.md) | Not original fields. They are populated by other API calls | [optional] 
**compatible_products** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**getting_started_instructions** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**language_code** | **str** |  | [optional] 
**listing_contacts** | [**List[AzureListingContact]**](AzureListingContact.md) |  | [optional] 
**listing_uris** | [**List[AzureListingUri]**](AzureListingUri.md) |  | [optional] 
**product_display_name** | **str** |  | [optional] 
**publisher_name** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_product_listing import AzureProductListing

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductListing from a JSON string
azure_product_listing_instance = AzureProductListing.from_json(json)
# print the JSON string representation of the object
print AzureProductListing.to_json()

# convert the object into a dict
azure_product_listing_dict = azure_product_listing_instance.to_dict()
# create an instance of AzureProductListing from a dict
azure_product_listing_form_dict = azure_product_listing.from_dict(azure_product_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


