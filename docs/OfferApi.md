# suger_sdk_python.OfferApi

All URIs are relative to *http://https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_offer**](OfferApi.md#cancel_offer) | **POST** /org/{orgId}/offer/{offerId}/cancel | cancel offer
[**create_offer**](OfferApi.md#create_offer) | **POST** /org/{orgId}/offer | create offer
[**create_or_update_draft_offer**](OfferApi.md#create_or_update_draft_offer) | **POST** /org/{orgId}/draftOffer | create or update draft offer
[**delete_offer**](OfferApi.md#delete_offer) | **DELETE** /org/{orgId}/offer/{offerId} | delete offer
[**extend_private_offer_expiry_date**](OfferApi.md#extend_private_offer_expiry_date) | **POST** /org/{orgId}/offer/{offerId}/extendExpiryDate | extend offer expiry date
[**get_offer**](OfferApi.md#get_offer) | **GET** /org/{orgId}/offer/{offerId} | get offer
[**get_offer_by_external_id**](OfferApi.md#get_offer_by_external_id) | **GET** /org/{orgId}/offerExternalId/{offerExternalId} | get offer by external ID
[**get_offer_eula**](OfferApi.md#get_offer_eula) | **GET** /org/{orgId}/offer/{offerId}/eula | get offer EULA
[**get_offer_reseller_eula**](OfferApi.md#get_offer_reseller_eula) | **GET** /org/{orgId}/offer/{offerId}/resellerEula | get offer reseller EULA
[**list_offers**](OfferApi.md#list_offers) | **GET** /org/{orgId}/offer | list offers
[**send_offer_notifications**](OfferApi.md#send_offer_notifications) | **POST** /org/{orgId}/offer/{offerId}/notifyContacts | notify offer contacts
[**update_offer_meta_info**](OfferApi.md#update_offer_meta_info) | **PATCH** /org/{orgId}/offer/{offerId}/metaInfo | update offer meta info


# **cancel_offer**
> WorkloadOffer cancel_offer(org_id, offer_id)

cancel offer

Only the offer with status = "PENDING_ACCEPTANCE", "PENDING_CANCEL", "ACTIVE" or "USED" is allowed to cancel.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # cancel offer
        api_response = api_instance.cancel_offer(org_id, offer_id)
        print("The response of OfferApi->cancel_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->cancel_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 

### Return type

[**WorkloadOffer**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_offer**
> WorkloadOffer create_offer(org_id, data)

create offer

Create a private offer under the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.WorkloadOffer() # WorkloadOffer | Offer to create

    try:
        # create offer
        api_response = api_instance.create_offer(org_id, data)
        print("The response of OfferApi->create_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->create_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**WorkloadOffer**](WorkloadOffer.md)| Offer to create | 

### Return type

[**WorkloadOffer**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_draft_offer**
> WorkloadOffer create_or_update_draft_offer(org_id, data)

create or update draft offer

Create a new draft offer or update the existing draft offer. When updating draft offer, the offer.ID is required.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.WorkloadOffer() # WorkloadOffer | the draft offer to create

    try:
        # create or update draft offer
        api_response = api_instance.create_or_update_draft_offer(org_id, data)
        print("The response of OfferApi->create_or_update_draft_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->create_or_update_draft_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**WorkloadOffer**](WorkloadOffer.md)| the draft offer to create | 

### Return type

[**WorkloadOffer**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_offer**
> str delete_offer(org_id, offer_id)

delete offer

The offer is soft deleted (marked as DELETED status) in Suger service. Only the offer with status = "DRAFT", "CREATE_FAILED", "EXPIRED" or "CANCELLED" is allowed to be deleted.

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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # delete offer
        api_response = api_instance.delete_offer(org_id, offer_id)
        print("The response of OfferApi->delete_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->delete_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
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
**200** | Empty string if deletion is successful |  -  |
**400** | Bad request error |  -  |
**404** | Not found error |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_private_offer_expiry_date**
> WorkloadOffer extend_private_offer_expiry_date(org_id, offer_id, new_expiry_date)

extend offer expiry date

Only the offer with status = "PENDING_ACCEPTANCE", "EXPIRED" or "ACCEPTED" is allowed to extend expiry date.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID
    new_expiry_date = 'new_expiry_date_example' # str | new expiry date in YYYY-MM-DD format

    try:
        # extend offer expiry date
        api_response = api_instance.extend_private_offer_expiry_date(org_id, offer_id, new_expiry_date)
        print("The response of OfferApi->extend_private_offer_expiry_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->extend_private_offer_expiry_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 
 **new_expiry_date** | **str**| new expiry date in YYYY-MM-DD format | 

### Return type

[**WorkloadOffer**](WorkloadOffer.md)

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
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer**
> WorkloadOffer get_offer(org_id, offer_id)

get offer

Get the offer by the given offer ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # get offer
        api_response = api_instance.get_offer(org_id, offer_id)
        print("The response of OfferApi->get_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 

### Return type

[**WorkloadOffer**](WorkloadOffer.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Offer Object |  -  |
**400** | Bad request error |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_by_external_id**
> WorkloadOffer get_offer_by_external_id(org_id, offer_external_id)

get offer by external ID

Get the offer by the given offer external ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_external_id = 'offer_external_id_example' # str | Offer External ID

    try:
        # get offer by external ID
        api_response = api_instance.get_offer_by_external_id(org_id, offer_external_id)
        print("The response of OfferApi->get_offer_by_external_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_offer_by_external_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_external_id** | **str**| Offer External ID | 

### Return type

[**WorkloadOffer**](WorkloadOffer.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Offer Object |  -  |
**400** | Bad request error |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_eula**
> str get_offer_eula(org_id, offer_id, format=format)

get offer EULA

Get the EULA file of the given offer ID.

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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID
    format = 'format_example' # str | response format in JSON or string (optional)

    try:
        # get offer EULA
        api_response = api_instance.get_offer_eula(org_id, offer_id, format=format)
        print("The response of OfferApi->get_offer_eula:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_offer_eula: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 
 **format** | **str**| response format in JSON or string | [optional] 

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
**200** | AWS S3 signed URL with 30 minutes expiry time |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_reseller_eula**
> str get_offer_reseller_eula(org_id, offer_id)

get offer reseller EULA

Get the Reseller EULA file of the given offer ID.

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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # get offer reseller EULA
        api_response = api_instance.get_offer_reseller_eula(org_id, offer_id)
        print("The response of OfferApi->get_offer_reseller_eula:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->get_offer_reseller_eula: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
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
**200** | AWS S3 signed URL with 30 minutes expiry time |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_offers**
> List[WorkloadOffer] list_offers(org_id, status=status, partner=partner, offer_type=offer_type, product_id=product_id, buyer_id=buyer_id, hubspot_deal_id=hubspot_deal_id, contact_id=contact_id, limit=limit, offset=offset)

list offers

List offers under the given organization with pagination and optional filter.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_offer import WorkloadOffer
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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    status = 'status_example' # str | filter by offer status (optional)
    partner = 'partner_example' # str | filter by partner (optional)
    offer_type = 'offer_type_example' # str | filter by offerType (optional)
    product_id = 'product_id_example' # str | filter by productId (optional)
    buyer_id = 'buyer_id_example' # str | filter by buyerId (optional)
    hubspot_deal_id = 'hubspot_deal_id_example' # str | filter by hubspotDealId (optional)
    contact_id = 'contact_id_example' # str | filter by contactId (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list offers
        api_response = api_instance.list_offers(org_id, status=status, partner=partner, offer_type=offer_type, product_id=product_id, buyer_id=buyer_id, hubspot_deal_id=hubspot_deal_id, contact_id=contact_id, limit=limit, offset=offset)
        print("The response of OfferApi->list_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->list_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **status** | **str**| filter by offer status | [optional] 
 **partner** | **str**| filter by partner | [optional] 
 **offer_type** | **str**| filter by offerType | [optional] 
 **product_id** | **str**| filter by productId | [optional] 
 **buyer_id** | **str**| filter by buyerId | [optional] 
 **hubspot_deal_id** | **str**| filter by hubspotDealId | [optional] 
 **contact_id** | **str**| filter by contactId | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[WorkloadOffer]**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_offer_notifications**
> str send_offer_notifications(org_id, offer_id, contact_ids=contact_ids)

notify offer contacts

Send offer notifications to the given contact ids. If contactIDs is empty, send notifications to all contacts of the offer.

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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID
    contact_ids = ['contact_ids_example'] # List[str] | List of Contact IDs, if emoty or nil, send notifications to all contacts of the offer (optional)

    try:
        # notify offer contacts
        api_response = api_instance.send_offer_notifications(org_id, offer_id, contact_ids=contact_ids)
        print("The response of OfferApi->send_offer_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->send_offer_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 
 **contact_ids** | [**List[str]**](str.md)| List of Contact IDs, if emoty or nil, send notifications to all contacts of the offer | [optional] 

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
**200** | empty string if success |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer_meta_info**
> WorkloadMetaInfo update_offer_meta_info(org_id, offer_id, data)

update offer meta info

Update the meta info of the given offer.

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
    api_instance = suger_sdk_python.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID
    data = suger_sdk_python.WorkloadMetaInfo() # WorkloadMetaInfo | Offer meta info to update

    try:
        # update offer meta info
        api_response = api_instance.update_offer_meta_info(org_id, offer_id, data)
        print("The response of OfferApi->update_offer_meta_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->update_offer_meta_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| Offer ID | 
 **data** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md)| Offer meta info to update | 

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
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

