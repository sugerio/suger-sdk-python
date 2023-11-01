# AzureMarketplaceReseller


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**audiences** | [**List[AzureMarketplacePreviewAudience]**](AzureMarketplacePreviewAudience.md) |  | [optional] 
**id** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**reseller_channel_state** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_reseller import AzureMarketplaceReseller

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceReseller from a JSON string
azure_marketplace_reseller_instance = AzureMarketplaceReseller.from_json(json)
# print the JSON string representation of the object
print AzureMarketplaceReseller.to_json()

# convert the object into a dict
azure_marketplace_reseller_dict = azure_marketplace_reseller_instance.to_dict()
# create an instance of AzureMarketplaceReseller from a dict
azure_marketplace_reseller_form_dict = azure_marketplace_reseller.from_dict(azure_marketplace_reseller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


