# BillableMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_type** | [**BillableMetricAggregationType**](BillableMetricAggregationType.md) |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**BillableMetricInfo**](BillableMetricInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**status** | [**BillableMetricStatus**](BillableMetricStatus.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.billable_metric import BillableMetric

# TODO update the JSON string below
json = "{}"
# create an instance of BillableMetric from a JSON string
billable_metric_instance = BillableMetric.from_json(json)
# print the JSON string representation of the object
print(BillableMetric.to_json())

# convert the object into a dict
billable_metric_dict = billable_metric_instance.to_dict()
# create an instance of BillableMetric from a dict
billable_metric_from_dict = BillableMetric.from_dict(billable_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


