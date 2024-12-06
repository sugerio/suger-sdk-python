# UpdateBillableMetricParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**BillableMetricStatus**](BillableMetricStatus.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.update_billable_metric_params import UpdateBillableMetricParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBillableMetricParams from a JSON string
update_billable_metric_params_instance = UpdateBillableMetricParams.from_json(json)
# print the JSON string representation of the object
print(UpdateBillableMetricParams.to_json())

# convert the object into a dict
update_billable_metric_params_dict = update_billable_metric_params_instance.to_dict()
# create an instance of UpdateBillableMetricParams from a dict
update_billable_metric_params_from_dict = UpdateBillableMetricParams.from_dict(update_billable_metric_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


