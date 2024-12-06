# GcpMarketplaceMeteringMetricValueSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | MetricName: The metric name defined in the service configuration. | [optional] 
**metric_values** | [**List[GcpMarketplaceMeteringMetricValue]**](GcpMarketplaceMeteringMetricValue.md) | MetricValues: The values in this metric. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_metering_metric_value_set import GcpMarketplaceMeteringMetricValueSet

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceMeteringMetricValueSet from a JSON string
gcp_marketplace_metering_metric_value_set_instance = GcpMarketplaceMeteringMetricValueSet.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceMeteringMetricValueSet.to_json())

# convert the object into a dict
gcp_marketplace_metering_metric_value_set_dict = gcp_marketplace_metering_metric_value_set_instance.to_dict()
# create an instance of GcpMarketplaceMeteringMetricValueSet from a dict
gcp_marketplace_metering_metric_value_set_from_dict = GcpMarketplaceMeteringMetricValueSet.from_dict(gcp_marketplace_metering_metric_value_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


