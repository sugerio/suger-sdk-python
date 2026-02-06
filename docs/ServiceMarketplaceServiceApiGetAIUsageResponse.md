# ServiceMarketplaceServiceApiGetAIUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** | EndTime is the end of the queried time range. | [optional] 
**has_more** | **bool** | HasMore indicates if there are more records available beyond the current page. | [optional] 
**limit** | **int** | Limit is the limit used for this query. | [optional] 
**offset** | **int** | Offset is the offset used for this query. | [optional] 
**records** | [**List[ServiceMarketplaceServiceApiAIUsageRecord]**](ServiceMarketplaceServiceApiAIUsageRecord.md) | Records contains the usage records for the time range. | [optional] 
**start_time** | **str** | StartTime is the start of the queried time range. | [optional] 
**total_count** | **int** | TotalCount is the total number of records matching the query (before pagination). | [optional] 

## Example

```python
from suger_sdk_python.models.service_marketplace_service_api_get_ai_usage_response import ServiceMarketplaceServiceApiGetAIUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMarketplaceServiceApiGetAIUsageResponse from a JSON string
service_marketplace_service_api_get_ai_usage_response_instance = ServiceMarketplaceServiceApiGetAIUsageResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceMarketplaceServiceApiGetAIUsageResponse.to_json())

# convert the object into a dict
service_marketplace_service_api_get_ai_usage_response_dict = service_marketplace_service_api_get_ai_usage_response_instance.to_dict()
# create an instance of ServiceMarketplaceServiceApiGetAIUsageResponse from a dict
service_marketplace_service_api_get_ai_usage_response_from_dict = ServiceMarketplaceServiceApiGetAIUsageResponse.from_dict(service_marketplace_service_api_get_ai_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


