# GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | Dimension identifier | [optional] 
**effective_start_time** | **str** | Time in UTC when the usage event occurred | [optional] 
**error** | [**GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventConflictResponse**](GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventConflictResponse.md) |  | [optional] 
**message_time** | **str** | Time this message was created in UTC | [optional] 
**plan_id** | **str** | Plan associated with the purchased offer | [optional] 
**quantity** | **float** | Number of units consumed | [optional] 
**resource_id** | **str** | Identifier of the resource against which usage is emitted | [optional] 
**resource_uri** | **str** | Identifier of the managed app resource against which usage is emitted | [optional] 
**status** | [**GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventStatusEnum**](GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageEventStatusEnum.md) | Status of the operation. | [optional] 
**usage_event_id** | **str** | Unique identifier associated with the usage event | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_batch_event_ok_message import GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage from a JSON string
github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_batch_event_ok_message_instance = GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_batch_event_ok_message_dict = github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_batch_event_ok_message_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage from a dict
github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_batch_event_ok_message_from_dict = GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage.from_dict(github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_usage_batch_event_ok_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


