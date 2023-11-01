# UsageMeteringDailyRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**key** | **str** | The dimension key of the usage metering. | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.usage_metering_daily_record import UsageMeteringDailyRecord

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeteringDailyRecord from a JSON string
usage_metering_daily_record_instance = UsageMeteringDailyRecord.from_json(json)
# print the JSON string representation of the object
print UsageMeteringDailyRecord.to_json()

# convert the object into a dict
usage_metering_daily_record_dict = usage_metering_daily_record_instance.to_dict()
# create an instance of UsageMeteringDailyRecord from a dict
usage_metering_daily_record_form_dict = usage_metering_daily_record.from_dict(usage_metering_daily_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


