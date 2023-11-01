# openapi_client.APIApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_client**](APIApi.md#create_api_client) | **POST** /org/{orgId}/apiClient | create api client
[**get_api_client**](APIApi.md#get_api_client) | **GET** /org/{orgId}/apiClient/{apiClientId} | get api client
[**get_api_client_access_token**](APIApi.md#get_api_client_access_token) | **POST** /public/apiClient/accessToken | get api access token
[**list_api_clients**](APIApi.md#list_api_clients) | **GET** /org/{orgId}/apiClient | list api clients


# **create_api_client**
> GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient create_api_client(org_id, type=type)

create api client

Create an API client to access Suger API. Please note that only one API client is permitted per organization at this moment.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_identity_api_client import GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerTokenAuth
configuration.api_key['BearerTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    type = 'type_example' # str | API client type, the default is BEARER_TOKEN if not provided (optional)

    try:
        # create api client
        api_response = api_instance.create_api_client(org_id, type=type)
        print("The response of APIApi->create_api_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->create_api_client: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **type** | **str**| API client type, the default is BEARER_TOKEN if not provided | [optional] 

### Return type

[**GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient**](GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

# **get_api_client**
> GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient get_api_client(org_id, api_client_id)

get api client

Get the API client by ID.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_identity_api_client import GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerTokenAuth
configuration.api_key['BearerTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIApi(api_client)
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

[**GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient**](GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

# **get_api_client_access_token**
> ApiClientAccessToken get_api_client_access_token(data)

get api access token

Get the Bearer Access Token by giving the Suger API Client ID & Client Secret.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.api_client_access_token import ApiClientAccessToken
from openapi_client.models.get_api_client_access_token_params import GetApiClientAccessTokenParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIApi(api_client)
    data = openapi_client.GetApiClientAccessTokenParams() # GetApiClientAccessTokenParams | Suger API Client

    try:
        # get api access token
        api_response = api_instance.get_api_client_access_token(data)
        print("The response of APIApi->get_api_client_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->get_api_client_access_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GetApiClientAccessTokenParams**](GetApiClientAccessTokenParams.md)| Suger API Client | 

### Return type

[**ApiClientAccessToken**](ApiClientAccessToken.md)

### Authorization

No authorization required

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

# **list_api_clients**
> List[GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient] list_api_clients(org_id)

list api clients

List all API clients in the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_identity_api_client import GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerTokenAuth
configuration.api_key['BearerTokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIApi(api_client)
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

[**List[GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient]**](GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

