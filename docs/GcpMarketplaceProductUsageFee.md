# GcpMarketplaceProductUsageFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_quantity** | **int** | such as 1 | [optional] 
**metric_id** | **str** | such as \&quot;Starter_storage\&quot; | [optional] 
**price_tiers** | [**List[GcpPriceTier]**](GcpPriceTier.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_usage_fee import GcpMarketplaceProductUsageFee

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductUsageFee from a JSON string
gcp_marketplace_product_usage_fee_instance = GcpMarketplaceProductUsageFee.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductUsageFee.to_json()

# convert the object into a dict
gcp_marketplace_product_usage_fee_dict = gcp_marketplace_product_usage_fee_instance.to_dict()
# create an instance of GcpMarketplaceProductUsageFee from a dict
gcp_marketplace_product_usage_fee_form_dict = gcp_marketplace_product_usage_fee.from_dict(gcp_marketplace_product_usage_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


