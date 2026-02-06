# suger_sdk_python.BuyerApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_credit_wallet**](BuyerApi.md#close_credit_wallet) | **PATCH** /org/{orgId}/buyer/{buyerId}/wallet/{walletId}/close | close credit wallet
[**create_buyer**](BuyerApi.md#create_buyer) | **POST** /org/{orgId}/buyer | create buyer
[**create_credit_wallet**](BuyerApi.md#create_credit_wallet) | **POST** /org/{orgId}/buyer/{buyerId}/wallet | create credit wallet
[**delete_buyer_wallet**](BuyerApi.md#delete_buyer_wallet) | **DELETE** /org/{orgId}/buyer/{buyerId}/wallet/{walletId} | delete buyer wallet
[**get_buyer**](BuyerApi.md#get_buyer) | **GET** /org/{orgId}/buyer/{buyerId} | get buyer
[**list_buyer_wallets**](BuyerApi.md#list_buyer_wallets) | **GET** /org/{orgId}/buyer/{buyerId}/wallet | list buyer&#39;s wallets
[**list_buyers**](BuyerApi.md#list_buyers) | **GET** /org/{orgId}/buyer | list buyers
[**query_buyers**](BuyerApi.md#query_buyers) | **GET** /org/{orgId}/buyer/query | query buyers
[**set_buyer_default_wallet**](BuyerApi.md#set_buyer_default_wallet) | **PATCH** /org/{orgId}/buyer/{buyerId}/wallet/{walletId}/default | set buyer default wallet
[**update_buyer**](BuyerApi.md#update_buyer) | **PATCH** /org/{orgId}/buyer/{buyerId} | update buyer
[**update_credit_wallet**](BuyerApi.md#update_credit_wallet) | **PATCH** /org/{orgId}/buyer/{buyerId}/wallet/{walletId} | update credit wallet


# **close_credit_wallet**
> BillingWallet close_credit_wallet(org_id, buyer_id, wallet_id)

close credit wallet

Close the given credit wallet, if it's a payment method, sync to payment provider too. Once closed, it can't be used for payment.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_wallet import BillingWallet
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    wallet_id = 'wallet_id_example' # str | Wallet ID

    try:
        # close credit wallet
        api_response = api_instance.close_credit_wallet(org_id, buyer_id, wallet_id)
        print("The response of BuyerApi->close_credit_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->close_credit_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **wallet_id** | **str**| Wallet ID | 

### Return type

[**BillingWallet**](BillingWallet.md)

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

# **create_buyer**
> IdentityBuyer create_buyer(org_id, data)

create buyer

create a new buyer for Stripe or Adyen under the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.create_buyer_params import CreateBuyerParams
from suger_sdk_python.models.identity_buyer import IdentityBuyer
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.CreateBuyerParams() # CreateBuyerParams | CreateBuyerParams

    try:
        # create buyer
        api_response = api_instance.create_buyer(org_id, data)
        print("The response of BuyerApi->create_buyer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->create_buyer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**CreateBuyerParams**](CreateBuyerParams.md)| CreateBuyerParams | 

### Return type

[**IdentityBuyer**](IdentityBuyer.md)

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

# **create_credit_wallet**
> BillingWallet create_credit_wallet(org_id, buyer_id)

create credit wallet

create a new credit wallet for the buyer.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_wallet import BillingWallet
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID

    try:
        # create credit wallet
        api_response = api_instance.create_credit_wallet(org_id, buyer_id)
        print("The response of BuyerApi->create_credit_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->create_credit_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 

### Return type

[**BillingWallet**](BillingWallet.md)

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

# **delete_buyer_wallet**
> str delete_buyer_wallet(org_id, buyer_id, wallet_id)

delete buyer wallet

delete a wallet of the buyer, if it's a payment method, sync to payment provider too.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    wallet_id = 'wallet_id_example' # str | Wallet ID

    try:
        # delete buyer wallet
        api_response = api_instance.delete_buyer_wallet(org_id, buyer_id, wallet_id)
        print("The response of BuyerApi->delete_buyer_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->delete_buyer_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **wallet_id** | **str**| Wallet ID | 

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

# **get_buyer**
> IdentityBuyer get_buyer(org_id, buyer_id)

get buyer

get buyer by the given organization and buyer id.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_buyer import IdentityBuyer
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID

    try:
        # get buyer
        api_response = api_instance.get_buyer(org_id, buyer_id)
        print("The response of BuyerApi->get_buyer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->get_buyer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 

### Return type

[**IdentityBuyer**](IdentityBuyer.md)

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
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_wallets**
> List[BillingWallet] list_buyer_wallets(org_id, buyer_id)

list buyer's wallets

list all wallets of a buyer.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_wallet import BillingWallet
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID

    try:
        # list buyer's wallets
        api_response = api_instance.list_buyer_wallets(org_id, buyer_id)
        print("The response of BuyerApi->list_buyer_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->list_buyer_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 

### Return type

[**List[BillingWallet]**](BillingWallet.md)

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

# **list_buyers**
> List[IdentityBuyer] list_buyers(org_id, partner=partner, email_domain=email_domain, aws_account_id=aws_account_id, limit=limit, offset=offset)

list buyers

list buyers by the given organization with pagination and optional filters.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_buyer import IdentityBuyer
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | filter by partner (optional)
    email_domain = 'email_domain_example' # str | filter by email domain (optional)
    aws_account_id = 'aws_account_id_example' # str | filter by awsAccountId (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list buyers
        api_response = api_instance.list_buyers(org_id, partner=partner, email_domain=email_domain, aws_account_id=aws_account_id, limit=limit, offset=offset)
        print("The response of BuyerApi->list_buyers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->list_buyers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| filter by partner | [optional] 
 **email_domain** | **str**| filter by email domain | [optional] 
 **aws_account_id** | **str**| filter by awsAccountId | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[IdentityBuyer]**](IdentityBuyer.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_buyers**
> GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityBuyer query_buyers(org_id, page_size=page_size, page_number=page_number, q=q, s=s)

query buyers

Query buyers with advanced filtering, sorting, and pagination using CRUD query language. Supports complex filters, sorting by multiple fields, and pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_crud_list_base_response_github_com_sugerio_marketplace_service_pkg_orm_identity_buyer import GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityBuyer
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    page_size = 56 # int | Number of items per page (default 20, max 1000) (optional)
    page_number = 56 # int | Page number (default 1) (optional)
    q = 'q_example' # str | LISP-style filter expression (e.g., '(= partner \\ (optional)
    s = 's_example' # str | Sort fields: 'field:asc,field2:desc' or '-field,field2' format (e.g., 'creation_time:desc,name:asc' or '-creation_time,name') (optional)

    try:
        # query buyers
        api_response = api_instance.query_buyers(org_id, page_size=page_size, page_number=page_number, q=q, s=s)
        print("The response of BuyerApi->query_buyers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->query_buyers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **page_size** | **int**| Number of items per page (default 20, max 1000) | [optional] 
 **page_number** | **int**| Page number (default 1) | [optional] 
 **q** | **str**| LISP-style filter expression (e.g., &#39;(&#x3D; partner \\ | [optional] 
 **s** | **str**| Sort fields: &#39;field:asc,field2:desc&#39; or &#39;-field,field2&#39; format (e.g., &#39;creation_time:desc,name:asc&#39; or &#39;-creation_time,name&#39;) | [optional] 

### Return type

[**GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityBuyer**](GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityBuyer.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of buyers |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_buyer_default_wallet**
> IdentityBuyer set_buyer_default_wallet(org_id, buyer_id, wallet_id)

set buyer default wallet

set a payment method wallet as buyer's default wallet.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_buyer import IdentityBuyer
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    wallet_id = 'wallet_id_example' # str | Wallet ID

    try:
        # set buyer default wallet
        api_response = api_instance.set_buyer_default_wallet(org_id, buyer_id, wallet_id)
        print("The response of BuyerApi->set_buyer_default_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->set_buyer_default_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **wallet_id** | **str**| Wallet ID | 

### Return type

[**IdentityBuyer**](IdentityBuyer.md)

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

# **update_buyer**
> IdentityBuyer update_buyer(org_id, buyer_id, data)

update buyer

update buyer by the given organization and buyer id.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_buyer import IdentityBuyer
from suger_sdk_python.models.update_buyer_params import UpdateBuyerParams
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    data = suger_sdk_python.UpdateBuyerParams() # UpdateBuyerParams | UpdateBuyerParams

    try:
        # update buyer
        api_response = api_instance.update_buyer(org_id, buyer_id, data)
        print("The response of BuyerApi->update_buyer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->update_buyer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **data** | [**UpdateBuyerParams**](UpdateBuyerParams.md)| UpdateBuyerParams | 

### Return type

[**IdentityBuyer**](IdentityBuyer.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_wallet**
> BillingWallet update_credit_wallet(org_id, buyer_id, wallet_id)

update credit wallet

update startTime or expireTime of the wallet.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billing_wallet import BillingWallet
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
    api_instance = suger_sdk_python.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    wallet_id = 'wallet_id_example' # str | Wallet ID

    try:
        # update credit wallet
        api_response = api_instance.update_credit_wallet(org_id, buyer_id, wallet_id)
        print("The response of BuyerApi->update_credit_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->update_credit_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **wallet_id** | **str**| Wallet ID | 

### Return type

[**BillingWallet**](BillingWallet.md)

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

