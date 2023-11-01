# AzureProductListingAsset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**file_sas_uri** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**publisher_defined_sas_uri** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_product_listing_asset import AzureProductListingAsset

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductListingAsset from a JSON string
azure_product_listing_asset_instance = AzureProductListingAsset.from_json(json)
# print the JSON string representation of the object
print AzureProductListingAsset.to_json()

# convert the object into a dict
azure_product_listing_asset_dict = azure_product_listing_asset_instance.to_dict()
# create an instance of AzureProductListingAsset from a dict
azure_product_listing_asset_form_dict = azure_product_listing_asset.from_dict(azure_product_listing_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


