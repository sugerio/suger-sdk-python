# suger_sdk_python.OperationApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_operation_v2**](OperationApi.md#get_operation_v2) | **GET** /org/{orgId}/v2/operation/{operationId} | get operation details
[**list_operation_history_v2**](OperationApi.md#list_operation_history_v2) | **GET** /org/{orgId}/v2/operation/{operationId}/history | get operation history events
[**list_operations_v2**](OperationApi.md#list_operations_v2) | **POST** /org/{orgId}/v2/operation/list | list operations with filters


# **get_operation_v2**
> Operation get_operation_v2(org_id, operation_id, run_id=run_id, has_children=has_children)

get operation details

Get the details of a Temporal workflow operation by operation ID. Optionally include child workflow data.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.operation import Operation
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
    api_instance = suger_sdk_python.OperationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    operation_id = 'operation_id_example' # str | Temporal Workflow ID
    run_id = 'run_id_example' # str | Temporal run ID of the workflow (optional)
    has_children = True # bool | Include data aggregated from all child workflows (1 level), default false (optional)

    try:
        # get operation details
        api_response = api_instance.get_operation_v2(org_id, operation_id, run_id=run_id, has_children=has_children)
        print("The response of OperationApi->get_operation_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationApi->get_operation_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **operation_id** | **str**| Temporal Workflow ID | 
 **run_id** | **str**| Temporal run ID of the workflow | [optional] 
 **has_children** | **bool**| Include data aggregated from all child workflows (1 level), default false | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operation_history_v2**
> OperationEventsResponse list_operation_history_v2(org_id, operation_id)

get operation history events

Get the history events for a Temporal workflow operation by operation ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.operation_events_response import OperationEventsResponse
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
    api_instance = suger_sdk_python.OperationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    operation_id = 'operation_id_example' # str | Temporal Workflow ID

    try:
        # get operation history events
        api_response = api_instance.list_operation_history_v2(org_id, operation_id)
        print("The response of OperationApi->list_operation_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationApi->list_operation_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **operation_id** | **str**| Temporal Workflow ID | 

### Return type

[**OperationEventsResponse**](OperationEventsResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_v2**
> ListOperationsResponse list_operations_v2(org_id, request)

list operations with filters

List or search Temporal workflow operations with flexible filter expressions.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_operations_response import ListOperationsResponse
from suger_sdk_python.models.list_operations_v2_request import ListOperationsV2Request
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
    api_instance = suger_sdk_python.OperationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    request = suger_sdk_python.ListOperationsV2Request() # ListOperationsV2Request | Supports logical operators (and/or) and comparison operators (=, !=, in, not_in).

    try:
        # list operations with filters
        api_response = api_instance.list_operations_v2(org_id, request)
        print("The response of OperationApi->list_operations_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationApi->list_operations_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **request** | [**ListOperationsV2Request**](ListOperationsV2Request.md)| Supports logical operators (and/or) and comparison operators (&#x3D;, !&#x3D;, in, not_in). | 

### Return type

[**ListOperationsResponse**](ListOperationsResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

