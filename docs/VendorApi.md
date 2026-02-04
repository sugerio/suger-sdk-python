# suger_sdk_python.VendorApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vendor_product**](VendorApi.md#get_vendor_product) | **GET** /org/{orgId}/vendor/{vendorId}/product/{productId} | get vendor product
[**list_vendor_products**](VendorApi.md#list_vendor_products) | **GET** /org/{orgId}/vendor/{vendorId}/product | list vendor products


# **get_vendor_product**
> GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing get_vendor_product(org_id, vendor_id, product_id)

get vendor product

Get a specific marketplace listing/product for a vendor by its internal UUID. Returns the marketplace listing if it belongs to the specified vendor.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing import GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing
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
    api_instance = suger_sdk_python.VendorApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    vendor_id = 'vendor_id_example' # str | Vendor ID (Company ID where is_vendor=true)
    product_id = 'product_id_example' # str | Product ID (MarketplaceListing internal UUID)

    try:
        # get vendor product
        api_response = api_instance.get_vendor_product(org_id, vendor_id, product_id)
        print("The response of VendorApi->get_vendor_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->get_vendor_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **vendor_id** | **str**| Vendor ID (Company ID where is_vendor&#x3D;true) | 
 **product_id** | **str**| Product ID (MarketplaceListing internal UUID) | 

### Return type

[**GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing**](GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing.md)

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
**404** | Product not found or does not belong to vendor |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendor_products**
> GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmMarketplaceListing list_vendor_products(org_id, vendor_id, page_size=page_size, page_number=page_number, q=q, s=s)

list vendor products

List marketplace listings/products for a specific vendor with pagination and filtering. Returns marketplace listings linked to the vendor via company_id.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_crud_list_base_response_github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing import GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmMarketplaceListing
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
    api_instance = suger_sdk_python.VendorApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    vendor_id = 'vendor_id_example' # str | Vendor ID (Company ID where is_vendor=true)
    page_size = 56 # int | Number of items per page (default 20, max 1000) (optional)
    page_number = 56 # int | Page number (default 1) (optional)
    q = 'q_example' # str | LISP-style filter expression (e.g., '(ilike name \\ (optional)
    s = 's_example' # str | Sort fields: 'field:asc,field2:desc' or '-field,field2' format (e.g., 'name:asc' or '-name') (optional)

    try:
        # list vendor products
        api_response = api_instance.list_vendor_products(org_id, vendor_id, page_size=page_size, page_number=page_number, q=q, s=s)
        print("The response of VendorApi->list_vendor_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->list_vendor_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **vendor_id** | **str**| Vendor ID (Company ID where is_vendor&#x3D;true) | 
 **page_size** | **int**| Number of items per page (default 20, max 1000) | [optional] 
 **page_number** | **int**| Page number (default 1) | [optional] 
 **q** | **str**| LISP-style filter expression (e.g., &#39;(ilike name \\ | [optional] 
 **s** | **str**| Sort fields: &#39;field:asc,field2:desc&#39; or &#39;-field,field2&#39; format (e.g., &#39;name:asc&#39; or &#39;-name&#39;) | [optional] 

### Return type

[**GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmMarketplaceListing**](GithubComSugerioMarketplaceServicePkgCrudListBaseResponseGithubComSugerioMarketplaceServicePkgOrmMarketplaceListing.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of vendor products |  -  |
**400** | Bad request error |  -  |
**404** | Vendor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

