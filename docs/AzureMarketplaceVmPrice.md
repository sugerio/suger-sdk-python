# AzureMarketplaceVmPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern_properties** | [**Dict[str, AzureMarketplaceVmPricePropertyItem]**](AzureMarketplaceVmPricePropertyItem.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_vm_price import AzureMarketplaceVmPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceVmPrice from a JSON string
azure_marketplace_vm_price_instance = AzureMarketplaceVmPrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceVmPrice.to_json())

# convert the object into a dict
azure_marketplace_vm_price_dict = azure_marketplace_vm_price_instance.to_dict()
# create an instance of AzureMarketplaceVmPrice from a dict
azure_marketplace_vm_price_from_dict = AzureMarketplaceVmPrice.from_dict(azure_marketplace_vm_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


