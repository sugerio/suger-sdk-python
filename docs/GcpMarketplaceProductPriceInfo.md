# GcpMarketplaceProductPriceInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**price_model** | [**GcpMarketplacePriceModel**](GcpMarketplacePriceModel.md) |  | [optional] 
**subscription_plans** | [**List[GcpMarketplaceProductSubscriptionPlan]**](GcpMarketplaceProductSubscriptionPlan.md) | Subscription Plan (Flat Commitment) | [optional] 
**usage_fees** | [**List[GcpMarketplaceProductUsageFee]**](GcpMarketplaceProductUsageFee.md) | Usage Metering Dimension/Metric if available | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_price_info import GcpMarketplaceProductPriceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductPriceInfo from a JSON string
gcp_marketplace_product_price_info_instance = GcpMarketplaceProductPriceInfo.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductPriceInfo.to_json()

# convert the object into a dict
gcp_marketplace_product_price_info_dict = gcp_marketplace_product_price_info_instance.to_dict()
# create an instance of GcpMarketplaceProductPriceInfo from a dict
gcp_marketplace_product_price_info_form_dict = gcp_marketplace_product_price_info.from_dict(gcp_marketplace_product_price_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


