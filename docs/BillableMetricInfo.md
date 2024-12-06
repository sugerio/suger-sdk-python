# BillableMetricInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_groups** | [**List[BillableMetricFilterGroup]**](BillableMetricFilterGroup.md) | FilterGroups is a list of filter groups. The filterGroups are connected by AND. | [optional] 
**group_bys** | **List[str]** | GroupBys is a list of fields to group by. | [optional] 
**property_unique_on** | **str** | The target property for unique count aggregate. | [optional] 

## Example

```python
from suger_sdk_python.models.billable_metric_info import BillableMetricInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillableMetricInfo from a JSON string
billable_metric_info_instance = BillableMetricInfo.from_json(json)
# print the JSON string representation of the object
print(BillableMetricInfo.to_json())

# convert the object into a dict
billable_metric_info_dict = billable_metric_info_instance.to_dict()
# create an instance of BillableMetricInfo from a dict
billable_metric_info_from_dict = BillableMetricInfo.from_dict(billable_metric_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


