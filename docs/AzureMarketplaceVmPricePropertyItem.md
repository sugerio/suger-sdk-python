# AzureMarketplaceVmPricePropertyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** |  | [optional] 
**unit_price_per_payment_period_in_usd** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_vm_price_property_item import AzureMarketplaceVmPricePropertyItem

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceVmPricePropertyItem from a JSON string
azure_marketplace_vm_price_property_item_instance = AzureMarketplaceVmPricePropertyItem.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceVmPricePropertyItem.to_json())

# convert the object into a dict
azure_marketplace_vm_price_property_item_dict = azure_marketplace_vm_price_property_item_instance.to_dict()
# create an instance of AzureMarketplaceVmPricePropertyItem from a dict
azure_marketplace_vm_price_property_item_from_dict = AzureMarketplaceVmPricePropertyItem.from_dict(azure_marketplace_vm_price_property_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


