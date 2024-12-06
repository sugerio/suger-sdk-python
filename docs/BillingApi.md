# suger_sdk_python.BillingApi

All URIs are relative to *http://https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon**](BillingApi.md#create_addon) | **POST** /org/{orgId}/addon | create addon
[**create_refund**](BillingApi.md#create_refund) | **POST** /org/{orgId}/buyer/{buyerId}/paymentTransaction/{paymentTransactionId}/refund | create refund.
[**delete_addon**](BillingApi.md#delete_addon) | **DELETE** /org/{orgId}/addon/{addonId} | delete addon
[**get_addon**](BillingApi.md#get_addon) | **GET** /org/{orgId}/addon/{addonId} | get addon
[**get_invoice**](BillingApi.md#get_invoice) | **GET** /org/{orgId}/entitlement/{entitlementId}/invoice/{invoiceId} | get invoice
[**issue_invoice**](BillingApi.md#issue_invoice) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/invoice/{invoiceId}/issue | issue invoice
[**list_addons**](BillingApi.md#list_addons) | **GET** /org/{orgId}/addon | list addons
[**list_invoices**](BillingApi.md#list_invoices) | **GET** /org/{orgId}/invoice | list invoices
[**list_payment_transactions**](BillingApi.md#list_payment_transactions) | **GET** /org/{orgId}/paymentTransaction | list payment transactions
[**list_refund_of_payment_transaction**](BillingApi.md#list_refund_of_payment_transaction) | **GET** /org/{orgId}/buyer/{buyerId}/paymentTransaction/{paymentTransactionId}/refund | list refunds.
[**pay_invoice**](BillingApi.md#pay_invoice) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/invoice/{invoiceId}/pay | pay invoice
[**update_addon**](BillingApi.md#update_addon) | **PATCH** /org/{orgId}/addon/{addonId} | update addon
[**void_invoice**](BillingApi.md#void_invoice) | **PATCH** /org/{orgId}/entitlement/{entitlementId}/invoice/{invoiceId}/void | void invoice


# **create_addon**
> BillingAddon create_addon(org_id, data)

create addon

Create an addon template

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_addon import BillingAddon
from suger_sdk_python.models.create_and_update_addon_params import CreateAndUpdateAddonParams
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.CreateAndUpdateAddonParams() # CreateAndUpdateAddonParams | CreateAndUpdateAddonParams

    try:
        # create addon
        api_response = api_instance.create_addon(org_id, data)
        print("The response of BillingApi->create_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**CreateAndUpdateAddonParams**](CreateAndUpdateAddonParams.md)| CreateAndUpdateAddonParams | 

### Return type

[**BillingAddon**](BillingAddon.md)

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
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund**
> str create_refund(org_id, buyer_id, payment_transaction_id, amount)

create refund.

create refund on the payment transaction, support partial refunds multiple times.

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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    payment_transaction_id = 'payment_transaction_id_example' # str | Payment transaction ID
    amount = 3.4 # float | Refund amount

    try:
        # create refund.
        api_response = api_instance.create_refund(org_id, buyer_id, payment_transaction_id, amount)
        print("The response of BillingApi->create_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **payment_transaction_id** | **str**| Payment transaction ID | 
 **amount** | **float**| Refund amount | 

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
**200** | Empty string if succeed |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_addon**
> str delete_addon(org_id, addon_id)

delete addon

Soft delete an addon template

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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    addon_id = 'addon_id_example' # str | Addon ID

    try:
        # delete addon
        api_response = api_instance.delete_addon(org_id, addon_id)
        print("The response of BillingApi->delete_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->delete_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **addon_id** | **str**| Addon ID | 

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
**200** | Empty string if deletion is successful |  -  |
**400** | Bad request error |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon**
> BillingAddon get_addon(org_id, addon_id)

get addon

Get an addon template

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_addon import BillingAddon
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    addon_id = 'addon_id_example' # str | Addon ID

    try:
        # get addon
        api_response = api_instance.get_addon(org_id, addon_id)
        print("The response of BillingApi->get_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **addon_id** | **str**| Addon ID | 

### Return type

[**BillingAddon**](BillingAddon.md)

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
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> BillingInvoice get_invoice(org_id, entitlement_id, invoice_id)

get invoice

Get the invoice by ID

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_invoice import BillingInvoice
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    invoice_id = 'invoice_id_example' # str | Invoice ID

    try:
        # get invoice
        api_response = api_instance.get_invoice(org_id, entitlement_id, invoice_id)
        print("The response of BillingApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **invoice_id** | **str**| Invoice ID | 

### Return type

[**BillingInvoice**](BillingInvoice.md)

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

# **issue_invoice**
> str issue_invoice(org_id, entitlement_id, invoice_id)

issue invoice

Issue the invoice immediately. It can be used for manual issue or reissue invoice.

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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    invoice_id = 'invoice_id_example' # str | Invoice ID

    try:
        # issue invoice
        api_response = api_instance.issue_invoice(org_id, entitlement_id, invoice_id)
        print("The response of BillingApi->issue_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->issue_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **invoice_id** | **str**| Invoice ID | 

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
**200** | Empty string if issue is successful |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addons**
> List[BillingAddon] list_addons(org_id, limit=limit, offset=offset)

list addons

List all addon templates

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_addon import BillingAddon
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list addons
        api_response = api_instance.list_addons(org_id, limit=limit, offset=offset)
        print("The response of BillingApi->list_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[BillingAddon]**](BillingAddon.md)

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
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> List[BillingInvoice] list_invoices(org_id, entitlement_id=entitlement_id, buyer_id=buyer_id, status=status, limit=limit, offset=offset)

list invoices

List invoices with pagination and filter by status (optional)

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_invoice import BillingInvoice
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Optional, filter by the entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | Optional, filter by the given buyer ID (optional)
    status = 'status_example' # str | Optional, filter by invoice status as filter, if not provided, all status invoices are returned (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list invoices
        api_response = api_instance.list_invoices(org_id, entitlement_id=entitlement_id, buyer_id=buyer_id, status=status, limit=limit, offset=offset)
        print("The response of BillingApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Optional, filter by the entitlement ID | [optional] 
 **buyer_id** | **str**| Optional, filter by the given buyer ID | [optional] 
 **status** | **str**| Optional, filter by invoice status as filter, if not provided, all status invoices are returned | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[BillingInvoice]**](BillingInvoice.md)

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
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_transactions**
> List[BillingPaymentTransaction] list_payment_transactions(org_id, buyer_id=buyer_id, entitlement_id=entitlement_id, invoice_id=invoice_id, status=status, type=type, limit=limit, offset=offset)

list payment transactions

List payment transactions with pagination and filters

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_payment_transaction import BillingPaymentTransaction
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Optional, filter by the given buyer ID (optional)
    entitlement_id = 'entitlement_id_example' # str | Optional, filter by the given entitlement ID (optional)
    invoice_id = 'invoice_id_example' # str | Optional, filter by the given invoice ID (optional)
    status = 'status_example' # str | Optional, filter by status (optional)
    type = 'type_example' # str | Optional, filter by transaction type (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list payment transactions
        api_response = api_instance.list_payment_transactions(org_id, buyer_id=buyer_id, entitlement_id=entitlement_id, invoice_id=invoice_id, status=status, type=type, limit=limit, offset=offset)
        print("The response of BillingApi->list_payment_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_payment_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Optional, filter by the given buyer ID | [optional] 
 **entitlement_id** | **str**| Optional, filter by the given entitlement ID | [optional] 
 **invoice_id** | **str**| Optional, filter by the given invoice ID | [optional] 
 **status** | **str**| Optional, filter by status | [optional] 
 **type** | **str**| Optional, filter by transaction type | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[BillingPaymentTransaction]**](BillingPaymentTransaction.md)

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

# **list_refund_of_payment_transaction**
> List[BillingPaymentTransaction] list_refund_of_payment_transaction(org_id, buyer_id, payment_transaction_id)

list refunds.

list refunds of the payment transactions.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_payment_transaction import BillingPaymentTransaction
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    payment_transaction_id = 'payment_transaction_id_example' # str | Payment transaction ID

    try:
        # list refunds.
        api_response = api_instance.list_refund_of_payment_transaction(org_id, buyer_id, payment_transaction_id)
        print("The response of BillingApi->list_refund_of_payment_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_refund_of_payment_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **payment_transaction_id** | **str**| Payment transaction ID | 

### Return type

[**List[BillingPaymentTransaction]**](BillingPaymentTransaction.md)

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

# **pay_invoice**
> str pay_invoice(org_id, entitlement_id, invoice_id)

pay invoice

Initiate the payment for the invoice immediately. It can be used for manual payment or retry payment.

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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    invoice_id = 'invoice_id_example' # str | Invoice ID

    try:
        # pay invoice
        api_response = api_instance.pay_invoice(org_id, entitlement_id, invoice_id)
        print("The response of BillingApi->pay_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->pay_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **invoice_id** | **str**| Invoice ID | 

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
**200** | Empty string if pay is successful |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_addon**
> BillingAddon update_addon(org_id, addon_id, data)

update addon

Update an addon template

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_addon import BillingAddon
from suger_sdk_python.models.create_and_update_addon_params import CreateAndUpdateAddonParams
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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    addon_id = 'addon_id_example' # str | Addon ID
    data = suger_sdk_python.CreateAndUpdateAddonParams() # CreateAndUpdateAddonParams | CreateAndUpdateAddonParams

    try:
        # update addon
        api_response = api_instance.update_addon(org_id, addon_id, data)
        print("The response of BillingApi->update_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **addon_id** | **str**| Addon ID | 
 **data** | [**CreateAndUpdateAddonParams**](CreateAndUpdateAddonParams.md)| CreateAndUpdateAddonParams | 

### Return type

[**BillingAddon**](BillingAddon.md)

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
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_invoice**
> str void_invoice(org_id, entitlement_id, invoice_id)

void invoice

Void the invoice. It can be used for manual void or cancel the invoice.

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
    api_instance = suger_sdk_python.BillingApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    invoice_id = 'invoice_id_example' # str | Invoice ID

    try:
        # void invoice
        api_response = api_instance.void_invoice(org_id, entitlement_id, invoice_id)
        print("The response of BillingApi->void_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->void_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **invoice_id** | **str**| Invoice ID | 

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
**200** | Empty string if void is successful |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

