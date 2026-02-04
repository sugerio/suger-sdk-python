# suger_sdk_python.SupportApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_support_ticket**](SupportApi.md#close_support_ticket) | **PATCH** /org/{orgId}/support/ticket/{ticketId}/close | close support ticket
[**create_support_ticket**](SupportApi.md#create_support_ticket) | **POST** /org/{orgId}/support/ticket | create support ticket
[**create_support_ticket_attachment**](SupportApi.md#create_support_ticket_attachment) | **POST** /org/{orgId}/support/ticket/{ticketId}/attachment | create support ticket attachment
[**create_support_ticket_comment**](SupportApi.md#create_support_ticket_comment) | **POST** /org/{orgId}/support/ticket/{ticketId}/comment | create support ticket comment
[**get_support_ticket**](SupportApi.md#get_support_ticket) | **GET** /org/{orgId}/support/ticket/{ticketId} | get support ticket
[**list_support_tickets**](SupportApi.md#list_support_tickets) | **GET** /org/{orgId}/support/ticket | list support tickets
[**reopen_support_ticket**](SupportApi.md#reopen_support_ticket) | **PATCH** /org/{orgId}/support/ticket/{ticketId}/reopen | reopen support ticket
[**update_support_ticket**](SupportApi.md#update_support_ticket) | **PATCH** /org/{orgId}/support/ticket/{ticketId} | update support ticket


# **close_support_ticket**
> SupportTicket close_support_ticket(org_id, ticket_id)

close support ticket

close suuport ticket

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket import SupportTicket
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    ticket_id = 'ticket_id_example' # str | Ticket ID

    try:
        # close support ticket
        api_response = api_instance.close_support_ticket(org_id, ticket_id)
        print("The response of SupportApi->close_support_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->close_support_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **ticket_id** | **str**| Ticket ID | 

### Return type

[**SupportTicket**](SupportTicket.md)

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

# **create_support_ticket**
> SupportTicket create_support_ticket(org_id, body)

create support ticket

create support ticket

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket import SupportTicket
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    body = suger_sdk_python.SupportTicket() # SupportTicket | Ticket create request

    try:
        # create support ticket
        api_response = api_instance.create_support_ticket(org_id, body)
        print("The response of SupportApi->create_support_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->create_support_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **body** | [**SupportTicket**](SupportTicket.md)| Ticket create request | 

### Return type

[**SupportTicket**](SupportTicket.md)

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

# **create_support_ticket_attachment**
> List[SupportTicketAttachment] create_support_ticket_attachment(org_id, ticket_id, file)

create support ticket attachment

create support ticket attachment

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket_attachment import SupportTicketAttachment
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    ticket_id = 'ticket_id_example' # str | Ticket ID
    file = None # bytearray | File to upload

    try:
        # create support ticket attachment
        api_response = api_instance.create_support_ticket_attachment(org_id, ticket_id, file)
        print("The response of SupportApi->create_support_ticket_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->create_support_ticket_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **ticket_id** | **str**| Ticket ID | 
 **file** | **bytearray**| File to upload | 

### Return type

[**List[SupportTicketAttachment]**](SupportTicketAttachment.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_support_ticket_comment**
> SupportTicketComment create_support_ticket_comment(org_id, ticket_id, body)

create support ticket comment

create support ticket comment

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket_comment import SupportTicketComment
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    ticket_id = 'ticket_id_example' # str | Ticket ID
    body = suger_sdk_python.SupportTicketComment() # SupportTicketComment | Ticket create request

    try:
        # create support ticket comment
        api_response = api_instance.create_support_ticket_comment(org_id, ticket_id, body)
        print("The response of SupportApi->create_support_ticket_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->create_support_ticket_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **ticket_id** | **str**| Ticket ID | 
 **body** | [**SupportTicketComment**](SupportTicketComment.md)| Ticket create request | 

### Return type

[**SupportTicketComment**](SupportTicketComment.md)

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

# **get_support_ticket**
> SupportTicket get_support_ticket(org_id, ticket_id)

get support ticket

get support ticket

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket import SupportTicket
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    ticket_id = 'ticket_id_example' # str | Ticket ID

    try:
        # get support ticket
        api_response = api_instance.get_support_ticket(org_id, ticket_id)
        print("The response of SupportApi->get_support_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->get_support_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **ticket_id** | **str**| Ticket ID | 

### Return type

[**SupportTicket**](SupportTicket.md)

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

# **list_support_tickets**
> ListSupportTicketsResponse list_support_tickets(org_id, limit=limit, offset=offset)

list support tickets

list support tickets

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_support_tickets_response import ListSupportTicketsResponse
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list support tickets
        api_response = api_instance.list_support_tickets(org_id, limit=limit, offset=offset)
        print("The response of SupportApi->list_support_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->list_support_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListSupportTicketsResponse**](ListSupportTicketsResponse.md)

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

# **reopen_support_ticket**
> SupportTicket reopen_support_ticket(org_id, ticket_id)

reopen support ticket

reopen support ticket

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket import SupportTicket
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    ticket_id = 'ticket_id_example' # str | Ticket ID

    try:
        # reopen support ticket
        api_response = api_instance.reopen_support_ticket(org_id, ticket_id)
        print("The response of SupportApi->reopen_support_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->reopen_support_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **ticket_id** | **str**| Ticket ID | 

### Return type

[**SupportTicket**](SupportTicket.md)

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

# **update_support_ticket**
> SupportTicket update_support_ticket(org_id, ticket_id, body)

update support ticket

update support ticket

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.support_ticket import SupportTicket
from suger_sdk_python.models.update_support_ticket_request import UpdateSupportTicketRequest
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
    api_instance = suger_sdk_python.SupportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    ticket_id = 'ticket_id_example' # str | Ticket ID
    body = suger_sdk_python.UpdateSupportTicketRequest() # UpdateSupportTicketRequest | Ticket create request

    try:
        # update support ticket
        api_response = api_instance.update_support_ticket(org_id, ticket_id, body)
        print("The response of SupportApi->update_support_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->update_support_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **ticket_id** | **str**| Ticket ID | 
 **body** | [**UpdateSupportTicketRequest**](UpdateSupportTicketRequest.md)| Ticket create request | 

### Return type

[**SupportTicket**](SupportTicket.md)

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

