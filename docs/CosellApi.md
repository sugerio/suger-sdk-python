# openapi_client.CosellApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crm_record**](CosellApi.md#get_crm_record) | **GET** /org/{orgId}/cosell/partner/{partner}/object/{objectType}/{id} | get a record from a CRM partner.
[**list_cosell_opp_referrals**](CosellApi.md#list_cosell_opp_referrals) | **POST** /org/{orgId}/cosell/oppReferral/query | list cosell opp referrals
[**list_crm_records**](CosellApi.md#list_crm_records) | **GET** /org/{orgId}/cosell/partner/{partner}/object/{objectType} | list records from a CRM partner by object type and other conditions.
[**update_opp_referral_meta**](CosellApi.md#update_opp_referral_meta) | **PATCH** /org/{orgId}/cosell/oppReferralMeta/{oppReferralId} | update the metadata for cosell opp referral


# **get_crm_record**
> CosellRecord get_crm_record(org_id, partner, object_type, id)

get a record from a CRM partner.

get a record from a CRM partner by object type and ID.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cosell_record import CosellRecord
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CosellApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | CRM Partner
    object_type = 'object_type_example' # str | Type of the CRM object, e,g, account, contact
    id = 'id_example' # str | ID of the CRM object

    try:
        # get a record from a CRM partner.
        api_response = api_instance.get_crm_record(org_id, partner, object_type, id)
        print("The response of CosellApi->get_crm_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosellApi->get_crm_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| CRM Partner | 
 **object_type** | **str**| Type of the CRM object, e,g, account, contact | 
 **id** | **str**| ID of the CRM object | 

### Return type

[**CosellRecord**](CosellRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cosell_opp_referrals**
> ListCosellOppReferralsResponse list_cosell_opp_referrals(org_id, type=type, data=data)

list cosell opp referrals

list cosell opportunity referrals by orgId, referral type, and query conditions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_cosell_opp_referrals_response import ListCosellOppReferralsResponse
from openapi_client.models.sql_condition import SqlCondition
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CosellApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    type = 'type_example' # str | Referral type: inbox, outbox, insync, archived (optional)
    data = [openapi_client.SqlCondition()] # List[SqlCondition] | Query conditions (optional)

    try:
        # list cosell opp referrals
        api_response = api_instance.list_cosell_opp_referrals(org_id, type=type, data=data)
        print("The response of CosellApi->list_cosell_opp_referrals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosellApi->list_cosell_opp_referrals: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **type** | **str**| Referral type: inbox, outbox, insync, archived | [optional] 
 **data** | [**List[SqlCondition]**](SqlCondition.md)| Query conditions | [optional] 

### Return type

[**ListCosellOppReferralsResponse**](ListCosellOppReferralsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crm_records**
> CosellRecord list_crm_records(org_id, partner, object_type, limit=limit, offset=offset, name=name, website=website, email=email, account_id=account_id)

list records from a CRM partner by object type and other conditions.

list records from a CRM partner by object type, or search for SFDC accounts/contacts with given hints. To search for SFDC Accounts, add name and website in query params. To search for SFDC Contacts, add accountId and email in query params.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cosell_record import CosellRecord
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CosellApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | CRM Partner
    object_type = 'object_type_example' # str | Type of the CRM object, e,g, account, contact
    limit = 'limit_example' # str | Maximum number of records returned (optional)
    offset = 'offset_example' # str | Skip the given number of records (for pagination) (optional)
    name = 'name_example' # str | Name of the SFDC Account to search with (optional)
    website = 'website_example' # str | Website of the SFDC Account to search with (optional)
    email = 'email_example' # str | Email of the SFDC contact to search with (optional)
    account_id = 'account_id_example' # str | Only search for contacts within the given SFDC Account ID (optional)

    try:
        # list records from a CRM partner by object type and other conditions.
        api_response = api_instance.list_crm_records(org_id, partner, object_type, limit=limit, offset=offset, name=name, website=website, email=email, account_id=account_id)
        print("The response of CosellApi->list_crm_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosellApi->list_crm_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| CRM Partner | 
 **object_type** | **str**| Type of the CRM object, e,g, account, contact | 
 **limit** | **str**| Maximum number of records returned | [optional] 
 **offset** | **str**| Skip the given number of records (for pagination) | [optional] 
 **name** | **str**| Name of the SFDC Account to search with | [optional] 
 **website** | **str**| Website of the SFDC Account to search with | [optional] 
 **email** | **str**| Email of the SFDC contact to search with | [optional] 
 **account_id** | **str**| Only search for contacts within the given SFDC Account ID | [optional] 

### Return type

[**CosellRecord**](CosellRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_opp_referral_meta**
> str update_opp_referral_meta(org_id, opp_referral_id, data)

update the metadata for cosell opp referral

update the metadata for a coselll opp referral to change the referral status, archive, etc.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.cosell_opp_meta import CosellOppMeta
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CosellApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    opp_referral_id = 'opp_referral_id_example' # str | ID of the OppReferral instance
    data = openapi_client.CosellOppMeta() # CosellOppMeta | metainfo to update

    try:
        # update the metadata for cosell opp referral
        api_response = api_instance.update_opp_referral_meta(org_id, opp_referral_id, data)
        print("The response of CosellApi->update_opp_referral_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosellApi->update_opp_referral_meta: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **opp_referral_id** | **str**| ID of the OppReferral instance | 
 **data** | [**CosellOppMeta**](CosellOppMeta.md)| metainfo to update | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

