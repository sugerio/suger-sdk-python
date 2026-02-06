# GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_metadata** | **object** | Metadata pertaining to the operation&#39;s result. | [optional] 
**results** | [**List[GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecordResult]**](GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecordResult.md) | Contains all UsageRecords processed by BatchMeterUsage . These records were either honored by Amazon Web Services Marketplace Metering Service or were invalid. Invalid records should be fixed before being resubmitted. | [optional] 
**unprocessed_records** | [**List[GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord]**](GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord.md) | Contains all UsageRecords that were not processed by BatchMeterUsage . This is a list of UsageRecords . You can retry the failed request by making another BatchMeterUsage call with this list as input in the BatchMeterUsageRequest . | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_aws_aws_sdk_go_v2_service_marketplacemetering_batch_meter_usage_output import GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput from a JSON string
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_batch_meter_usage_output_instance = GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput.from_json(json)
# print the JSON string representation of the object
print(GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput.to_json())

# convert the object into a dict
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_batch_meter_usage_output_dict = github_com_aws_aws_sdk_go_v2_service_marketplacemetering_batch_meter_usage_output_instance.to_dict()
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput from a dict
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_batch_meter_usage_output_from_dict = GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringBatchMeterUsageOutput.from_dict(github_com_aws_aws_sdk_go_v2_service_marketplacemetering_batch_meter_usage_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


