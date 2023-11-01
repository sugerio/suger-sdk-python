# openapi_client.OfferApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_offer**](OfferApi.md#cancel_offer) | **POST** /org/{orgId}/offer/{offerId}/cancel | cancel offer
[**create_offer**](OfferApi.md#create_offer) | **POST** /org/{orgId}/offer | create offer
[**create_or_update_draft_offer**](OfferApi.md#create_or_update_draft_offer) | **POST** /org/{orgId}/draftOffer | create or update draft offer
[**delete_offer**](OfferApi.md#delete_offer) | **DELETE** /org/{orgId}/offer/{offerId} | delete offer
[**extend_private_offer_expiry_date**](OfferApi.md#extend_private_offer_expiry_date) | **POST** /org/{orgId}/offer/{offerId}/extendExpiryDate | extend offer expiry date
[**get_offer**](OfferApi.md#get_offer) | **GET** /org/{orgId}/offer/{offerId} | get offer
[**get_offer_eula**](OfferApi.md#get_offer_eula) | **GET** /org/{orgId}/offer/{offerId}/eula | get offer EULA
[**list_offers_by_contact**](OfferApi.md#list_offers_by_contact) | **GET** /org/{orgId}/contact/{contactId}/offer | list offers by contact
[**list_offers_by_organization**](OfferApi.md#list_offers_by_organization) | **GET** /org/{orgId}/offer | list offers by organization
[**list_offers_by_partner**](OfferApi.md#list_offers_by_partner) | **GET** /org/{orgId}/partner/{partner}/offer | list offers by partner
[**list_offers_by_product**](OfferApi.md#list_offers_by_product) | **GET** /org/{orgId}/product/{productId}/offer | list offers by product
[**send_offer_notifications**](OfferApi.md#send_offer_notifications) | **POST** /org/{orgId}/offer/{offerId}/notifyContacts | notify offer contacts
[**update_offer_meta_info**](OfferApi.md#update_offer_meta_info) | **PATCH** /org/{orgId}/offer/{offerId}/metaInfo | update offer meta info


# **cancel_offer**
> str cancel_offer(org_id, offer_id)

cancel offer

Only the offer with status = \"PENDING_ACCEPTANCE\" or \"PENDING_CANCEL\" is allowed to cancel.

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
    api_instance = openapi_client.OfferApi(api_client)
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

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty string if cancellation is successful |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_offer**
> WorkloadOffer create_offer(org_id, data)

create offer

Create a private offer under the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = openapi_client.WorkloadOffer() # WorkloadOffer | Offer to create

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

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = openapi_client.WorkloadOffer() # WorkloadOffer | the draft offer to create

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

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

Only the offer with status = \"DRAFT\" or \"CREATE_FAILED\" is allowed to be deleted.

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
    api_instance = openapi_client.OfferApi(api_client)
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

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty string if deletion is successful |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_private_offer_expiry_date**
> str extend_private_offer_expiry_date(org_id, offer_id, new_expiry_date)

extend offer expiry date

Only the offer with status = \"PENDING_ACCEPTANCE\" or \"EXPIRED\" is allowed to extend expiry date.

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
    api_instance = openapi_client.OfferApi(api_client)
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

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty string if extension is successful |  -  |
**400** | Bad request error |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer**
> WorkloadOffer get_offer(org_id, offer_id)

get offer

Get the offer by the given offer ID.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
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

[BearerTokenAuth](../README.md#BearerTokenAuth)

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
> str get_offer_eula(org_id, offer_id)

get offer EULA

Get the EULA file of the given offer ID.

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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID

    try:
        # get offer EULA
        api_response = api_instance.get_offer_eula(org_id, offer_id)
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
**200** | AWS S3 signed URL with 10 minutes expiry time |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_offers_by_contact**
> List[WorkloadOffer] list_offers_by_contact(org_id, contact_id)

list offers by contact

List all offers under the given organization & contact.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    contact_id = 'contact_id_example' # str | Contact ID

    try:
        # list offers by contact
        api_response = api_instance.list_offers_by_contact(org_id, contact_id)
        print("The response of OfferApi->list_offers_by_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->list_offers_by_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **contact_id** | **str**| Contact ID | 

### Return type

[**List[WorkloadOffer]**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_offers_by_organization**
> List[WorkloadOffer] list_offers_by_organization(org_id)

list offers by organization

List all offers under the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # list offers by organization
        api_response = api_instance.list_offers_by_organization(org_id)
        print("The response of OfferApi->list_offers_by_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->list_offers_by_organization: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**List[WorkloadOffer]**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_offers_by_partner**
> List[WorkloadOffer] list_offers_by_partner(org_id, partner)

list offers by partner

List all offers under the given organization & cloud partner.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner

    try:
        # list offers by partner
        api_response = api_instance.list_offers_by_partner(org_id, partner)
        print("The response of OfferApi->list_offers_by_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->list_offers_by_partner: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 

### Return type

[**List[WorkloadOffer]**](WorkloadOffer.md)

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
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_offers_by_product**
> List[WorkloadOffer] list_offers_by_product(org_id, product_id)

list offers by product

List all offers under the given organization & product.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.workload_offer import WorkloadOffer
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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID

    try:
        # list offers by product
        api_response = api_instance.list_offers_by_product(org_id, product_id)
        print("The response of OfferApi->list_offers_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferApi->list_offers_by_product: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 

### Return type

[**List[WorkloadOffer]**](WorkloadOffer.md)

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

# **send_offer_notifications**
> NotificationEvent send_offer_notifications(org_id, offer_id, contact_ids=contact_ids)

notify offer contacts

Send offer notifications to the given contact ids. If contactIds is empty, send notifications to all contacts of the offer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.notification_event import NotificationEvent
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
    api_instance = openapi_client.OfferApi(api_client)
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

[**NotificationEvent**](NotificationEvent.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NotificationEvent object |  -  |
**400** | Bad request error |  -  |
**405** | Method not allowed |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer_meta_info**
> WorkloadMetaInfo update_offer_meta_info(org_id, offer_id, data)

update offer meta info

Update the meta info of the given offer.

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
    api_instance = openapi_client.OfferApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | Offer ID
    data = openapi_client.WorkloadMetaInfo() # WorkloadMetaInfo | Offer meta info to update

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

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

