# openapi_client.EntitlementTermApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entitlement_term**](EntitlementTermApi.md#get_entitlement_term) | **GET** /org/{orgId}/entitlement/{entitlementId}/entitlementTerm/{entitlementTermId} | get entitlement term
[**list_entitlement_terms**](EntitlementTermApi.md#list_entitlement_terms) | **GET** /org/{orgId}/entitlement/{entitlementId}/entitlementTerm | list entitlement terms


# **get_entitlement_term**
> WorkloadEntitlementTerm get_entitlement_term(org_id, entitlement_id, entitlement_term_id)

get entitlement term

Get the entitlement term by ID

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement_term import WorkloadEntitlementTerm
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
    api_instance = openapi_client.EntitlementTermApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    entitlement_term_id = 'entitlement_term_id_example' # str | Entitlement Term ID

    try:
        # get entitlement term
        api_response = api_instance.get_entitlement_term(org_id, entitlement_id, entitlement_term_id)
        print("The response of EntitlementTermApi->get_entitlement_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementTermApi->get_entitlement_term: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **entitlement_term_id** | **str**| Entitlement Term ID | 

### Return type

[**WorkloadEntitlementTerm**](WorkloadEntitlementTerm.md)

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

# **list_entitlement_terms**
> List[WorkloadEntitlementTerm] list_entitlement_terms(org_id, entitlement_id)

list entitlement terms

List all Entitlement Terms of the given Entitlement

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement_term import WorkloadEntitlementTerm
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
    api_instance = openapi_client.EntitlementTermApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID

    try:
        # list entitlement terms
        api_response = api_instance.list_entitlement_terms(org_id, entitlement_id)
        print("The response of EntitlementTermApi->list_entitlement_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementTermApi->list_entitlement_terms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 

### Return type

[**List[WorkloadEntitlementTerm]**](WorkloadEntitlementTerm.md)

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

