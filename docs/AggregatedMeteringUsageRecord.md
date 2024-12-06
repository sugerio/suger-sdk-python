# AggregatedMeteringUsageRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount calculated by billable dimension&#39;s price model, this is only used for report billable usage records to marketplace. | [optional] 
**billable_metric_aggregation_type** | [**BillableMetricAggregationType**](BillableMetricAggregationType.md) |  | [optional] 
**billable_metric_info** | [**BillableMetricInfo**](BillableMetricInfo.md) |  | [optional] 
**group_bys_expression** | **str** | GroupBysExpression is the string expression of array of group bys. | [optional] 
**key** | **str** | Key is the unique identifier of a billable metric. | [optional] 
**name** | **str** | Name is the name of a billable metric. Optional, it is only for display purpose. | [optional] 
**quantity** | **float** | Value is the value of a billable metric. | [optional] 
**unique_count_aggregation_result** | [**UniqueCountAggregationResult**](UniqueCountAggregationResult.md) | Unique count metric aggregate result. | [optional] 

## Example

```python
from suger_sdk_python.models.aggregated_metering_usage_record import AggregatedMeteringUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedMeteringUsageRecord from a JSON string
aggregated_metering_usage_record_instance = AggregatedMeteringUsageRecord.from_json(json)
# print the JSON string representation of the object
print(AggregatedMeteringUsageRecord.to_json())

# convert the object into a dict
aggregated_metering_usage_record_dict = aggregated_metering_usage_record_instance.to_dict()
# create an instance of AggregatedMeteringUsageRecord from a dict
aggregated_metering_usage_record_from_dict = AggregatedMeteringUsageRecord.from_dict(aggregated_metering_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


