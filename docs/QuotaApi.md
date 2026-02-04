# suger_sdk_python.QuotaApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**org_org_id_quota_get**](QuotaApi.md#org_org_id_quota_get) | **GET** /org/{orgId}/quota | List organization quotas


# **org_org_id_quota_get**
> List[object] org_org_id_quota_get(org_id)

List organization quotas

Retrieves all service quotas for a specific organization. Creates missing quotas if any are not found.

### Example


```python
import suger_sdk_python
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
    api_instance = suger_sdk_python.QuotaApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # List organization quotas
        api_response = api_instance.org_org_id_quota_get(org_id)
        print("The response of QuotaApi->org_org_id_quota_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->org_org_id_quota_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of organization quotas |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

