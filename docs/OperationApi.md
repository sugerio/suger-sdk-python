# openapi_client.OperationApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_operations**](OperationApi.md#list_operations) | **GET** /org/{orgId}/operation | list operations


# **list_operations**
> List[Operation] list_operations(org_id, offer_id=offer_id, entitlement_id=entitlement_id, crm_opportunity_id=crm_opportunity_id, partner_opportunity_id=partner_opportunity_id)

list operations

List all long running operations under the given organization, offer, entitlement, crmOpportunity or partnerOpportunity. Only provide one filter on a request.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.OperationApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    offer_id = 'offer_id_example' # str | filter by offerId (optional)
    entitlement_id = 'entitlement_id_example' # str | filter by entitlementId (optional)
    crm_opportunity_id = 'crm_opportunity_id_example' # str | filter by crmOpportunityId (optional)
    partner_opportunity_id = 'partner_opportunity_id_example' # str | filter by partnerOpportunityId (optional)

    try:
        # list operations
        api_response = api_instance.list_operations(org_id, offer_id=offer_id, entitlement_id=entitlement_id, crm_opportunity_id=crm_opportunity_id, partner_opportunity_id=partner_opportunity_id)
        print("The response of OperationApi->list_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationApi->list_operations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **offer_id** | **str**| filter by offerId | [optional] 
 **entitlement_id** | **str**| filter by entitlementId | [optional] 
 **crm_opportunity_id** | **str**| filter by crmOpportunityId | [optional] 
 **partner_opportunity_id** | **str**| filter by partnerOpportunityId | [optional] 

### Return type

[**List[Operation]**](Operation.md)

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

