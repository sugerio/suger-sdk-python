# suger_sdk_python.AuditingApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_auditing_events**](AuditingApi.md#query_auditing_events) | **GET** /org/{orgId}/auditingEvent/query | query auditing events


# **query_auditing_events**
> GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent query_auditing_events(org_id, page_size=page_size, page_number=page_number, q=q, s=s)

query auditing events

Query auditing events with advanced filtering, sorting, and pagination using CRUD query language. Supports complex filters, sorting by multiple fields, and pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event import GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent
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
    api_instance = suger_sdk_python.AuditingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    page_size = 56 # int | Number of items per page (default: 20, max: 1000) (optional)
    page_number = 56 # int | Page number (default: 1) (optional)
    q = 'q_example' # str | LISP-style filter expression (e.g., '(= event_type \\ (optional)
    s = 's_example' # str | Sort fields: 'field:asc,field2:desc' or '-field,field2' format (e.g., 'creation_time:desc,event_type:asc' or '-creation_time,event_type') (optional)

    try:
        # query auditing events
        api_response = api_instance.query_auditing_events(org_id, page_size=page_size, page_number=page_number, q=q, s=s)
        print("The response of AuditingApi->query_auditing_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditingApi->query_auditing_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **page_size** | **int**| Number of items per page (default: 20, max: 1000) | [optional] 
 **page_number** | **int**| Page number (default: 1) | [optional] 
 **q** | **str**| LISP-style filter expression (e.g., &#39;(&#x3D; event_type \\ | [optional] 
 **s** | **str**| Sort fields: &#39;field:asc,field2:desc&#39; or &#39;-field,field2&#39; format (e.g., &#39;creation_time:desc,event_type:asc&#39; or &#39;-creation_time,event_type&#39;) | [optional] 

### Return type

[**GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent**](GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of auditing events |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

