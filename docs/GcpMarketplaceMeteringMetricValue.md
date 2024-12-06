# GcpMarketplaceMeteringMetricValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool_value** | **bool** | BoolValue: A boolean value. | [optional] 
**double_value** | **float** | DoubleValue: A double precision floating point value. | [optional] 
**end_time** | **str** | EndTime: The end of the time period over which this metric value&#39;s measurement applies. If not specified, google.api.servicecontrol.v1.Operation.end_time will be used. | [optional] 
**int64_value** | **str** | Int64Value: A signed 64-bit integer value. | [optional] 
**labels** | **Dict[str, str]** | Labels: The labels describing the metric value. See comments on google.api.servicecontrol.v1.Operation.labels for the overriding relationship. Note that this map must not contain monitored resource labels. | [optional] 
**money_value** | [**GcpMarketplaceMeteringMoney**](GcpMarketplaceMeteringMoney.md) | MoneyValue: A money value. | [optional] 
**start_time** | **str** | StartTime: The start of the time period over which this metric value&#39;s measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, google.api.servicecontrol.v1.Operation.start_time will be used. | [optional] 
**string_value** | **str** | StringValue: A text string value. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_metering_metric_value import GcpMarketplaceMeteringMetricValue

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceMeteringMetricValue from a JSON string
gcp_marketplace_metering_metric_value_instance = GcpMarketplaceMeteringMetricValue.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceMeteringMetricValue.to_json())

# convert the object into a dict
gcp_marketplace_metering_metric_value_dict = gcp_marketplace_metering_metric_value_instance.to_dict()
# create an instance of GcpMarketplaceMeteringMetricValue from a dict
gcp_marketplace_metering_metric_value_from_dict = GcpMarketplaceMeteringMetricValue.from_dict(gcp_marketplace_metering_metric_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


