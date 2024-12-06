# AlibabaMarketplaceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_fail_msg** | **str** |  | [optional] 
**audit_status** | **str** |  | [optional] 
**audit_time** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**front_category_id** | **int** |  | [optional] 
**gmt_created** | **int** |  | [optional] 
**gmt_modified** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**pic_url** | **str** |  | [optional] 
**product_extras** | [**AlibabaMarketplaceProductExtras**](AlibabaMarketplaceProductExtras.md) |  | [optional] 
**product_skus** | [**AlibabaMarketplaceProductSkus**](AlibabaMarketplaceProductSkus.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**shop_info** | [**AlibabaMarketplaceProductShopInfo**](AlibabaMarketplaceProductShopInfo.md) |  | [optional] 
**short_description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**supplier_pk** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**use_count** | **int** |  | [optional] 

## Example

```python
from suger_sdk_python.models.alibaba_marketplace_product import AlibabaMarketplaceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaMarketplaceProduct from a JSON string
alibaba_marketplace_product_instance = AlibabaMarketplaceProduct.from_json(json)
# print the JSON string representation of the object
print(AlibabaMarketplaceProduct.to_json())

# convert the object into a dict
alibaba_marketplace_product_dict = alibaba_marketplace_product_instance.to_dict()
# create an instance of AlibabaMarketplaceProduct from a dict
alibaba_marketplace_product_from_dict = AlibabaMarketplaceProduct.from_dict(alibaba_marketplace_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


