# suger_sdk_python.APIApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_client**](APIApi.md#get_api_client) | **GET** /org/{orgId}/apiClient/{apiClientId} | get api client
[**list_api_clients**](APIApi.md#list_api_clients) | **GET** /org/{orgId}/apiClient | list api clients


# **get_api_client**
> GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient get_api_client(org_id, api_client_id)

get api client

Get the API client by ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_identity_api_client import GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient
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
    api_instance = suger_sdk_python.APIApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    api_client_id = 'api_client_id_example' # str | API client ID

    try:
        # get api client
        api_response = api_instance.get_api_client(org_id, api_client_id)
        print("The response of APIApi->get_api_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->get_api_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **api_client_id** | **str**| API client ID | 

### Return type

[**GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient.md)

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

# **list_api_clients**
> List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient] list_api_clients(org_id)

list api clients

List all API clients in the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_identity_api_client import GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient
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
    api_instance = suger_sdk_python.APIApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # list api clients
        api_response = api_instance.list_api_clients(org_id)
        print("The response of APIApi->list_api_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->list_api_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibIdentityApiClient.md)

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

