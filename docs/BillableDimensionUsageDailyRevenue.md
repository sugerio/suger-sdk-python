# BillableDimensionUsageDailyRevenue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_metric_key** | [**MeteringUsageRecordGroupByKey**](MeteringUsageRecordGroupByKey.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**unique_property_items** | **Dict[str, object]** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billable_dimension_usage_daily_revenue import BillableDimensionUsageDailyRevenue

# TODO update the JSON string below
json = "{}"
# create an instance of BillableDimensionUsageDailyRevenue from a JSON string
billable_dimension_usage_daily_revenue_instance = BillableDimensionUsageDailyRevenue.from_json(json)
# print the JSON string representation of the object
print(BillableDimensionUsageDailyRevenue.to_json())

# convert the object into a dict
billable_dimension_usage_daily_revenue_dict = billable_dimension_usage_daily_revenue_instance.to_dict()
# create an instance of BillableDimensionUsageDailyRevenue from a dict
billable_dimension_usage_daily_revenue_from_dict = BillableDimensionUsageDailyRevenue.from_dict(billable_dimension_usage_daily_revenue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


