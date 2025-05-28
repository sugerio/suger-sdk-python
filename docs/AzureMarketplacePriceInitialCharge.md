# AzureMarketplacePriceInitialCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**price_per_payment_in_usd** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_initial_charge import AzureMarketplacePriceInitialCharge

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceInitialCharge from a JSON string
azure_marketplace_price_initial_charge_instance = AzureMarketplacePriceInitialCharge.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceInitialCharge.to_json())

# convert the object into a dict
azure_marketplace_price_initial_charge_dict = azure_marketplace_price_initial_charge_instance.to_dict()
# create an instance of AzureMarketplacePriceInitialCharge from a dict
azure_marketplace_price_initial_charge_from_dict = AzureMarketplacePriceInitialCharge.from_dict(azure_marketplace_price_initial_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


