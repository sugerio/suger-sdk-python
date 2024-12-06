# GcpMarketplaceProductPurchaseSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[GcpMarketplaceProductFeature]**](GcpMarketplaceProductFeature.md) |  | [optional] 
**metrics** | [**List[GcpMarketplaceProductMeteringMetric]**](GcpMarketplaceProductMeteringMetric.md) | GCP Marketplace Product Usage Metering Dimension/Metric | [optional] 
**purchase_option_specs** | [**List[GcpMarketplaceProductPurchaseOptionSpec]**](GcpMarketplaceProductPurchaseOptionSpec.md) | GCP Marketplace Product Pricing Plans | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_product_purchase_spec import GcpMarketplaceProductPurchaseSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductPurchaseSpec from a JSON string
gcp_marketplace_product_purchase_spec_instance = GcpMarketplaceProductPurchaseSpec.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceProductPurchaseSpec.to_json())

# convert the object into a dict
gcp_marketplace_product_purchase_spec_dict = gcp_marketplace_product_purchase_spec_instance.to_dict()
# create an instance of GcpMarketplaceProductPurchaseSpec from a dict
gcp_marketplace_product_purchase_spec_from_dict = GcpMarketplaceProductPurchaseSpec.from_dict(gcp_marketplace_product_purchase_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


