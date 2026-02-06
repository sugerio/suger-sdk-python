# suger_sdk_python.SearchApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_searchable_objects**](SearchApi.md#list_searchable_objects) | **GET** /org/{orgId}/search | Global search


# **list_searchable_objects**
> SearchResponse list_searchable_objects(org_id, q, types=types, limit=limit, cursor=cursor)

Global search

Search across products, offers, etc. using fuzzy name + full-text match.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.search_response import SearchResponse
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
    api_instance = suger_sdk_python.SearchApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    q = 'q_example' # str | Search query
    types = 'types_example' # str | Comma-separated object types (e.g. product,offer) (optional)
    limit = 56 # int | Page size (default 20) (optional)
    cursor = 'cursor_example' # str | Cursor (offset:query base64 encoded) (optional)

    try:
        # Global search
        api_response = api_instance.list_searchable_objects(org_id, q, types=types, limit=limit, cursor=cursor)
        print("The response of SearchApi->list_searchable_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->list_searchable_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **q** | **str**| Search query | 
 **types** | **str**| Comma-separated object types (e.g. product,offer) | [optional] 
 **limit** | **int**| Page size (default 20) | [optional] 
 **cursor** | **str**| Cursor (offset:query base64 encoded) | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search response with items and nextCursor |  -  |
**400** | Bad request error |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

