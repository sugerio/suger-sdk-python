# GcpMarketplaceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **datetime** |  | [optional] 
**derived_discovery_state** | [**GcpMarketplaceProductDerivedDiscoveryState**](GcpMarketplaceProductDerivedDiscoveryState.md) |  | [optional] 
**id** | **str** | Nullable, GCP Marketplace Product UUID | [optional] 
**last_publish_time** | **datetime** |  | [optional] 
**listing_spec** | [**GcpMarketplaceProductListingSpec**](GcpMarketplaceProductListingSpec.md) |  | [optional] 
**marketplace** | **str** |  | [optional] 
**name** | **str** | In format of \&quot;projects/{project-number}/listings/{product-name}.endpoints.{provider-id}.cloud.goog\&quot; | [optional] 
**revision_create_time** | **datetime** |  | [optional] 
**revision_id** | **str** |  | [optional] 
**service** | **str** | In format of \&quot;services/{product-name}.endpoints.{provider-id}.cloud.goog\&quot; | [optional] 
**service_config** | [**GcpMarketplaceProductServiceConfig**](GcpMarketplaceProductServiceConfig.md) |  | [optional] 
**validation_summary** | **object** | TODO: add type | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_product import GcpMarketplaceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProduct from a JSON string
gcp_marketplace_product_instance = GcpMarketplaceProduct.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceProduct.to_json())

# convert the object into a dict
gcp_marketplace_product_dict = gcp_marketplace_product_instance.to_dict()
# create an instance of GcpMarketplaceProduct from a dict
gcp_marketplace_product_from_dict = GcpMarketplaceProduct.from_dict(gcp_marketplace_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


