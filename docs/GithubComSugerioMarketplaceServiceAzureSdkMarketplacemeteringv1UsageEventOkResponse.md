# GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | Dimension identifier | [optional] 
**effective_start_time** | **str** | Time in UTC when the usage event occurred | [optional] 
**message_time** | **str** | Time this message was created in UTC | [optional] 
**plan_id** | **str** | Plan associated with the purchased offer | [optional] 
**quantity** | **float** | Number of units consumed | [optional] 
**resource_id** | **str** | Identifier of the resource against which usage is emitted | [optional] 
**resource_uri** | **str** | Identifier of the managed app resource against which usage is emitted | [optional] 
**status** | [**GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventStatusEnum**](GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventStatusEnum.md) | Status of the operation. | [optional] 
**usage_event_id** | **str** | Unique identifier associated with the usage event | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response import GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse from a JSON string
github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response_instance = GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response_dict = github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse from a dict
github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response_from_dict = GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse.from_dict(github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


