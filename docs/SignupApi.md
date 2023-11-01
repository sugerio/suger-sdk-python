# openapi_client.SignupApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_signup_page_config_info**](SignupApi.md#get_client_signup_page_config_info) | **GET** /org/{orgId}/clientSignupPageConfigInfo | get client signup page config info
[**update_client_signup_page_config_info**](SignupApi.md#update_client_signup_page_config_info) | **PATCH** /org/{orgId}/clientSignupPageConfigInfo | update client signup page config info


# **get_client_signup_page_config_info**
> ClientSignupPageConfigInfo get_client_signup_page_config_info(org_id)

get client signup page config info

Get the client signup page config info of the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.client_signup_page_config_info import ClientSignupPageConfigInfo
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
    api_instance = openapi_client.SignupApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # get client signup page config info
        api_response = api_instance.get_client_signup_page_config_info(org_id)
        print("The response of SignupApi->get_client_signup_page_config_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignupApi->get_client_signup_page_config_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**ClientSignupPageConfigInfo**](ClientSignupPageConfigInfo.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client signup page config info |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_signup_page_config_info**
> ClientSignupPageConfigInfo update_client_signup_page_config_info(org_id, data)

update client signup page config info

Update the client signup page config info of the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.client_signup_page_config_info import ClientSignupPageConfigInfo
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
    api_instance = openapi_client.SignupApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = openapi_client.ClientSignupPageConfigInfo() # ClientSignupPageConfigInfo | The client signup page config info to update with

    try:
        # update client signup page config info
        api_response = api_instance.update_client_signup_page_config_info(org_id, data)
        print("The response of SignupApi->update_client_signup_page_config_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignupApi->update_client_signup_page_config_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**ClientSignupPageConfigInfo**](ClientSignupPageConfigInfo.md)| The client signup page config info to update with | 

### Return type

[**ClientSignupPageConfigInfo**](ClientSignupPageConfigInfo.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated client signup page config info |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

