# openapi_client.CosellApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_cosell_opp_referrals**](CosellApi.md#list_cosell_opp_referrals) | **POST** /org/{orgId}/cosell/oppReferral/query | list cosell opp referrals


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

