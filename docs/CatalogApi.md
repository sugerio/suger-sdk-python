# suger_sdk_python.CatalogApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vendor_details**](CatalogApi.md#get_vendor_details) | **GET** /org/{orgId}/catalog/vendor/{vendorId} | get vendor details
[**list_vendors**](CatalogApi.md#list_vendors) | **GET** /org/{orgId}/catalog/vendor | list vendors


# **get_vendor_details**
> GithubComSugerioMarketplaceServicePkgOrmGlobalCompany get_vendor_details(org_id, vendor_id)

get vendor details

Get detailed information about a specific vendor by ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_global_company import GithubComSugerioMarketplaceServicePkgOrmGlobalCompany
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
    api_instance = suger_sdk_python.CatalogApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    vendor_id = 'vendor_id_example' # str | Vendor ID

    try:
        # get vendor details
        api_response = api_instance.get_vendor_details(org_id, vendor_id)
        print("The response of CatalogApi->get_vendor_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_vendor_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **vendor_id** | **str**| Vendor ID | 

### Return type

[**GithubComSugerioMarketplaceServicePkgOrmGlobalCompany**](GithubComSugerioMarketplaceServicePkgOrmGlobalCompany.md)

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
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendors**
> GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmGlobalCompany list_vendors(org_id, page_size=page_size, page_number=page_number, q=q, s=s)

list vendors

List vendors with advanced filtering, sorting, and pagination using CRUD query language. Returns vendors that have is_vendor=true. Supports complex filters, sorting by multiple fields, and pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_crud_list_base_response_github_com_sugerio_marketplace_service_pkg_orm_global_company import GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmGlobalCompany
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
    api_instance = suger_sdk_python.CatalogApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    page_size = 56 # int | Number of items per page (default 20, max 1000) (optional)
    page_number = 56 # int | Page number (default 1) (optional)
    q = 'q_example' # str | LISP-style filter expression (e.g., '(and (= is_vendor true) (ilike name \\ (optional)
    s = 's_example' # str | Sort fields: 'field:asc,field2:desc' or '-field,field2' format (e.g., 'name:asc' or '-name') (optional)

    try:
        # list vendors
        api_response = api_instance.list_vendors(org_id, page_size=page_size, page_number=page_number, q=q, s=s)
        print("The response of CatalogApi->list_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->list_vendors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **page_size** | **int**| Number of items per page (default 20, max 1000) | [optional] 
 **page_number** | **int**| Page number (default 1) | [optional] 
 **q** | **str**| LISP-style filter expression (e.g., &#39;(and (&#x3D; is_vendor true) (ilike name \\ | [optional] 
 **s** | **str**| Sort fields: &#39;field:asc,field2:desc&#39; or &#39;-field,field2&#39; format (e.g., &#39;name:asc&#39; or &#39;-name&#39;) | [optional] 

### Return type

[**GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmGlobalCompany**](GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmGlobalCompany.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of vendors |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

