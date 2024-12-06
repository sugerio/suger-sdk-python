# ListUsageMeteringDailyRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** |  | [optional] 
**usage_metering_daily_records** | [**List[UsageMeteringDailyRecord]**](UsageMeteringDailyRecord.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.list_usage_metering_daily_records_response import ListUsageMeteringDailyRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsageMeteringDailyRecordsResponse from a JSON string
list_usage_metering_daily_records_response_instance = ListUsageMeteringDailyRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(ListUsageMeteringDailyRecordsResponse.to_json())

# convert the object into a dict
list_usage_metering_daily_records_response_dict = list_usage_metering_daily_records_response_instance.to_dict()
# create an instance of ListUsageMeteringDailyRecordsResponse from a dict
list_usage_metering_daily_records_response_from_dict = ListUsageMeteringDailyRecordsResponse.from_dict(list_usage_metering_daily_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


