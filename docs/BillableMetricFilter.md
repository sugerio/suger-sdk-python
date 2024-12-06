# BillableMetricFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**operation** | [**BillableMetricFilterOperation**](BillableMetricFilterOperation.md) |  | [optional] 
**value** | **object** | The value of the filter. The type of the value depends on the valueType. | [optional] 
**value_type** | [**BillableMetricFilterValueType**](BillableMetricFilterValueType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.billable_metric_filter import BillableMetricFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BillableMetricFilter from a JSON string
billable_metric_filter_instance = BillableMetricFilter.from_json(json)
# print the JSON string representation of the object
print(BillableMetricFilter.to_json())

# convert the object into a dict
billable_metric_filter_dict = billable_metric_filter_instance.to_dict()
# create an instance of BillableMetricFilter from a dict
billable_metric_filter_from_dict = BillableMetricFilter.from_dict(billable_metric_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


