# UsageMeteringDailyRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**entitlement_id** | **str** | The Entitlement ID of the usage metering daily record. | [optional] 
**group_bys_expression** | **str** | The group bys expression of the usage metering. When the same usage metering key may have multiple expressions of group bys to aggregate the usage. | [optional] 
**key** | **str** | The dimension key of the usage metering. | [optional] 
**partner** | [**Partner**](Partner.md) | The partner where this usage metering daily record is from. Such as AWS, AZURE or GCP. | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.usage_metering_daily_record import UsageMeteringDailyRecord

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeteringDailyRecord from a JSON string
usage_metering_daily_record_instance = UsageMeteringDailyRecord.from_json(json)
# print the JSON string representation of the object
print(UsageMeteringDailyRecord.to_json())

# convert the object into a dict
usage_metering_daily_record_dict = usage_metering_daily_record_instance.to_dict()
# create an instance of UsageMeteringDailyRecord from a dict
usage_metering_daily_record_from_dict = UsageMeteringDailyRecord.from_dict(usage_metering_daily_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


