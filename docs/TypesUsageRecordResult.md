# TypesUsageRecordResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering_record_id** | **str** | The MeteringRecordId is a unique identifier for this metering event. | [optional] 
**status** | [**TypesUsageRecordResultStatus**](TypesUsageRecordResultStatus.md) |  | [optional] 
**usage_record** | [**TypesUsageRecord**](TypesUsageRecord.md) |  | [optional] 

## Example

```python
from openapi_client.models.types_usage_record_result import TypesUsageRecordResult

# TODO update the JSON string below
json = "{}"
# create an instance of TypesUsageRecordResult from a JSON string
types_usage_record_result_instance = TypesUsageRecordResult.from_json(json)
# print the JSON string representation of the object
print TypesUsageRecordResult.to_json()

# convert the object into a dict
types_usage_record_result_dict = types_usage_record_result_instance.to_dict()
# create an instance of TypesUsageRecordResult from a dict
types_usage_record_result_form_dict = types_usage_record_result.from_dict(types_usage_record_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


