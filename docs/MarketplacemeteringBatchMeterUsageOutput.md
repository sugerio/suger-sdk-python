# MarketplacemeteringBatchMeterUsageOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_metadata** | **object** |  | [optional] 
**results** | [**List[TypesUsageRecordResult]**](TypesUsageRecordResult.md) | Contains all UsageRecords processed by BatchMeterUsage. These records were either honored by AWS Marketplace Metering Service or were invalid. Invalid records should be fixed before being resubmitted. | [optional] 
**unprocessed_records** | [**List[TypesUsageRecord]**](TypesUsageRecord.md) | Contains all UsageRecords that were not processed by BatchMeterUsage. This is a list of UsageRecords. You can retry the failed request by making another BatchMeterUsage call with this list as input in the BatchMeterUsageRequest. | [optional] 

## Example

```python
from openapi_client.models.marketplacemetering_batch_meter_usage_output import MarketplacemeteringBatchMeterUsageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacemeteringBatchMeterUsageOutput from a JSON string
marketplacemetering_batch_meter_usage_output_instance = MarketplacemeteringBatchMeterUsageOutput.from_json(json)
# print the JSON string representation of the object
print MarketplacemeteringBatchMeterUsageOutput.to_json()

# convert the object into a dict
marketplacemetering_batch_meter_usage_output_dict = marketplacemetering_batch_meter_usage_output_instance.to_dict()
# create an instance of MarketplacemeteringBatchMeterUsageOutput from a dict
marketplacemetering_batch_meter_usage_output_form_dict = marketplacemetering_batch_meter_usage_output.from_dict(marketplacemetering_batch_meter_usage_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


