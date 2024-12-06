# GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | One part of a key-value pair that makes up a tag . A key is a label that acts like a category for the specific tag values.  This member is required. | [optional] 
**value** | **str** | One part of a key-value pair that makes up a tag . A value acts as a descriptor within a tag category (key). The value can be empty or null.  This member is required. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_tag import GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag from a JSON string
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_tag_instance = GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag.from_json(json)
# print the JSON string representation of the object
print(GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag.to_json())

# convert the object into a dict
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_tag_dict = github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_tag_instance.to_dict()
# create an instance of GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag from a dict
github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_tag_from_dict = GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag.from_dict(github_com_aws_aws_sdk_go_v2_service_marketplacemetering_types_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


