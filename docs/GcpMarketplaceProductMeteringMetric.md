# GcpMarketplaceProductMeteringMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description: A detailed description of the metric, which can be used in documentation. | [optional] 
**display_name** | **str** |  | [optional] 
**display_unit** | **str** | such as \&quot;min\&quot; | [optional] 
**display_unit_description** | **str** | such as \&quot;minute\&quot; | [optional] 
**id** | **str** | The usage metering metric/dimension key It is in format of \&quot;{plan_id}_{usage_dimension_key}\&quot;. For example, \&quot;basic_plan_storage\&quot;. | [optional] 
**metric_kind** | **str** | such as \&quot;DELTA\&quot; | [optional] 
**name** | **str** | Name: The resource name of the metric descriptor, in format of \&quot;{productServiceName}/{plan_id}_{usage_dimension_key}\&quot; | [optional] 
**price_tiers** | [**List[GcpPriceTier]**](GcpPriceTier.md) | Price info of this usage metering metric. Only applicable for the default offer (plan) and private offer. | [optional] 
**reporting_unit** | **str** | such as \&quot;min\&quot; | [optional] 
**sku_id** | **str** | The SKU ID of this usage metering metric. Applicable only in Private Offer. | [optional] 
**unit** | **str** | such as \&quot;min\&quot; | [optional] 
**value_type** | [**ValueType**](ValueType.md) | such as \&quot;INT64\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_product_metering_metric import GcpMarketplaceProductMeteringMetric

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductMeteringMetric from a JSON string
gcp_marketplace_product_metering_metric_instance = GcpMarketplaceProductMeteringMetric.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceProductMeteringMetric.to_json())

# convert the object into a dict
gcp_marketplace_product_metering_metric_dict = gcp_marketplace_product_metering_metric_instance.to_dict()
# create an instance of GcpMarketplaceProductMeteringMetric from a dict
gcp_marketplace_product_metering_metric_from_dict = GcpMarketplaceProductMeteringMetric.from_dict(gcp_marketplace_product_metering_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


