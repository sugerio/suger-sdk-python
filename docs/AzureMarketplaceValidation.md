# AzureMarketplaceValidation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_validation import AzureMarketplaceValidation

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceValidation from a JSON string
azure_marketplace_validation_instance = AzureMarketplaceValidation.from_json(json)
# print the JSON string representation of the object
print AzureMarketplaceValidation.to_json()

# convert the object into a dict
azure_marketplace_validation_dict = azure_marketplace_validation_instance.to_dict()
# create an instance of AzureMarketplaceValidation from a dict
azure_marketplace_validation_form_dict = azure_marketplace_validation.from_dict(azure_marketplace_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


