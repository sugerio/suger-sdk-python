# GcpMarketplaceProductServiceConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing** | [**GcpMarketplaceProductServiceConfigBilling**](GcpMarketplaceProductServiceConfigBilling.md) |  | [optional] 
**metrics** | [**List[GcpMarketplaceProductMeteringMetric]**](GcpMarketplaceProductMeteringMetric.md) |  | [optional] 
**name** | **str** | in format of \&quot;product-name.endpoints.gcp-project-id.cloud.goog\&quot; | [optional] 
**producer_project_id** | **str** | The GCP project ID of the producer. | [optional] 
**title** | **str** | The title of the product listing. | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_service_config import GcpMarketplaceProductServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductServiceConfig from a JSON string
gcp_marketplace_product_service_config_instance = GcpMarketplaceProductServiceConfig.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductServiceConfig.to_json()

# convert the object into a dict
gcp_marketplace_product_service_config_dict = gcp_marketplace_product_service_config_instance.to_dict()
# create an instance of GcpMarketplaceProductServiceConfig from a dict
gcp_marketplace_product_service_config_form_dict = gcp_marketplace_product_service_config.from_dict(gcp_marketplace_product_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


