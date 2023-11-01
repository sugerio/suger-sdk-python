# AzureMarketplacePlanListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**name** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_plan_listing import AzureMarketplacePlanListing

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePlanListing from a JSON string
azure_marketplace_plan_listing_instance = AzureMarketplacePlanListing.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePlanListing.to_json()

# convert the object into a dict
azure_marketplace_plan_listing_dict = azure_marketplace_plan_listing_instance.to_dict()
# create an instance of AzureMarketplacePlanListing from a dict
azure_marketplace_plan_listing_form_dict = azure_marketplace_plan_listing.from_dict(azure_marketplace_plan_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


