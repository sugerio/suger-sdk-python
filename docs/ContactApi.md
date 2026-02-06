# suger_sdk_python.ContactApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact_to_buyer**](ContactApi.md#add_contact_to_buyer) | **POST** /org/{orgId}/contact/{contactId}/buyer/{buyerId} | add contact to buyer
[**add_contact_to_offer**](ContactApi.md#add_contact_to_offer) | **POST** /org/{orgId}/contact/{contactId}/offer/{offerId} | add contact to offer
[**batch_create_contacts**](ContactApi.md#batch_create_contacts) | **POST** /org/{orgId}/contact/batch | batch create contacts
[**create_contact**](ContactApi.md#create_contact) | **POST** /org/{orgId}/contact | create contact
[**get_contact**](ContactApi.md#get_contact) | **GET** /org/{orgId}/contact/{contactId} | get contact
[**list_contacts**](ContactApi.md#list_contacts) | **GET** /org/{orgId}/contact | list contacts
[**query_contacts**](ContactApi.md#query_contacts) | **GET** /org/{orgId}/contact/query | query contacts
[**remove_contact_from_buyer**](ContactApi.md#remove_contact_from_buyer) | **DELETE** /org/{orgId}/contact/{contactId}/buyer/{buyerId} | remove contact from buyer
[**remove_contact_from_offer**](ContactApi.md#remove_contact_from_offer) | **DELETE** /org/{orgId}/contact/{contactId}/offer/{offerId} | remove contact from offer
[**update_contact**](ContactApi.md#update_contact) | **PATCH** /org/{orgId}/contact/{contactId} | update contact
[**update_contact_tags**](ContactApi.md#update_contact_tags) | **PATCH** /org/{orgId}/contact/{contactId}/tag | update contact tags


# **add_contact_to_buyer**
> IdentityBuyer add_contact_to_buyer(org_id, buyer_id, contact_id)

add contact to buyer

add contact to buyer by the given organization, buyer id and contact id.

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
    api_instance = suger_sdk_python.ContactApi(api_client)
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

# **add_contact_to_offer**
> str add_contact_to_offer(org_id, contact_id, offer_id)

add contact to offer

add contact to offer by the given organization, offer id and contact id.

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
    api_instance = suger_sdk_python.ContactApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **batch_create_contacts**
> List[List[IdentityContact]] batch_create_contacts(org_id, data)

batch create contacts

Create multiple contacts under the given organization. If an email address already exists, return the existing contact.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_contact import IdentityContact
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
    api_instance = suger_sdk_python.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = [suger_sdk_python.IdentityContact()] # List[IdentityContact] | RequestBody

    try:
        # batch create contacts
        api_response = api_instance.batch_create_contacts(org_id, data)
        print("The response of ContactApi->batch_create_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->batch_create_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**List[IdentityContact]**](IdentityContact.md)| RequestBody | 

### Return type

**List[List[IdentityContact]]**

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

# **create_contact**
> IdentityContact create_contact(org_id, data)

create contact

Create a contact under the given organization. If the email address already exists, return the existing contact.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_contact import IdentityContact
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
    api_instance = suger_sdk_python.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.IdentityContact() # IdentityContact | RequestBody

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

# **get_contact**
> IdentityContact get_contact(org_id, contact_id)

get contact

Get the Contact by the given contact ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_contact import IdentityContact
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
    api_instance = suger_sdk_python.ContactApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **list_contacts**
> List[IdentityContact] list_contacts(org_id, contact_ids=contact_ids, email_domain=email_domain, keyword=keyword, limit=limit, offset=offset)

list contacts

List all contacts under the given organization. If contactIds parameter is provided, return only those specific contacts.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_contact import IdentityContact
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
    api_instance = suger_sdk_python.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_ids = 'contact_ids_example' # str | Comma-separated list of contact IDs to fetch specific contacts, up to 100 IDs (optional)
    email_domain = 'email_domain_example' # str | Email domain to filter contacts (optional)
    keyword = 'keyword_example' # str | the keyword string to search contacts by name or email (uses ORM for better performance) (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (ignored when contactIds is provided) (optional)
    offset = 56 # int | List pagination offset, default 0 (ignored when contactIds is provided) (optional)

    try:
        # list contacts
        api_response = api_instance.list_contacts(org_id, contact_ids=contact_ids, email_domain=email_domain, keyword=keyword, limit=limit, offset=offset)
        print("The response of ContactApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->list_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_ids** | **str**| Comma-separated list of contact IDs to fetch specific contacts, up to 100 IDs | [optional] 
 **email_domain** | **str**| Email domain to filter contacts | [optional] 
 **keyword** | **str**| the keyword string to search contacts by name or email (uses ORM for better performance) | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 (ignored when contactIds is provided) | [optional] 
 **offset** | **int**| List pagination offset, default 0 (ignored when contactIds is provided) | [optional] 

### Return type

[**List[IdentityContact]**](IdentityContact.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **query_contacts**
> GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityContact query_contacts(org_id, page_size=page_size, page_number=page_number, q=q, s=s)

query contacts

Query contacts with advanced filtering, sorting, and pagination using CRUD query language. Supports complex filters, sorting by multiple fields, and pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_crud_list_base_response_github_com_sugerio_marketplace_service_pkg_orm_identity_contact import GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityContact
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
    api_instance = suger_sdk_python.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    page_size = 56 # int | Number of items per page (default 20, max 1000) (optional)
    page_number = 56 # int | Page number (default 1) (optional)
    q = 'q_example' # str | LISP-style filter expression (e.g., '(= name \\ (optional)
    s = 's_example' # str | Sort fields: 'field:asc,field2:desc' or '-field,field2' format (e.g., 'creation_time:desc,name:asc' or '-creation_time,name') (optional)

    try:
        # query contacts
        api_response = api_instance.query_contacts(org_id, page_size=page_size, page_number=page_number, q=q, s=s)
        print("The response of ContactApi->query_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->query_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **page_size** | **int**| Number of items per page (default 20, max 1000) | [optional] 
 **page_number** | **int**| Page number (default 1) | [optional] 
 **q** | **str**| LISP-style filter expression (e.g., &#39;(&#x3D; name \\ | [optional] 
 **s** | **str**| Sort fields: &#39;field:asc,field2:desc&#39; or &#39;-field,field2&#39; format (e.g., &#39;creation_time:desc,name:asc&#39; or &#39;-creation_time,name&#39;) | [optional] 

### Return type

[**GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityContact**](GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmIdentityContact.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of contacts |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contact_from_buyer**
> str remove_contact_from_buyer(org_id, buyer_id, contact_id)

remove contact from buyer

remove contact from buyer by the given organization, buyer id and contact id.

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
    api_instance = suger_sdk_python.ContactApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

remove contact from offer by given organization, offer id and contact id.

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
    api_instance = suger_sdk_python.ContactApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

Update the contact for the given organization and contact ID. This endpoint supports partial updates. Only the fields provided in the request body will be updated. To clear a field, provide it with an empty value.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.identity_contact import IdentityContact
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
    api_instance = suger_sdk_python.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID
    data = suger_sdk_python.IdentityContact() # IdentityContact | Request Body

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

# **update_contact_tags**
> List[str] update_contact_tags(org_id, contact_id, data)

update contact tags

Update the tags for a contact. Tags must be alphabetic strings, max 10 characters each, max 5 tags total.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.service_marketplace_service_api_update_contact_tags_request import ServiceMarketplaceServiceApiUpdateContactTagsRequest
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
    api_instance = suger_sdk_python.ContactApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID
    data = suger_sdk_python.ServiceMarketplaceServiceApiUpdateContactTagsRequest() # ServiceMarketplaceServiceApiUpdateContactTagsRequest | Request Body

    try:
        # update contact tags
        api_response = api_instance.update_contact_tags(org_id, contact_id, data)
        print("The response of ContactApi->update_contact_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->update_contact_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 
 **data** | [**ServiceMarketplaceServiceApiUpdateContactTagsRequest**](ServiceMarketplaceServiceApiUpdateContactTagsRequest.md)| Request Body | 

### Return type

**List[str]**

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully validated and updated tags |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

