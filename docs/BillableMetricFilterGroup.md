# BillableMetricFilterGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[BillableMetricFilter]**](BillableMetricFilter.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.billable_metric_filter_group import BillableMetricFilterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of BillableMetricFilterGroup from a JSON string
billable_metric_filter_group_instance = BillableMetricFilterGroup.from_json(json)
# print the JSON string representation of the object
print(BillableMetricFilterGroup.to_json())

# convert the object into a dict
billable_metric_filter_group_dict = billable_metric_filter_group_instance.to_dict()
# create an instance of BillableMetricFilterGroup from a dict
billable_metric_filter_group_from_dict = BillableMetricFilterGroup.from_dict(billable_metric_filter_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


