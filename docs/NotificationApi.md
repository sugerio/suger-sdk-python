# suger_sdk_python.NotificationApi

All URIs are relative to *http://https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notification_message**](NotificationApi.md#get_notification_message) | **GET** /org/{orgId}/notificationMessage/{notificationMessageId} | get notification message
[**list_notification_events**](NotificationApi.md#list_notification_events) | **GET** /org/{orgId}/notificationEvent | list notification events
[**list_notification_events_by_entity**](NotificationApi.md#list_notification_events_by_entity) | **GET** /org/{orgId}/notificationEvent/{entityType}/{entityId} | list notification events by entity
[**list_notification_messages**](NotificationApi.md#list_notification_messages) | **GET** /org/{orgId}/notificationMessage | list notification messages


# **get_notification_message**
> NotificationMessage get_notification_message(org_id, notification_message_id)

get notification message

Get the notification message of the organization & notification message ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.notification_message import NotificationMessage
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
    api_instance = suger_sdk_python.NotificationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    notification_message_id = 'notification_message_id_example' # str | Notification Message ID

    try:
        # get notification message
        api_response = api_instance.get_notification_message(org_id, notification_message_id)
        print("The response of NotificationApi->get_notification_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->get_notification_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **notification_message_id** | **str**| Notification Message ID | 

### Return type

[**NotificationMessage**](NotificationMessage.md)

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

# **list_notification_events**
> ListNotificationEventsResponse list_notification_events(org_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset, priorities=priorities)

list notification events

List the notification events of the given organization with pagination and optional filters.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_notification_events_response import ListNotificationEventsResponse
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
    api_instance = suger_sdk_python.NotificationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)
    priorities = 'priorities_example' # str | Filter by priorities, empty means HIGH and CRITICAL only. Valid values are: LOW, MEDIUM, HIGH, CRITICAL. Multiple values are supported, separated by comma. (optional)

    try:
        # list notification events
        api_response = api_instance.list_notification_events(org_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset, priorities=priorities)
        print("The response of NotificationApi->list_notification_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->list_notification_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 
 **priorities** | **str**| Filter by priorities, empty means HIGH and CRITICAL only. Valid values are: LOW, MEDIUM, HIGH, CRITICAL. Multiple values are supported, separated by comma. | [optional] 

### Return type

[**ListNotificationEventsResponse**](ListNotificationEventsResponse.md)

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

# **list_notification_events_by_entity**
> ListNotificationEventsResponse list_notification_events_by_entity(org_id, entity_type, entity_id, limit=limit, offset=offset)

list notification events by entity

List the notification events of the given organization and entity with pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_notification_events_response import ListNotificationEventsResponse
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
    api_instance = suger_sdk_python.NotificationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entity_type = 'entity_type_example' # str | Entity type, valid values are: PRODUCT, OFFER, ENTITLEMENT, INTEGRATION etc.
    entity_id = 'entity_id_example' # str | Entity ID
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list notification events by entity
        api_response = api_instance.list_notification_events_by_entity(org_id, entity_type, entity_id, limit=limit, offset=offset)
        print("The response of NotificationApi->list_notification_events_by_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->list_notification_events_by_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entity_type** | **str**| Entity type, valid values are: PRODUCT, OFFER, ENTITLEMENT, INTEGRATION etc. | 
 **entity_id** | **str**| Entity ID | 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListNotificationEventsResponse**](ListNotificationEventsResponse.md)

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

# **list_notification_messages**
> ListNotificationMessagesResponse list_notification_messages(org_id, limit=limit, offset=offset)

list notification messages

List the notification messages of the given organization with pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_notification_messages_response import ListNotificationMessagesResponse
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
    api_instance = suger_sdk_python.NotificationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list notification messages
        api_response = api_instance.list_notification_messages(org_id, limit=limit, offset=offset)
        print("The response of NotificationApi->list_notification_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->list_notification_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListNotificationMessagesResponse**](ListNotificationMessagesResponse.md)

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

