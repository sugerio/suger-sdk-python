# GcpMarketplaceProductFeatureValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_description** | **str** | such as \&quot;CPU per VM\&quot; | [optional] 
**feature_name** | **str** | such as \&quot;cpu\&quot; | [optional] 
**feature_title** | **str** | such as \&quot;CPU\&quot; | [optional] 
**feature_value** | **str** | such as \&quot;2 CPU per VM\&quot; | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_feature_value import GcpMarketplaceProductFeatureValue

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductFeatureValue from a JSON string
gcp_marketplace_product_feature_value_instance = GcpMarketplaceProductFeatureValue.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductFeatureValue.to_json()

# convert the object into a dict
gcp_marketplace_product_feature_value_dict = gcp_marketplace_product_feature_value_instance.to_dict()
# create an instance of GcpMarketplaceProductFeatureValue from a dict
gcp_marketplace_product_feature_value_form_dict = gcp_marketplace_product_feature_value.from_dict(gcp_marketplace_product_feature_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


