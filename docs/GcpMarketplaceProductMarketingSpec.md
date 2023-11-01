# GcpMarketplaceProductMarketingSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_names** | **List[str]** |  | [optional] 
**documentation_specs** | [**List[GcpMarketplaceProductDocumentationSpec]**](GcpMarketplaceProductDocumentationSpec.md) |  | [optional] 
**eula_url** | **str** |  | [optional] 
**external_license_specs** | [**List[GcpMarketplaceProductLicenseSpec]**](GcpMarketplaceProductLicenseSpec.md) |  | [optional] 
**external_marketing_url** | **str** |  | [optional] 
**icon** | **str** | in format of \&quot;base64://...\&quot; | [optional] 
**search_categories** | **List[str]** |  | [optional] 
**search_description** | **str** |  | [optional] 
**search_keywords** | **List[str]** |  | [optional] 
**signup_uri** | **str** |  | [optional] 
**support_spec** | [**GcpMarketplaceProductSupportSpec**](GcpMarketplaceProductSupportSpec.md) |  | [optional] 
**tag_line** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_marketing_spec import GcpMarketplaceProductMarketingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductMarketingSpec from a JSON string
gcp_marketplace_product_marketing_spec_instance = GcpMarketplaceProductMarketingSpec.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductMarketingSpec.to_json()

# convert the object into a dict
gcp_marketplace_product_marketing_spec_dict = gcp_marketplace_product_marketing_spec_instance.to_dict()
# create an instance of GcpMarketplaceProductMarketingSpec from a dict
gcp_marketplace_product_marketing_spec_form_dict = gcp_marketplace_product_marketing_spec.from_dict(gcp_marketplace_product_marketing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


