# suger_sdk_python.CosellApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**org_org_id_cosell_partner_aws_search_partner_post**](CosellApi.md#org_org_id_cosell_partner_aws_search_partner_post) | **POST** /org/{orgId}/cosell/partner/AWS/searchPartner | Search partner connections


# **org_org_id_cosell_partner_aws_search_partner_post**
> List[GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult] org_org_id_cosell_partner_aws_search_partner_post(org_id, query, limit=limit)

Search partner connections

Search for connected partners by name for AWS co-sell

### Example


```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result import GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult
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
    api_instance = suger_sdk_python.CosellApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    query = 'query_example' # str | Search query (partner name)
    limit = 56 # int | Maximum results (default 20, max 100) (optional)

    try:
        # Search partner connections
        api_response = api_instance.org_org_id_cosell_partner_aws_search_partner_post(org_id, query, limit=limit)
        print("The response of CosellApi->org_org_id_cosell_partner_aws_search_partner_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosellApi->org_org_id_cosell_partner_aws_search_partner_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **query** | **str**| Search query (partner name) | 
 **limit** | **int**| Maximum results (default 20, max 100) | [optional] 

### Return type

[**List[GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult]**](GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult.md)

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

