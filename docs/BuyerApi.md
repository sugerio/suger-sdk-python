# openapi_client.BuyerApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buyer**](BuyerApi.md#get_buyer) | **GET** /org/{orgId}/buyer/{buyerId} | get buyer
[**list_buyers_by_contact**](BuyerApi.md#list_buyers_by_contact) | **GET** /org/{orgId}/contact/{contactId}/buyer | list buyers by contact
[**list_buyers_by_organization**](BuyerApi.md#list_buyers_by_organization) | **GET** /org/{orgId}/buyer | list buyers by organization
[**list_buyers_by_partner**](BuyerApi.md#list_buyers_by_partner) | **GET** /org/{orgId}/partner/{partner}/buyer | list buyers by partner
[**update_buyer**](BuyerApi.md#update_buyer) | **PATCH** /org/{orgId}/buyer/{buyerId} | update buyer


# **get_buyer**
> IdentityBuyer get_buyer(org_id, buyer_id)

get buyer

get buyer by the given organization and buyer id

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_buyer import IdentityBuyer
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
    api_instance = openapi_client.BuyerApi(api_client)
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

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

# **list_buyers_by_contact**
> List[IdentityBuyer] list_buyers_by_contact(org_id, contact_id)

list buyers by contact

list all buyers by the given organization and contact

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_buyer import IdentityBuyer
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
    api_instance = openapi_client.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID

    try:
        # list buyers by contact
        api_response = api_instance.list_buyers_by_contact(org_id, contact_id)
        print("The response of BuyerApi->list_buyers_by_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->list_buyers_by_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 

### Return type

[**List[IdentityBuyer]**](IdentityBuyer.md)

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

# **list_buyers_by_organization**
> List[IdentityBuyer] list_buyers_by_organization(org_id)

list buyers by organization

list all buyers by the given organization

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_buyer import IdentityBuyer
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
    api_instance = openapi_client.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # list buyers by organization
        api_response = api_instance.list_buyers_by_organization(org_id)
        print("The response of BuyerApi->list_buyers_by_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->list_buyers_by_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[IdentityBuyer]**](IdentityBuyer.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyers_by_partner**
> List[IdentityBuyer] list_buyers_by_partner(org_id, partner)

list buyers by partner

list all buyers by the given organization and partner

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_buyer import IdentityBuyer
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
    api_instance = openapi_client.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner

    try:
        # list buyers by partner
        api_response = api_instance.list_buyers_by_partner(org_id, partner)
        print("The response of BuyerApi->list_buyers_by_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerApi->list_buyers_by_partner: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 

### Return type

[**List[IdentityBuyer]**](IdentityBuyer.md)

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

# **update_buyer**
> IdentityBuyer update_buyer(org_id, buyer_id, data)

update buyer

update buyer by the given organization and buyer id

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_buyer import IdentityBuyer
from openapi_client.models.update_buyer_params import UpdateBuyerParams
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
    api_instance = openapi_client.BuyerApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    data = openapi_client.UpdateBuyerParams() # UpdateBuyerParams | UpdateBuyerParams

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

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

