# AzureMarketplacePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | ISO 4217 currency code | [optional] 
**markets** | **List[str]** | PriceAndAvailability audience definition | [optional] 
**price** | **float** | Prices   interface{} &#x60;json:\&quot;prices,omitempty\&quot;&#x60; | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price import AzureMarketplacePrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrice from a JSON string
azure_marketplace_price_instance = AzureMarketplacePrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePrice.to_json())

# convert the object into a dict
azure_marketplace_price_dict = azure_marketplace_price_instance.to_dict()
# create an instance of AzureMarketplacePrice from a dict
azure_marketplace_price_from_dict = AzureMarketplacePrice.from_dict(azure_marketplace_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


