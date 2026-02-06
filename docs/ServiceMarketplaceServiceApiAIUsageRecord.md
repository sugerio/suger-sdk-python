# ServiceMarketplaceServiceApiAIUsageRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_microcents** | **int** | CostMicrocents is the total cost in microcents. | [optional] 
**cost_usd** | **float** | CostUSD is the total cost in USD. | [optional] 
**hour_bucket** | **str** | HourBucket is the hour this record represents. | [optional] 
**input_tokens** | **int** | InputTokens is the total input tokens for this hour. | [optional] 
**is_byok** | **bool** | IsBYOK indicates if the organization&#39;s own API key was used. | [optional] 
**model** | **str** | Model is the model name. | [optional] 
**output_tokens** | **int** | OutputTokens is the total output tokens for this hour. | [optional] 
**provider** | **str** | Provider is the AI provider (openai, anthropic, gemini). | [optional] 
**request_count** | **int** | RequestCount is the number of requests in this hour. | [optional] 
**user_id** | **str** | UserID is the user who made the requests (empty if unattributed). | [optional] 

## Example

```python
from suger_sdk_python.models.service_marketplace_service_api_ai_usage_record import ServiceMarketplaceServiceApiAIUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMarketplaceServiceApiAIUsageRecord from a JSON string
service_marketplace_service_api_ai_usage_record_instance = ServiceMarketplaceServiceApiAIUsageRecord.from_json(json)
# print the JSON string representation of the object
print(ServiceMarketplaceServiceApiAIUsageRecord.to_json())

# convert the object into a dict
service_marketplace_service_api_ai_usage_record_dict = service_marketplace_service_api_ai_usage_record_instance.to_dict()
# create an instance of ServiceMarketplaceServiceApiAIUsageRecord from a dict
service_marketplace_service_api_ai_usage_record_from_dict = ServiceMarketplaceServiceApiAIUsageRecord.from_dict(service_marketplace_service_api_ai_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


