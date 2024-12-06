# GcpMarketplaceProductDocumentationSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_product_documentation_spec import GcpMarketplaceProductDocumentationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductDocumentationSpec from a JSON string
gcp_marketplace_product_documentation_spec_instance = GcpMarketplaceProductDocumentationSpec.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceProductDocumentationSpec.to_json())

# convert the object into a dict
gcp_marketplace_product_documentation_spec_dict = gcp_marketplace_product_documentation_spec_instance.to_dict()
# create an instance of GcpMarketplaceProductDocumentationSpec from a dict
gcp_marketplace_product_documentation_spec_from_dict = GcpMarketplaceProductDocumentationSpec.from_dict(gcp_marketplace_product_documentation_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


