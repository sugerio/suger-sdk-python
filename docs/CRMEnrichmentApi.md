# suger_sdk_python.CRMEnrichmentApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**org_org_id_crm_enrichment_on_demand_post**](CRMEnrichmentApi.md#org_org_id_crm_enrichment_on_demand_post) | **POST** /org/{orgId}/crm/enrichment/on-demand | Trigger on-demand CRM record enrichment
[**org_org_id_integration_partner_service_enrichment_progress_get**](CRMEnrichmentApi.md#org_org_id_integration_partner_service_enrichment_progress_get) | **GET** /org/{orgId}/integration/{partner}/{service}/enrichment/progress | Get CRM enrichment progress
[**org_org_id_integration_partner_service_enrichment_validate_query_post**](CRMEnrichmentApi.md#org_org_id_integration_partner_service_enrichment_validate_query_post) | **POST** /org/{orgId}/integration/{partner}/{service}/enrichment/validate-query | Validate CRM query


# **org_org_id_crm_enrichment_on_demand_post**
> TriggerOnDemandEnrichmentResponse org_org_id_crm_enrichment_on_demand_post(org_id, company_domain, crm_record_id, crm_record_type, company_name=company_name)

Trigger on-demand CRM record enrichment

Enriches a single CRM record with intelligence data when viewing the record in browser extension

### Example


```python
import suger_sdk_python
from suger_sdk_python.models.trigger_on_demand_enrichment_response import TriggerOnDemandEnrichmentResponse
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with suger_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suger_sdk_python.CRMEnrichmentApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    company_domain = 'company_domain_example' # str | Company domain (e.g., acme.com)
    crm_record_id = 'crm_record_id_example' # str | CRM record ID
    crm_record_type = 'crm_record_type_example' # str | CRM record type (e.g., Opportunity, deals)
    company_name = 'company_name_example' # str | Company name (fallback if domain lookup fails) (optional)

    try:
        # Trigger on-demand CRM record enrichment
        api_response = api_instance.org_org_id_crm_enrichment_on_demand_post(org_id, company_domain, crm_record_id, crm_record_type, company_name=company_name)
        print("The response of CRMEnrichmentApi->org_org_id_crm_enrichment_on_demand_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRMEnrichmentApi->org_org_id_crm_enrichment_on_demand_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **company_domain** | **str**| Company domain (e.g., acme.com) | 
 **crm_record_id** | **str**| CRM record ID | 
 **crm_record_type** | **str**| CRM record type (e.g., Opportunity, deals) | 
 **company_name** | **str**| Company name (fallback if domain lookup fails) | [optional] 

### Return type

[**TriggerOnDemandEnrichmentResponse**](TriggerOnDemandEnrichmentResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_org_id_integration_partner_service_enrichment_progress_get**
> PkgHandlerGetEnrichmentProgressResponse org_org_id_integration_partner_service_enrichment_progress_get(org_id, partner, service, record_type)

Get CRM enrichment progress

Returns the progress of enrichment for a specific CRM record type, including cycle status and record counts

### Example


```python
import suger_sdk_python
from suger_sdk_python.models.pkg_handler_get_enrichment_progress_response import PkgHandlerGetEnrichmentProgressResponse
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with suger_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suger_sdk_python.CRMEnrichmentApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Partner (SALESFORCE or HUBSPOT)
    service = 'service_example' # str | Service (CRM)
    record_type = 'record_type_example' # str | Record type (e.g., Opportunity, Account, deals, companies)

    try:
        # Get CRM enrichment progress
        api_response = api_instance.org_org_id_integration_partner_service_enrichment_progress_get(org_id, partner, service, record_type)
        print("The response of CRMEnrichmentApi->org_org_id_integration_partner_service_enrichment_progress_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRMEnrichmentApi->org_org_id_integration_partner_service_enrichment_progress_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Partner (SALESFORCE or HUBSPOT) | 
 **service** | **str**| Service (CRM) | 
 **record_type** | **str**| Record type (e.g., Opportunity, Account, deals, companies) | 

### Return type

[**PkgHandlerGetEnrichmentProgressResponse**](PkgHandlerGetEnrichmentProgressResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_org_id_integration_partner_service_enrichment_validate_query_post**
> PkgHandlerValidateQueryResponse org_org_id_integration_partner_service_enrichment_validate_query_post(org_id, partner, service, request)

Validate CRM query

Validates a SOQL query (Salesforce) or Search API query (HubSpot) by executing it and returning record count

### Example


```python
import suger_sdk_python
from suger_sdk_python.models.pkg_handler_validate_query_request import PkgHandlerValidateQueryRequest
from suger_sdk_python.models.pkg_handler_validate_query_response import PkgHandlerValidateQueryResponse
from suger_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suger.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = suger_sdk_python.Configuration(
    host = "https://api.suger.cloud"
)


# Enter a context with an instance of the API client
with suger_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suger_sdk_python.CRMEnrichmentApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Partner (SALESFORCE or HUBSPOT)
    service = 'service_example' # str | Service (CRM)
    request = suger_sdk_python.PkgHandlerValidateQueryRequest() # PkgHandlerValidateQueryRequest | Query validation request

    try:
        # Validate CRM query
        api_response = api_instance.org_org_id_integration_partner_service_enrichment_validate_query_post(org_id, partner, service, request)
        print("The response of CRMEnrichmentApi->org_org_id_integration_partner_service_enrichment_validate_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRMEnrichmentApi->org_org_id_integration_partner_service_enrichment_validate_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Partner (SALESFORCE or HUBSPOT) | 
 **service** | **str**| Service (CRM) | 
 **request** | [**PkgHandlerValidateQueryRequest**](PkgHandlerValidateQueryRequest.md)| Query validation request | 

### Return type

[**PkgHandlerValidateQueryResponse**](PkgHandlerValidateQueryResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

