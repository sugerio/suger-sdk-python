# GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_aws_account_id** | **str** | The CustomerAWSAccountID parameter specifies the AWS account ID of the buyer. | [optional] 
**customer_identifier** | **str** | The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application. | [optional] 
**dimension** | **str** | During the process of registering a product on Amazon Web Services Marketplace, dimensions are specified. These represent different units of value in your application.  This member is required. | [optional] 
**license_arn** | **str** |  | [optional] 
**quantity** | **int** | The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified. | [optional] 
**timestamp** | **str** | Timestamp, in UTC, for which the usage is being reported.  Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.  This member is required. | [optional] 
**usage_allocations** | [**List[GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageAllocation]**](GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageAllocation.md) | The set of UsageAllocations to submit. The sum of all UsageAllocation quantities must equal the Quantity of the UsageRecord . | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_usage_record import GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord from a JSON string
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_usage_record_instance = GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord.from_json(json)
# print the JSON string representation of the object
print(GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord.to_json())

# convert the object into a dict
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_usage_record_dict = github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_usage_record_instance.to_dict()
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord from a dict
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_usage_record_from_dict = GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesUsageRecord.from_dict(github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


