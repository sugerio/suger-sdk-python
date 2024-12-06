# AzureMarketplaceListingAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_order** | **int** | minimum: 0 | [optional] 
**file_name** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**language_id** | **str** | Max string length is 10. | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) | Default value is \&quot;generallyAvailable\&quot;. | [optional] 
**listing** | **str** |  | [optional] 
**product** | **str** | Product resource name, in format of \&quot;product/product-durable-id\&quot; | [optional] 
**resource_name** | **str** |  | [optional] 
**type** | [**AzureMarketplaceListingAssetType**](AzureMarketplaceListingAssetType.md) |  | [optional] 
**url** | **str** | pattern: \&quot;^https?://\&quot; | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_listing_asset import AzureMarketplaceListingAsset

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceListingAsset from a JSON string
azure_marketplace_listing_asset_instance = AzureMarketplaceListingAsset.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceListingAsset.to_json())

# convert the object into a dict
azure_marketplace_listing_asset_dict = azure_marketplace_listing_asset_instance.to_dict()
# create an instance of AzureMarketplaceListingAsset from a dict
azure_marketplace_listing_asset_from_dict = AzureMarketplaceListingAsset.from_dict(azure_marketplace_listing_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


