# openapi_client.EntitlementApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entitlement_credit**](EntitlementApi.md#add_entitlement_credit) | **POST** /org/{orgId}/entitlement/{entitlementId}/addCredit | add entitlement credit
[**approve_entitlement**](EntitlementApi.md#approve_entitlement) | **POST** /org/{orgId}/entitlement/{entitlementId}/approve | approve entitlement
[**divide_entitlement_commit**](EntitlementApi.md#divide_entitlement_commit) | **POST** /org/{orgId}/entitlement/{entitlementId}/divideCommit | divide entitlement commit
[**get_entitlement**](EntitlementApi.md#get_entitlement) | **GET** /org/{orgId}/entitlement/{entitlementId} | get entitlement
[**list_entitlements**](EntitlementApi.md#list_entitlements) | **GET** /org/{orgId}/entitlement | list entitlements
[**list_entitlements_by_buyer**](EntitlementApi.md#list_entitlements_by_buyer) | **GET** /org/{orgId}/buyer/{buyerId}/entitlement | list entitlements by buyer
[**list_entitlements_by_offer**](EntitlementApi.md#list_entitlements_by_offer) | **GET** /org/{orgId}/offer/{offerId}/entitlement | list entitlements by offer
[**list_entitlements_by_partner**](EntitlementApi.md#list_entitlements_by_partner) | **GET** /org/{orgId}/partner/{partner}/entitlement | list entitlements by partner
[**list_entitlements_by_product**](EntitlementApi.md#list_entitlements_by_product) | **GET** /org/{orgId}/product/{productId}/entitlement | list entitlements by product
[**update_entitlement_meta_info**](EntitlementApi.md#update_entitlement_meta_info) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/metaInfo | update entitlement meta info
[**update_entitlement_name**](EntitlementApi.md#update_entitlement_name) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/entitlementName | update entitlement name


# **add_entitlement_credit**
> AddEntitlementCreditResponse add_entitlement_credit(org_id, entitlement_id, data)

add entitlement credit

Add the credit amount to the given Entitlement. The credit amount is accumulated & saved in the current Entitlement Term of the gvien Entitlement.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.add_entitlement_credit_params import AddEntitlementCreditParams
from openapi_client.models.add_entitlement_credit_response import AddEntitlementCreditResponse
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = openapi_client.AddEntitlementCreditParams() # AddEntitlementCreditParams | RequestBody

    try:
        # add entitlement credit
        api_response = api_instance.add_entitlement_credit(org_id, entitlement_id, data)
        print("The response of EntitlementApi->add_entitlement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->add_entitlement_credit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**AddEntitlementCreditParams**](AddEntitlementCreditParams.md)| RequestBody | 

### Return type

[**AddEntitlementCreditResponse**](AddEntitlementCreditResponse.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_entitlement**
> WorkloadEntitlement approve_entitlement(org_id, entitlement_id)

approve entitlement

Approve the given Entitlement. Only applicable to the GCP Entitlements with the status of \"PENDING_START\". Return 200 if the entitlement is already active.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID

    try:
        # approve entitlement
        api_response = api_instance.approve_entitlement(org_id, entitlement_id)
        print("The response of EntitlementApi->approve_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->approve_entitlement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **divide_entitlement_commit**
> str divide_entitlement_commit(org_id, entitlement_id, data)

divide entitlement commit

Divide the commit equally from the given entitlement into sub entitlement terms based on the given time periods.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.divide_entitlement_commit_params import DivideEntitlementCommitParams
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = openapi_client.DivideEntitlementCommitParams() # DivideEntitlementCommitParams | RequestBody

    try:
        # divide entitlement commit
        api_response = api_instance.divide_entitlement_commit(org_id, entitlement_id, data)
        print("The response of EntitlementApi->divide_entitlement_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->divide_entitlement_commit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**DivideEntitlementCommitParams**](DivideEntitlementCommitParams.md)| RequestBody | 

### Return type

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

# **get_entitlement**
> WorkloadEntitlement get_entitlement(org_id, entitlement_id)

get entitlement

Get the entitlement by ID

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID

    try:
        # get entitlement
        api_response = api_instance.get_entitlement(org_id, entitlement_id)
        print("The response of EntitlementApi->get_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->get_entitlement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entitlements**
> List[WorkloadEntitlement] list_entitlements(org_id)

list entitlements

List all entitlements under the organization

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # list entitlements
        api_response = api_instance.list_entitlements(org_id)
        print("The response of EntitlementApi->list_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[WorkloadEntitlement]**](WorkloadEntitlement.md)

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

# **list_entitlements_by_buyer**
> List[WorkloadEntitlement] list_entitlements_by_buyer(org_id, buyer_id)

list entitlements by buyer

List all entitlements of the given buyer

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID

    try:
        # list entitlements by buyer
        api_response = api_instance.list_entitlements_by_buyer(org_id, buyer_id)
        print("The response of EntitlementApi->list_entitlements_by_buyer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlements_by_buyer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 

### Return type

[**List[WorkloadEntitlement]**](WorkloadEntitlement.md)

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

# **list_entitlements_by_offer**
> List[WorkloadEntitlement] list_entitlements_by_offer(org_id, offer_id)

list entitlements by offer

List all entitlements under the given offer

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # list entitlements by offer
        api_response = api_instance.list_entitlements_by_offer(org_id, offer_id)
        print("The response of EntitlementApi->list_entitlements_by_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlements_by_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 

### Return type

[**List[WorkloadEntitlement]**](WorkloadEntitlement.md)

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

# **list_entitlements_by_partner**
> List[WorkloadEntitlement] list_entitlements_by_partner(org_id, partner)

list entitlements by partner

List all entitlements under the given partner

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner

    try:
        # list entitlements by partner
        api_response = api_instance.list_entitlements_by_partner(org_id, partner)
        print("The response of EntitlementApi->list_entitlements_by_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlements_by_partner: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 

### Return type

[**List[WorkloadEntitlement]**](WorkloadEntitlement.md)

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

# **list_entitlements_by_product**
> List[WorkloadEntitlement] list_entitlements_by_product(org_id, product_id)

list entitlements by product

List all entitlements under the given product

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID

    try:
        # list entitlements by product
        api_response = api_instance.list_entitlements_by_product(org_id, product_id)
        print("The response of EntitlementApi->list_entitlements_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlements_by_product: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 

### Return type

[**List[WorkloadEntitlement]**](WorkloadEntitlement.md)

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

# **update_entitlement_meta_info**
> WorkloadMetaInfo update_entitlement_meta_info(org_id, entitlement_id, data)

update entitlement meta info

Update the meta info of the given entitlement.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_meta_info import WorkloadMetaInfo
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = openapi_client.WorkloadMetaInfo() # WorkloadMetaInfo | Entitlement meta info to update

    try:
        # update entitlement meta info
        api_response = api_instance.update_entitlement_meta_info(org_id, entitlement_id, data)
        print("The response of EntitlementApi->update_entitlement_meta_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->update_entitlement_meta_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md)| Entitlement meta info to update | 

### Return type

[**WorkloadMetaInfo**](WorkloadMetaInfo.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entitlement_name**
> WorkloadEntitlement update_entitlement_name(org_id, entitlement_id, data)

update entitlement name

Update the name of the given Entitlement

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.github_com_sugerio_marketplace_service_rds_db_lib_update_entitlement_name_params import GithubComSugerioMarketplaceServiceRdsDbLibUpdateEntitlementNameParams
from openapi_client.models.workload_entitlement import WorkloadEntitlement
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
    api_instance = openapi_client.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = openapi_client.GithubComSugerioMarketplaceServiceRdsDbLibUpdateEntitlementNameParams() # GithubComSugerioMarketplaceServiceRdsDbLibUpdateEntitlementNameParams | UpdateEntitlementNameParams

    try:
        # update entitlement name
        api_response = api_instance.update_entitlement_name(org_id, entitlement_id, data)
        print("The response of EntitlementApi->update_entitlement_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->update_entitlement_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**GithubComSugerioMarketplaceServiceRdsDbLibUpdateEntitlementNameParams**](GithubComSugerioMarketplaceServiceRdsDbLibUpdateEntitlementNameParams.md)| UpdateEntitlementNameParams | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

