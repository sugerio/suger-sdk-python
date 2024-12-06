# GcpMarketplaceProductInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavor_external_name** | **str** | The service level (price plan) with time duration suffix, such as \&quot;basic-plan-P1Y\&quot; | [optional] 
**product_external_name** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**service_level** | **str** | The price plan, such as \&quot;basic-plan\&quot; | [optional] 
**service_name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_product_info import GcpMarketplaceProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductInfo from a JSON string
gcp_marketplace_product_info_instance = GcpMarketplaceProductInfo.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceProductInfo.to_json())

# convert the object into a dict
gcp_marketplace_product_info_dict = gcp_marketplace_product_info_instance.to_dict()
# create an instance of GcpMarketplaceProductInfo from a dict
gcp_marketplace_product_info_from_dict = GcpMarketplaceProductInfo.from_dict(gcp_marketplace_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


