# GcpMarketplaceProductPurchaseOptionSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_values** | [**List[GcpMarketplaceProductFeatureValue]**](GcpMarketplaceProductFeatureValue.md) |  | [optional] 
**name** | **str** | The plan ID, such as \&quot;starter\&quot;, without the duration suffix, such as \&quot;P1Y\&quot;. | [optional] 
**price_info** | [**GcpMarketplaceProductPriceInfo**](GcpMarketplaceProductPriceInfo.md) |  | [optional] 
**purchase_mode** | **str** |  | [optional] 
**title** | **str** | such as \&quot;Starter\&quot; | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_purchase_option_spec import GcpMarketplaceProductPurchaseOptionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductPurchaseOptionSpec from a JSON string
gcp_marketplace_product_purchase_option_spec_instance = GcpMarketplaceProductPurchaseOptionSpec.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductPurchaseOptionSpec.to_json()

# convert the object into a dict
gcp_marketplace_product_purchase_option_spec_dict = gcp_marketplace_product_purchase_option_spec_instance.to_dict()
# create an instance of GcpMarketplaceProductPurchaseOptionSpec from a dict
gcp_marketplace_product_purchase_option_spec_form_dict = gcp_marketplace_product_purchase_option_spec.from_dict(gcp_marketplace_product_purchase_option_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


