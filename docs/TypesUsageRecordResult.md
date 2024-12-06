# TypesUsageRecordResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering_record_id** | **str** | The MeteringRecordId is a unique identifier for this metering event. | [optional] 
**status** | [**TypesUsageRecordResultStatus**](TypesUsageRecordResultStatus.md) | The UsageRecordResult Status indicates the status of an individual UsageRecord processed by BatchMeterUsage .   - Success- The UsageRecord was accepted and honored by BatchMeterUsage .   - CustomerNotSubscribed- The CustomerIdentifier specified is not able to use   your product. The UsageRecord was not honored. There are three causes for this   result:   - The customer identifier is invalid.   - The customer identifier provided in the metering record does not have an   active agreement or subscription with this product. Future UsageRecords for   this customer will fail until the customer subscribes to your product.   - The customer&#39;s AWS account was suspended.   - DuplicateRecord- Indicates that the UsageRecord was invalid and not honored.   A previously metered UsageRecord had the same customer, dimension, and time,   but a different quantity. | [optional] 
**usage_record** | [**TypesUsageRecord**](TypesUsageRecord.md) | The UsageRecord that was part of the BatchMeterUsage request. | [optional] 

## Example

```python
from suger_sdk_python.models.types_usage_record_result import TypesUsageRecordResult

# TODO update the JSON string below
json = "{}"
# create an instance of TypesUsageRecordResult from a JSON string
types_usage_record_result_instance = TypesUsageRecordResult.from_json(json)
# print the JSON string representation of the object
print(TypesUsageRecordResult.to_json())

# convert the object into a dict
types_usage_record_result_dict = types_usage_record_result_instance.to_dict()
# create an instance of TypesUsageRecordResult from a dict
types_usage_record_result_from_dict = TypesUsageRecordResult.from_dict(types_usage_record_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


