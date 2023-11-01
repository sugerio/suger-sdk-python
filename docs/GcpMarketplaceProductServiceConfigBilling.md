# GcpMarketplaceProductServiceConfigBilling


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **List[str]** | The list of metrics that are available for billing for the product. In format of \&quot;product-name.endpoints.gcp-project-id.cloud.goog/plan_name_metric_name\&quot; | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_service_config_billing import GcpMarketplaceProductServiceConfigBilling

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductServiceConfigBilling from a JSON string
gcp_marketplace_product_service_config_billing_instance = GcpMarketplaceProductServiceConfigBilling.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductServiceConfigBilling.to_json()

# convert the object into a dict
gcp_marketplace_product_service_config_billing_dict = gcp_marketplace_product_service_config_billing_instance.to_dict()
# create an instance of GcpMarketplaceProductServiceConfigBilling from a dict
gcp_marketplace_product_service_config_billing_form_dict = gcp_marketplace_product_service_config_billing.from_dict(gcp_marketplace_product_service_config_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


