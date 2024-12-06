# AzureMarketplaceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**alias** | **str** | The Product Display Name | [optional] 
**id** | **str** | in format of \&quot;product/product-durable-id\&quot; | [optional] 
**identity** | [**AzureMarketplaceIdentity**](AzureMarketplaceIdentity.md) |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**product_group** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**type** | [**AzureMarketplaceProductType**](AzureMarketplaceProductType.md) |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_product import AzureMarketplaceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceProduct from a JSON string
azure_marketplace_product_instance = AzureMarketplaceProduct.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceProduct.to_json())

# convert the object into a dict
azure_marketplace_product_dict = azure_marketplace_product_instance.to_dict()
# create an instance of AzureMarketplaceProduct from a dict
azure_marketplace_product_from_dict = AzureMarketplaceProduct.from_dict(azure_marketplace_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


