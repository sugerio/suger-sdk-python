# openapi_client.ContactApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact_to_buyer**](ContactApi.md#add_contact_to_buyer) | **POST** /org/{orgId}/contact/{contactId}/buyer/{buyerId} | add contact to buyer
[**add_contact_to_offer**](ContactApi.md#add_contact_to_offer) | **POST** /org/{orgId}/contact/{contactId}/offer/{offerId} | add contact to offer
[**create_contact**](ContactApi.md#create_contact) | **POST** /org/{orgId}/contact | create contact
[**get_contact**](ContactApi.md#get_contact) | **GET** /org/{orgId}/contact/{contactId} | get contact
[**list_contacts_by_organization**](ContactApi.md#list_contacts_by_organization) | **GET** /org/{orgId}/contact | list contacts by organization
[**remove_contact_from_buyer**](ContactApi.md#remove_contact_from_buyer) | **DELETE** /org/{orgId}/contact/{contactId}/buyer/{buyerId} | remove contact from buyer
[**remove_contact_from_offer**](ContactApi.md#remove_contact_from_offer) | **DELETE** /org/{orgId}/contact/{contactId}/offer/{offerId} | remove contact from offer
[**update_contact**](ContactApi.md#update_contact) | **PATCH** /org/{orgId}/contact/{contactId} | update contact


# **add_contact_to_buyer**
> str add_contact_to_buyer(org_id, buyer_id, contact_id)

add contact to buyer

add contact to buyer by the given organization, buyer id and contact id.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    contact_id = 'contact_id_example' # str | Contact ID

    try:
        # add contact to buyer
        api_response = api_instance.add_contact_to_buyer(org_id, buyer_id, contact_id)
        print("The response of ContactApi->add_contact_to_buyer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->add_contact_to_buyer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **contact_id** | **str**| Contact ID | 

### Return type

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | empty string if success |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_contact_to_offer**
> str add_contact_to_offer(org_id, contact_id, offer_id)

add contact to offer

add contact to offer by the given organization, offer id and contact id.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # add contact to offer
        api_response = api_instance.add_contact_to_offer(org_id, contact_id, offer_id)
        print("The response of ContactApi->add_contact_to_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->add_contact_to_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 
 **offer_id** | **str**| Offer ID | 

### Return type

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | empty string if success |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> IdentityContact create_contact(org_id, data)

create contact

Create a contact under the given organization. If the email address already exists, return the existing contact.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_contact import IdentityContact
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = openapi_client.IdentityContact() # IdentityContact | RequestBody

    try:
        # create contact
        api_response = api_instance.create_contact(org_id, data)
        print("The response of ContactApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->create_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**IdentityContact**](IdentityContact.md)| RequestBody | 

### Return type

[**IdentityContact**](IdentityContact.md)

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

# **get_contact**
> IdentityContact get_contact(org_id, contact_id)

get contact

Get the Contact by the given contact ID.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_contact import IdentityContact
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID

    try:
        # get contact
        api_response = api_instance.get_contact(org_id, contact_id)
        print("The response of ContactApi->get_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 

### Return type

[**IdentityContact**](IdentityContact.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Contact Object |  -  |
**400** | Bad request error description |  -  |
**500** | internal error description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts_by_organization**
> List[IdentityContact] list_contacts_by_organization(org_id)

list contacts by organization

List all contacts under the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_contact import IdentityContact
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # list contacts by organization
        api_response = api_instance.list_contacts_by_organization(org_id)
        print("The response of ContactApi->list_contacts_by_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->list_contacts_by_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[IdentityContact]**](IdentityContact.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error description |  -  |
**500** | internal error description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contact_from_buyer**
> str remove_contact_from_buyer(org_id, buyer_id, contact_id)

remove contact from buyer

remove contact from buyer by the given organization, buyer id and contact id.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    buyer_id = 'buyer_id_example' # str | Buyer ID
    contact_id = 'contact_id_example' # str | Contact ID

    try:
        # remove contact from buyer
        api_response = api_instance.remove_contact_from_buyer(org_id, buyer_id, contact_id)
        print("The response of ContactApi->remove_contact_from_buyer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->remove_contact_from_buyer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **buyer_id** | **str**| Buyer ID | 
 **contact_id** | **str**| Contact ID | 

### Return type

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | empty string if success |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contact_from_offer**
> str remove_contact_from_offer(org_id, contact_id, offer_id)

remove contact from offer

remove contact from offer by the given organization, offer id and contact id.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # remove contact from offer
        api_response = api_instance.remove_contact_from_offer(org_id, contact_id, offer_id)
        print("The response of ContactApi->remove_contact_from_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->remove_contact_from_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 
 **offer_id** | **str**| Offer ID | 

### Return type

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | empty string if success |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> IdentityContact update_contact(org_id, contact_id, data)

update contact

update contact by the given organization and buyer id. The given name and information should be complete. Please note that this function does not support partial updates.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.identity_contact import IdentityContact
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
    api_instance = openapi_client.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID
    data = openapi_client.IdentityContact() # IdentityContact | Request Body

    try:
        # update contact
        api_response = api_instance.update_contact(org_id, contact_id, data)
        print("The response of ContactApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->update_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 
 **data** | [**IdentityContact**](IdentityContact.md)| Request Body | 

### Return type

[**IdentityContact**](IdentityContact.md)

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

