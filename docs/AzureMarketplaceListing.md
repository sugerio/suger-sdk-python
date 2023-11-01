# AzureMarketplaceListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**cloud_solution_provider_contact** | [**AzureMarketplaceContact**](AzureMarketplaceContact.md) |  | [optional] 
**cloud_solution_provider_marketing_materials** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**engineering_contact** | [**AzureMarketplaceContact**](AzureMarketplaceContact.md) |  | [optional] 
**general_links** | [**List[AzureMarketplaceGeneralLink]**](AzureMarketplaceGeneralLink.md) |  | [optional] 
**getting_started_instructions** | **str** |  | [optional] 
**gloabal_support_website** | **str** |  | [optional] 
**government_support_website** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**privacy_policy_link** | **str** |  | [optional] 
**product** | **str** | Product resource name, in format of \&quot;product/product-durable-id\&quot; | [optional] 
**resource_name** | **str** |  | [optional] 
**search_keywords** | **List[str]** |  | [optional] 
**search_result_summary** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**support_contact** | [**AzureMarketplaceContact**](AzureMarketplaceContact.md) |  | [optional] 
**title** | **str** | Max string length is 200. | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_listing import AzureMarketplaceListing

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceListing from a JSON string
azure_marketplace_listing_instance = AzureMarketplaceListing.from_json(json)
# print the JSON string representation of the object
print AzureMarketplaceListing.to_json()

# convert the object into a dict
azure_marketplace_listing_dict = azure_marketplace_listing_instance.to_dict()
# create an instance of AzureMarketplaceListing from a dict
azure_marketplace_listing_form_dict = azure_marketplace_listing.from_dict(azure_marketplace_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


