# suger_sdk_python.ProductApi

All URIs are relative to *http://https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_draft_product**](ProductApi.md#create_or_update_draft_product) | **POST** /org/{orgId}/draftProduct | create or update draft product
[**create_product**](ProductApi.md#create_product) | **POST** /org/{orgId}/product | create product
[**delete_product**](ProductApi.md#delete_product) | **DELETE** /org/{orgId}/product/{productId} | delete product
[**get_product**](ProductApi.md#get_product) | **GET** /org/{orgId}/product/{productId} | get product
[**list_product_metering_dimensions**](ProductApi.md#list_product_metering_dimensions) | **GET** /org/{orgId}/product/{productId}/dimension | list metering dimensions of product
[**list_products**](ProductApi.md#list_products) | **GET** /org/{orgId}/product | list products
[**list_products_by_partner**](ProductApi.md#list_products_by_partner) | **GET** /org/{orgId}/partner/{partner}/product | list products by partner
[**publish_product**](ProductApi.md#publish_product) | **PATCH** /org/{orgId}/product/{productId}/publish | publish product
[**update_product**](ProductApi.md#update_product) | **PATCH** /org/{orgId}/product/{productId} | update product
[**update_product_fulfillment_url**](ProductApi.md#update_product_fulfillment_url) | **PATCH** /org/{orgId}/product/{productId}/fulfillmentUrl | update product fulfillment url
[**update_product_meta_info**](ProductApi.md#update_product_meta_info) | **PATCH** /org/{orgId}/product/{productId}/metaInfo | update product meta info


# **create_or_update_draft_product**
> WorkloadProduct create_or_update_draft_product(org_id, data)

create or update draft product

Create a new draft product or update the existing draft product. When updating draft product, the product.ID is required.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.WorkloadProduct() # WorkloadProduct | the draft product to create

    try:
        # create or update draft product
        api_response = api_instance.create_or_update_draft_product(org_id, data)
        print("The response of ProductApi->create_or_update_draft_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_or_update_draft_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**WorkloadProduct**](WorkloadProduct.md)| the draft product to create | 

### Return type

[**WorkloadProduct**](WorkloadProduct.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product**
> WorkloadProduct create_product(org_id, data)

create product

create a new product in the marketplace

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.WorkloadProduct() # WorkloadProduct | the product to create

    try:
        # create product
        api_response = api_instance.create_product(org_id, data)
        print("The response of ProductApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**WorkloadProduct**](WorkloadProduct.md)| the product to create | 

### Return type

[**WorkloadProduct**](WorkloadProduct.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product**
> str delete_product(org_id, product_id)

delete product

The product is soft deleted (marked as DELETED status) in Suger service. only the products with non PUBLIC status are allowed to be deleted.

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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID

    try:
        # delete product
        api_response = api_instance.delete_product(org_id, product_id)
        print("The response of ProductApi->delete_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->delete_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> WorkloadProduct get_product(org_id, product_id)

get product

get product by product id

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID

    try:
        # get product
        api_response = api_instance.get_product(org_id, product_id)
        print("The response of ProductApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 

### Return type

[**WorkloadProduct**](WorkloadProduct.md)

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
**404** | Not found error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_metering_dimensions**
> List[MeteringDimension] list_product_metering_dimensions(org_id, product_id)

list metering dimensions of product

list all metering dimensions of the given product

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.metering_dimension import MeteringDimension
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID

    try:
        # list metering dimensions of product
        api_response = api_instance.list_product_metering_dimensions(org_id, product_id)
        print("The response of ProductApi->list_product_metering_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_product_metering_dimensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 

### Return type

[**List[MeteringDimension]**](MeteringDimension.md)

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
**404** | Not found error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> List[WorkloadProduct] list_products(org_id, partner=partner, limit=limit, offset=offset)

list products

list all products under the given organization

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | filter by partner (optional)
    limit = 56 # int | List pagination size, default 100, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list products
        api_response = api_instance.list_products(org_id, partner=partner, limit=limit, offset=offset)
        print("The response of ProductApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| filter by partner | [optional] 
 **limit** | **int**| List pagination size, default 100, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**List[WorkloadProduct]**](WorkloadProduct.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products_by_partner**
> List[WorkloadProduct] list_products_by_partner(org_id, partner)

list products by partner

list all products under the given organization and cloud partner

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner

    try:
        # list products by partner
        api_response = api_instance.list_products_by_partner(org_id, partner)
        print("The response of ProductApi->list_products_by_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->list_products_by_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 

### Return type

[**List[WorkloadProduct]**](WorkloadProduct.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_product**
> WorkloadProduct publish_product(org_id, product_id, data)

publish product

publish the given product to the public status in the marketplace

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID
    data = suger_sdk_python.WorkloadProduct() # WorkloadProduct | the product to publish

    try:
        # publish product
        api_response = api_instance.publish_product(org_id, product_id, data)
        print("The response of ProductApi->publish_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->publish_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 
 **data** | [**WorkloadProduct**](WorkloadProduct.md)| the product to publish | 

### Return type

[**WorkloadProduct**](WorkloadProduct.md)

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
**404** | Not found error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> WorkloadProduct update_product(org_id, product_id, data)

update product

update product info, no price update is allowed via this API.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID
    data = suger_sdk_python.WorkloadProduct() # WorkloadProduct | the product to update

    try:
        # update product
        api_response = api_instance.update_product(org_id, product_id, data)
        print("The response of ProductApi->update_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 
 **data** | [**WorkloadProduct**](WorkloadProduct.md)| the product to update | 

### Return type

[**WorkloadProduct**](WorkloadProduct.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_fulfillment_url**
> WorkloadProduct update_product_fulfillment_url(org_id, product_id, data)

update product fulfillment url

update the fulfillment url of the given product

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.update_product_params import UpdateProductParams
from suger_sdk_python.models.workload_product import WorkloadProduct
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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID
    data = suger_sdk_python.UpdateProductParams() # UpdateProductParams | Update Product Params

    try:
        # update product fulfillment url
        api_response = api_instance.update_product_fulfillment_url(org_id, product_id, data)
        print("The response of ProductApi->update_product_fulfillment_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_product_fulfillment_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 
 **data** | [**UpdateProductParams**](UpdateProductParams.md)| Update Product Params | 

### Return type

[**WorkloadProduct**](WorkloadProduct.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_meta_info**
> WorkloadMetaInfo update_product_meta_info(org_id, product_id, data)

update product meta info

Update the meta info of the given product.

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
    api_instance = suger_sdk_python.ProductApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | Product ID
    data = suger_sdk_python.WorkloadMetaInfo() # WorkloadMetaInfo | Product meta info to update

    try:
        # update product meta info
        api_response = api_instance.update_product_meta_info(org_id, product_id, data)
        print("The response of ProductApi->update_product_meta_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->update_product_meta_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| Product ID | 
 **data** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md)| Product meta info to update | 

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
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

