# ListUsageRecordReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** |  | [optional] 
**usage_record_reports** | [**List[MeteringUsageRecordReport]**](MeteringUsageRecordReport.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.list_usage_record_reports_response import ListUsageRecordReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsageRecordReportsResponse from a JSON string
list_usage_record_reports_response_instance = ListUsageRecordReportsResponse.from_json(json)
# print the JSON string representation of the object
print(ListUsageRecordReportsResponse.to_json())

# convert the object into a dict
list_usage_record_reports_response_dict = list_usage_record_reports_response_instance.to_dict()
# create an instance of ListUsageRecordReportsResponse from a dict
list_usage_record_reports_response_from_dict = ListUsageRecordReportsResponse.from_dict(list_usage_record_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


