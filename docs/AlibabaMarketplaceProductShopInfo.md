# AlibabaMarketplaceProductShopInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**telephones** | [**AlibabaMarketplaceProductShopInfoTelephones**](AlibabaMarketplaceProductShopInfoTelephones.md) |  | [optional] 
**wang_wangs** | [**AlibabaMarketplaceProductShopInfoWangWangs**](AlibabaMarketplaceProductShopInfoWangWangs.md) |  | [optional] 

## Example

```python
from openapi_client.models.alibaba_marketplace_product_shop_info import AlibabaMarketplaceProductShopInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaMarketplaceProductShopInfo from a JSON string
alibaba_marketplace_product_shop_info_instance = AlibabaMarketplaceProductShopInfo.from_json(json)
# print the JSON string representation of the object
print AlibabaMarketplaceProductShopInfo.to_json()

# convert the object into a dict
alibaba_marketplace_product_shop_info_dict = alibaba_marketplace_product_shop_info_instance.to_dict()
# create an instance of AlibabaMarketplaceProductShopInfo from a dict
alibaba_marketplace_product_shop_info_form_dict = alibaba_marketplace_product_shop_info.from_dict(alibaba_marketplace_product_shop_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


