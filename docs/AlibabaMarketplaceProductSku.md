# AlibabaMarketplaceProductSku


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_type** | **str** | POSTPAY or PREPAY | [optional] 
**code** | **str** |  | [optional] 
**constraints** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**modules** | [**AlibabaMarketplaceProductSkuModules**](AlibabaMarketplaceProductSkuModules.md) |  | [optional] 
**name** | **str** |  | [optional] 
**order_periods** | [**AlibabaMarketplaceProductSkuOrderPeriods**](AlibabaMarketplaceProductSkuOrderPeriods.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.alibaba_marketplace_product_sku import AlibabaMarketplaceProductSku

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaMarketplaceProductSku from a JSON string
alibaba_marketplace_product_sku_instance = AlibabaMarketplaceProductSku.from_json(json)
# print the JSON string representation of the object
print(AlibabaMarketplaceProductSku.to_json())

# convert the object into a dict
alibaba_marketplace_product_sku_dict = alibaba_marketplace_product_sku_instance.to_dict()
# create an instance of AlibabaMarketplaceProductSku from a dict
alibaba_marketplace_product_sku_from_dict = AlibabaMarketplaceProductSku.from_dict(alibaba_marketplace_product_sku_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


