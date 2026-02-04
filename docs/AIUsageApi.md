# suger_sdk_python.AIUsageApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_usage**](AIUsageApi.md#get_ai_usage) | **GET** /org/{orgId}/ai-usage | Get AI usage data


# **get_ai_usage**
> ServiceMarketplaceServiceApiGetAIUsageResponse get_ai_usage(org_id, start_time, end_time, limit=limit, offset=offset)

Get AI usage data

Returns AI token usage records for the specified time range (max 90 days). Records are hourly aggregates that can be further grouped by the client. Supports pagination via limit and offset parameters.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.service_marketplace_service_api_get_ai_usage_response import ServiceMarketplaceServiceApiGetAIUsageResponse
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "https://api.suger.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with suger_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suger_sdk_python.AIUsageApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    start_time = 'start_time_example' # str | Start time (RFC3339 format)
    end_time = 'end_time_example' # str | End time (RFC3339 format)
    limit = 56 # int | Maximum number of records to return (default: 1000, max: 10000) (optional)
    offset = 56 # int | Number of records to skip for pagination (default: 0) (optional)

    try:
        # Get AI usage data
        api_response = api_instance.get_ai_usage(org_id, start_time, end_time, limit=limit, offset=offset)
        print("The response of AIUsageApi->get_ai_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIUsageApi->get_ai_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **start_time** | **str**| Start time (RFC3339 format) | 
 **end_time** | **str**| End time (RFC3339 format) | 
 **limit** | **int**| Maximum number of records to return (default: 1000, max: 10000) | [optional] 
 **offset** | **int**| Number of records to skip for pagination (default: 0) | [optional] 

### Return type

[**ServiceMarketplaceServiceApiGetAIUsageResponse**](ServiceMarketplaceServiceApiGetAIUsageResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI usage records with pagination info |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

