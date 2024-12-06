# GcpMarketplaceProductSupportSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_product_support_spec import GcpMarketplaceProductSupportSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductSupportSpec from a JSON string
gcp_marketplace_product_support_spec_instance = GcpMarketplaceProductSupportSpec.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceProductSupportSpec.to_json())

# convert the object into a dict
gcp_marketplace_product_support_spec_dict = gcp_marketplace_product_support_spec_instance.to_dict()
# create an instance of GcpMarketplaceProductSupportSpec from a dict
gcp_marketplace_product_support_spec_from_dict = GcpMarketplaceProductSupportSpec.from_dict(gcp_marketplace_product_support_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


