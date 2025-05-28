# suger_sdk_python.EntitlementApi

All URIs are relative to *http://https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entitlement_credit**](EntitlementApi.md#add_entitlement_credit) | **POST** /org/{orgId}/entitlement/{entitlementId}/addCredit | add entitlement credit
[**apply_addon_to_entitlement**](EntitlementApi.md#apply_addon_to_entitlement) | **POST** /org/{orgId}/entitlement/{entitlementId}/addon | apply addon to entitlement
[**approve_entitlement**](EntitlementApi.md#approve_entitlement) | **POST** /org/{orgId}/entitlement/{entitlementId}/approve | approve entitlement
[**cancel_entitlement**](EntitlementApi.md#cancel_entitlement) | **POST** /org/{orgId}/entitlement/{entitlementId}/cancel | cancel entitlement
[**create_entitlement**](EntitlementApi.md#create_entitlement) | **POST** /org/{orgId}/entitlement | create entitlement
[**delete_entitlement_term**](EntitlementApi.md#delete_entitlement_term) | **DELETE** /org/{orgId}/entitlement/{entitlementId}/entitlementTerm/{entitlementTermId} | delete entitlement term
[**divide_entitlement_commit**](EntitlementApi.md#divide_entitlement_commit) | **POST** /org/{orgId}/entitlement/{entitlementId}/divideCommit | divide entitlement commit
[**get_entitlement**](EntitlementApi.md#get_entitlement) | **GET** /org/{orgId}/entitlement/{entitlementId} | get entitlement
[**get_entitlement_term**](EntitlementApi.md#get_entitlement_term) | **GET** /org/{orgId}/entitlement/{entitlementId}/entitlementTerm/{entitlementTermId} | get entitlement term
[**list_entitlement_terms**](EntitlementApi.md#list_entitlement_terms) | **GET** /org/{orgId}/entitlement/{entitlementId}/entitlementTerm | list entitlement terms
[**list_entitlements**](EntitlementApi.md#list_entitlements) | **GET** /org/{orgId}/entitlement | list entitlements
[**schedule_entitlement_cancellation**](EntitlementApi.md#schedule_entitlement_cancellation) | **POST** /org/{orgId}/entitlement/{entitlementId}/scheduleCancellation | schedule entitlement cancellation
[**unschedule_entitlement_cancellation**](EntitlementApi.md#unschedule_entitlement_cancellation) | **POST** /org/{orgId}/entitlement/{entitlementId}/unscheduleCancellation | unschedule entitlement cancellation
[**update_entitlement_meta_info**](EntitlementApi.md#update_entitlement_meta_info) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/metaInfo | update entitlement meta info
[**update_entitlement_name**](EntitlementApi.md#update_entitlement_name) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/entitlementName | update entitlement name
[**update_entitlement_price_model**](EntitlementApi.md#update_entitlement_price_model) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/priceModel | update entitlement price model
[**update_entitlement_seat**](EntitlementApi.md#update_entitlement_seat) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/seat | update seat for the active AZURE subscription


# **add_entitlement_credit**
> AddEntitlementCreditResponse add_entitlement_credit(org_id, entitlement_id, data)

add entitlement credit

Add the credit amount to the given Entitlement. The credit amount is accumulated & saved in the current Entitlement Term of the gvien Entitlement.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.add_entitlement_credit_params import AddEntitlementCreditParams
from suger_sdk_python.models.add_entitlement_credit_response import AddEntitlementCreditResponse
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.AddEntitlementCreditParams() # AddEntitlementCreditParams | RequestBody

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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **apply_addon_to_entitlement**
> WorkloadEntitlement apply_addon_to_entitlement(org_id, entitlement_id, data)

apply addon to entitlement

Apply one billing addon to the given Entitlement. The entitlement status must be ACTIVE.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_addon_record import BillingAddonRecord
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.BillingAddonRecord() # BillingAddonRecord | RequestBody

    try:
        # apply addon to entitlement
        api_response = api_instance.apply_addon_to_entitlement(org_id, entitlement_id, data)
        print("The response of EntitlementApi->apply_addon_to_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->apply_addon_to_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**BillingAddonRecord**](BillingAddonRecord.md)| RequestBody | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entitlement |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_entitlement**
> WorkloadEntitlement approve_entitlement(org_id, entitlement_id)

approve entitlement

Approve the given Entitlement. Only applicable to the Azure or GCP Entitlements with the status of "PENDING_START". Return 200 if the entitlement is already active.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **cancel_entitlement**
> WorkloadEntitlement cancel_entitlement(org_id, entitlement_id)

cancel entitlement

Cancel the active subscription in Azure Marketplace.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID

    try:
        # cancel entitlement
        api_response = api_instance.cancel_entitlement(org_id, entitlement_id)
        print("The response of EntitlementApi->cancel_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->cancel_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the canceled Entitlement |  -  |
**400** | Bad request error |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entitlement**
> WorkloadEntitlement create_entitlement(org_id, data)

create entitlement

Create an new entitlement for the given buyer & offer. Only applicable to non cloud billing partners.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.create_entitlement_params import CreateEntitlementParams
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.CreateEntitlementParams() # CreateEntitlementParams | RequestBody

    try:
        # create entitlement
        api_response = api_instance.create_entitlement(org_id, data)
        print("The response of EntitlementApi->create_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->create_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**CreateEntitlementParams**](CreateEntitlementParams.md)| RequestBody | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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

# **delete_entitlement_term**
> str delete_entitlement_term(org_id, entitlement_id, entitlement_term_id)

delete entitlement term

Delete the entitlement term by the given entitlement ID and entitlement term ID. Only allow to delete the divided entitlement term.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    entitlement_term_id = 'entitlement_term_id_example' # str | Entitlement Term ID

    try:
        # delete entitlement term
        api_response = api_instance.delete_entitlement_term(org_id, entitlement_id, entitlement_term_id)
        print("The response of EntitlementApi->delete_entitlement_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->delete_entitlement_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **entitlement_term_id** | **str**| Entitlement Term ID | 

### Return type

**str**

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

# **divide_entitlement_commit**
> str divide_entitlement_commit(org_id, entitlement_id, data)

divide entitlement commit

Divide the commit equally from the given entitlement into sub entitlement terms based on the given time periods.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.divide_entitlement_commit_params import DivideEntitlementCommitParams
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.DivideEntitlementCommitParams() # DivideEntitlementCommitParams | RequestBody

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

# **get_entitlement**
> WorkloadEntitlement get_entitlement(org_id, entitlement_id)

get entitlement

Get the entitlement by ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **get_entitlement_term**
> WorkloadEntitlementTerm get_entitlement_term(org_id, entitlement_id, entitlement_term_id)

get entitlement term

Get the entitlement term by ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement_term import WorkloadEntitlementTerm
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    entitlement_term_id = 'entitlement_term_id_example' # str | Entitlement Term ID

    try:
        # get entitlement term
        api_response = api_instance.get_entitlement_term(org_id, entitlement_id, entitlement_term_id)
        print("The response of EntitlementApi->get_entitlement_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->get_entitlement_term: %s\n" % e)
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

# **list_entitlement_terms**
> List[WorkloadEntitlementTerm] list_entitlement_terms(org_id, entitlement_id)

list entitlement terms

List all Entitlement Terms of the given Entitlement.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement_term import WorkloadEntitlementTerm
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID

    try:
        # list entitlement terms
        api_response = api_instance.list_entitlement_terms(org_id, entitlement_id)
        print("The response of EntitlementApi->list_entitlement_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlement_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 

### Return type

[**List[WorkloadEntitlementTerm]**](WorkloadEntitlementTerm.md)

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

# **list_entitlements**
> List[WorkloadEntitlement] list_entitlements(org_id, partner=partner, product_id=product_id, offer_id=offer_id, buyer_id=buyer_id, external_id=external_id, buyer_account_id=buyer_account_id, limit=limit, offset=offset)

list entitlements

List entitlements under the given organization with pagination and optional filters.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | filter by partner (optional)
    product_id = 'product_id_example' # str | filter by productId (optional)
    offer_id = 'offer_id_example' # str | filter by offerId (optional)
    buyer_id = 'buyer_id_example' # str | filter by buyerId (optional)
    external_id = 'external_id_example' # str | filter by externalId (optional)
    buyer_account_id = 'buyer_account_id_example' # str | filter by buyerAccountId is currently supported only for AWS (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list entitlements
        api_response = api_instance.list_entitlements(org_id, partner=partner, product_id=product_id, offer_id=offer_id, buyer_id=buyer_id, external_id=external_id, buyer_account_id=buyer_account_id, limit=limit, offset=offset)
        print("The response of EntitlementApi->list_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->list_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| filter by partner | [optional] 
 **product_id** | **str**| filter by productId | [optional] 
 **offer_id** | **str**| filter by offerId | [optional] 
 **buyer_id** | **str**| filter by buyerId | [optional] 
 **external_id** | **str**| filter by externalId | [optional] 
 **buyer_account_id** | **str**| filter by buyerAccountId is currently supported only for AWS | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[WorkloadEntitlement]**](WorkloadEntitlement.md)

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

# **schedule_entitlement_cancellation**
> WorkloadEntitlement schedule_entitlement_cancellation(org_id, entitlement_id, data)

schedule entitlement cancellation

Schedule the cancellation of the given Entitlement.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.cancellation_schedule import CancellationSchedule
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.CancellationSchedule() # CancellationSchedule | RequestBody

    try:
        # schedule entitlement cancellation
        api_response = api_instance.schedule_entitlement_cancellation(org_id, entitlement_id, data)
        print("The response of EntitlementApi->schedule_entitlement_cancellation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->schedule_entitlement_cancellation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**CancellationSchedule**](CancellationSchedule.md)| RequestBody | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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

# **unschedule_entitlement_cancellation**
> WorkloadEntitlement unschedule_entitlement_cancellation(org_id, entitlement_id)

unschedule entitlement cancellation

Unschedule the cancellation of the given Entitlement.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID

    try:
        # unschedule entitlement cancellation
        api_response = api_instance.unschedule_entitlement_cancellation(org_id, entitlement_id)
        print("The response of EntitlementApi->unschedule_entitlement_cancellation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->unschedule_entitlement_cancellation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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

# **update_entitlement_meta_info**
> WorkloadMetaInfo update_entitlement_meta_info(org_id, entitlement_id, data)

update entitlement meta info

Update the meta info of the given entitlement.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_meta_info import WorkloadMetaInfo
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.WorkloadMetaInfo() # WorkloadMetaInfo | Entitlement meta info to update

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

[APIKeyAuth](../README.md#APIKeyAuth)

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

Update the name of the given Entitlement.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_update_entitlement_name_params import GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams() # GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams | UpdateEntitlementNameParams

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
 **data** | [**GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams.md)| UpdateEntitlementNameParams | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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

# **update_entitlement_price_model**
> WorkloadEntitlement update_entitlement_price_model(org_id, entitlement_id, data)

update entitlement price model

Update the price model of the given entitlement, such as recurring commits, billable dimensions. Only applicable to non cloud billing partners.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.update_entitlement_price_model_params import UpdateEntitlementPriceModelParams
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.UpdateEntitlementPriceModelParams() # UpdateEntitlementPriceModelParams | Entitlement price model update params

    try:
        # update entitlement price model
        api_response = api_instance.update_entitlement_price_model(org_id, entitlement_id, data)
        print("The response of EntitlementApi->update_entitlement_price_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->update_entitlement_price_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**UpdateEntitlementPriceModelParams**](UpdateEntitlementPriceModelParams.md)| Entitlement price model update params | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

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
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entitlement_seat**
> WorkloadEntitlement update_entitlement_seat(org_id, entitlement_id, new_seat)

update seat for the active AZURE subscription

Update the seat number for the active AZURE subscription.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_entitlement import WorkloadEntitlement
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "http://https://api.suger.cloud"
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
    api_instance = suger_sdk_python.EntitlementApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    new_seat = 56 # int | New seat number

    try:
        # update seat for the active AZURE subscription
        api_response = api_instance.update_entitlement_seat(org_id, entitlement_id, new_seat)
        print("The response of EntitlementApi->update_entitlement_seat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementApi->update_entitlement_seat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **new_seat** | **int**| New seat number | 

### Return type

[**WorkloadEntitlement**](WorkloadEntitlement.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the original entitlement before the seat update |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

