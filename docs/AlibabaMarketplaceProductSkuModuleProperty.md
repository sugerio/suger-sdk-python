# AlibabaMarketplaceProductSkuModuleProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_unit** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**property_values** | [**AlibabaMarketplaceProductSkuModulePropertyValues**](AlibabaMarketplaceProductSkuModulePropertyValues.md) |  | [optional] 
**show_type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.alibaba_marketplace_product_sku_module_property import AlibabaMarketplaceProductSkuModuleProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaMarketplaceProductSkuModuleProperty from a JSON string
alibaba_marketplace_product_sku_module_property_instance = AlibabaMarketplaceProductSkuModuleProperty.from_json(json)
# print the JSON string representation of the object
print(AlibabaMarketplaceProductSkuModuleProperty.to_json())

# convert the object into a dict
alibaba_marketplace_product_sku_module_property_dict = alibaba_marketplace_product_sku_module_property_instance.to_dict()
# create an instance of AlibabaMarketplaceProductSkuModuleProperty from a dict
alibaba_marketplace_product_sku_module_property_from_dict = AlibabaMarketplaceProductSkuModuleProperty.from_dict(alibaba_marketplace_product_sku_module_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


