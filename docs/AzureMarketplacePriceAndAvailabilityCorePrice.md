# AzureMarketplacePriceAndAvailabilityCorePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**price_input_option** | **str** |  | [optional] 
**price_per_core** | **float** |  | [optional] 
**price_per_core_size** | **object** |  | [optional] 
**prices** | [**List[AzureMarketplacePrice]**](AzureMarketplacePrice.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_core_price import AzureMarketplacePriceAndAvailabilityCorePrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCorePrice from a JSON string
azure_marketplace_price_and_availability_core_price_instance = AzureMarketplacePriceAndAvailabilityCorePrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityCorePrice.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_core_price_dict = azure_marketplace_price_and_availability_core_price_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCorePrice from a dict
azure_marketplace_price_and_availability_core_price_from_dict = AzureMarketplacePriceAndAvailabilityCorePrice.from_dict(azure_marketplace_price_and_availability_core_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


