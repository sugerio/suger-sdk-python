# openapi_client.MeteringApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_report_usage_record_groups**](MeteringApi.md#batch_report_usage_record_groups) | **POST** /org/{orgId}/batchCreateUsageRecordGroups | batch report usageRecordGroups
[**batch_validate_usage_record_groups**](MeteringApi.md#batch_validate_usage_record_groups) | **POST** /org/{orgId}/batchValidateUsageRecordGroups | batch validate usageRecordGroups
[**delete_usage_record_group**](MeteringApi.md#delete_usage_record_group) | **DELETE** /org/{orgId}/usageRecordGroup/{usageRecordGroupId} | delete usageRecordGroup
[**get_usage_metering_config_info**](MeteringApi.md#get_usage_metering_config_info) | **GET** /org/{orgId}/usageMeteringConfigInfo | get usage metering config info
[**get_usage_record_group**](MeteringApi.md#get_usage_record_group) | **GET** /org/{orgId}/usageRecordGroup/{usageRecordGroupId} | get usageRecordGroup
[**get_usage_record_report**](MeteringApi.md#get_usage_record_report) | **GET** /org/{orgId}/usageRecordReport/{usageRecordReportId} | get usageRecordReport
[**list_usage_record_groups**](MeteringApi.md#list_usage_record_groups) | **GET** /org/{orgId}/usageRecordGroup | list usageRecordGroups
[**list_usage_record_groups_by_entitlement**](MeteringApi.md#list_usage_record_groups_by_entitlement) | **GET** /org/{orgId}/entitlement/{entitlementId}/usageRecordGroup | list usageRecordGroups by entitlement
[**list_usage_record_groups_by_product**](MeteringApi.md#list_usage_record_groups_by_product) | **GET** /org/{orgId}/product/{productId}/usageRecordGroup | list usageRecordGroups by product
[**list_usage_record_reports**](MeteringApi.md#list_usage_record_reports) | **GET** /org/{orgId}/usageRecordReport | list usageRecordReports
[**report_usage_record_group**](MeteringApi.md#report_usage_record_group) | **POST** /org/{orgId}/entitlement/{entitlementId}/usageRecordGroup | report usageRecordGroup
[**update_usage_metering_config_info**](MeteringApi.md#update_usage_metering_config_info) | **PATCH** /org/{orgId}/usageMeteringConfigInfo | update usage metering config info


# **batch_report_usage_record_groups**
> List[MeteringUsageRecordGroup] batch_report_usage_record_groups(org_id, usage_record_groups)

batch report usageRecordGroups

Batch report new usage record groups.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.metering_usage_record_group import MeteringUsageRecordGroup
from openapi_client.models.new_usage_record_group import NewUsageRecordGroup
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_groups = [openapi_client.NewUsageRecordGroup()] # List[NewUsageRecordGroup] | Array of new usage record groups to report

    try:
        # batch report usageRecordGroups
        api_response = api_instance.batch_report_usage_record_groups(org_id, usage_record_groups)
        print("The response of MeteringApi->batch_report_usage_record_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->batch_report_usage_record_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **usage_record_groups** | [**List[NewUsageRecordGroup]**](NewUsageRecordGroup.md)| Array of new usage record groups to report | 

### Return type

[**List[MeteringUsageRecordGroup]**](MeteringUsageRecordGroup.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | all the quantity of usage records are zero |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_validate_usage_record_groups**
> str batch_validate_usage_record_groups(org_id, data)

batch validate usageRecordGroups

Provide a batch of usage record groups and validate each individual usage record group one by one.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.new_usage_record_group import NewUsageRecordGroup
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = [openapi_client.NewUsageRecordGroup()] # List[NewUsageRecordGroup] | Array of usage record groups to be validated

    try:
        # batch validate usageRecordGroups
        api_response = api_instance.batch_validate_usage_record_groups(org_id, data)
        print("The response of MeteringApi->batch_validate_usage_record_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->batch_validate_usage_record_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**List[NewUsageRecordGroup]**](NewUsageRecordGroup.md)| Array of usage record groups to be validated | 

### Return type

**str**

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty string if validation is successful |  -  |
**400** | Bad request error description |  -  |
**500** | validation failed for usage record group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage_record_group**
> MeteringUsageRecordGroup delete_usage_record_group(org_id, usage_record_group_id)

delete usageRecordGroup

delete the UsageRecordGroup for the given organization and usageRecordGroup ID. Only usageRecordGroup with status \"CREATED\" or \"INVALID\" can be deleted.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.metering_usage_record_group import MeteringUsageRecordGroup
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_group_id = 'usage_record_group_id_example' # str | UsageRecordGroup ID

    try:
        # delete usageRecordGroup
        api_response = api_instance.delete_usage_record_group(org_id, usage_record_group_id)
        print("The response of MeteringApi->delete_usage_record_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->delete_usage_record_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **usage_record_group_id** | **str**| UsageRecordGroup ID | 

### Return type

[**MeteringUsageRecordGroup**](MeteringUsageRecordGroup.md)

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
**404** | usageRecordGroup not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_metering_config_info**
> UsageMeteringConfigInfo get_usage_metering_config_info(org_id)

get usage metering config info

Get the usage metering config info of the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.usage_metering_config_info import UsageMeteringConfigInfo
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # get usage metering config info
        api_response = api_instance.get_usage_metering_config_info(org_id)
        print("The response of MeteringApi->get_usage_metering_config_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_usage_metering_config_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**UsageMeteringConfigInfo**](UsageMeteringConfigInfo.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage metering config info |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_record_group**
> MeteringUsageRecordGroup get_usage_record_group(org_id, usage_record_group_id)

get usageRecordGroup

get UsageRecordGroup for the given organization and usageRecordGroup ID

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.metering_usage_record_group import MeteringUsageRecordGroup
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_group_id = 'usage_record_group_id_example' # str | UsageRecordGroup ID

    try:
        # get usageRecordGroup
        api_response = api_instance.get_usage_record_group(org_id, usage_record_group_id)
        print("The response of MeteringApi->get_usage_record_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_usage_record_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **usage_record_group_id** | **str**| UsageRecordGroup ID | 

### Return type

[**MeteringUsageRecordGroup**](MeteringUsageRecordGroup.md)

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
**404** | usageRecordGroup not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_record_report**
> MeteringUsageRecordReport get_usage_record_report(org_id, usage_record_report_id)

get usageRecordReport

get the usageRecordReport for a given organization and usageRecordReport ID.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.metering_usage_record_report import MeteringUsageRecordReport
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_report_id = 'usage_record_report_id_example' # str | UsageRecordReport ID

    try:
        # get usageRecordReport
        api_response = api_instance.get_usage_record_report(org_id, usage_record_report_id)
        print("The response of MeteringApi->get_usage_record_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_usage_record_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **usage_record_report_id** | **str**| UsageRecordReport ID | 

### Return type

[**MeteringUsageRecordReport**](MeteringUsageRecordReport.md)

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
**404** | usageRecordReport not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_groups**
> ListUsageRecordGroupsResponse list_usage_record_groups(org_id, partner=partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usageRecordGroups

List UsageRecordGroups by the given organization, partner, product, entitlement or buyer. Only provide one or none of the optional query parameters: partner, productId, entitlementId & buyerId .

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_usage_record_groups_response import ListUsageRecordGroupsResponse
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner (optional)
    product_id = 'product_id_example' # str | product ID (optional)
    entitlement_id = 'entitlement_id_example' # str | entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | buyer ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usageRecordGroups
        api_response = api_instance.list_usage_record_groups(org_id, partner=partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of MeteringApi->list_usage_record_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->list_usage_record_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | [optional] 
 **product_id** | **str**| product ID | [optional] 
 **entitlement_id** | **str**| entitlement ID | [optional] 
 **buyer_id** | **str**| buyer ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageRecordGroupsResponse**](ListUsageRecordGroupsResponse.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_groups_by_entitlement**
> ListUsageRecordGroupsResponse list_usage_record_groups_by_entitlement(org_id, entitlement_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usageRecordGroups by entitlement

List UsageRecordGroups by the given organization and entitlement.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_usage_record_groups_response import ListUsageRecordGroupsResponse
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | entitlement ID
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usageRecordGroups by entitlement
        api_response = api_instance.list_usage_record_groups_by_entitlement(org_id, entitlement_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of MeteringApi->list_usage_record_groups_by_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->list_usage_record_groups_by_entitlement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| entitlement ID | 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageRecordGroupsResponse**](ListUsageRecordGroupsResponse.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_groups_by_product**
> ListUsageRecordGroupsResponse list_usage_record_groups_by_product(org_id, product_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usageRecordGroups by product

List UsageRecordGroups by the given organization and product.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_usage_record_groups_response import ListUsageRecordGroupsResponse
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    product_id = 'product_id_example' # str | product ID
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usageRecordGroups by product
        api_response = api_instance.list_usage_record_groups_by_product(org_id, product_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of MeteringApi->list_usage_record_groups_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->list_usage_record_groups_by_product: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **product_id** | **str**| product ID | 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageRecordGroupsResponse**](ListUsageRecordGroupsResponse.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_reports**
> ListUsageRecordReportsResponse list_usage_record_reports(org_id, partner=partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usageRecordReports

List usageRecordReports under the given organization, partner, product, entitlement or buyer. Only provide one or none of the following parameters: partner, product, entitlement or buyer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_usage_record_reports_response import ListUsageRecordReportsResponse
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner (optional)
    product_id = 'product_id_example' # str | product ID (optional)
    entitlement_id = 'entitlement_id_example' # str | entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | buyer ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usageRecordReports
        api_response = api_instance.list_usage_record_reports(org_id, partner=partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of MeteringApi->list_usage_record_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->list_usage_record_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | [optional] 
 **product_id** | **str**| product ID | [optional] 
 **entitlement_id** | **str**| entitlement ID | [optional] 
 **buyer_id** | **str**| buyer ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageRecordReportsResponse**](ListUsageRecordReportsResponse.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_usage_record_group**
> MeteringUsageRecordGroup report_usage_record_group(org_id, entitlement_id, data)

report usageRecordGroup

It is recommended to provide the ID in the request body CreateUsageRecordGroupParams, so the report can be deduplicated. All duplicate report will return error code 409.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.create_usage_record_group_params import CreateUsageRecordGroupParams
from openapi_client.models.metering_usage_record_group import MeteringUsageRecordGroup
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = openapi_client.CreateUsageRecordGroupParams() # CreateUsageRecordGroupParams | RequestBody

    try:
        # report usageRecordGroup
        api_response = api_instance.report_usage_record_group(org_id, entitlement_id, data)
        print("The response of MeteringApi->report_usage_record_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->report_usage_record_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **entitlement_id** | **str**| Entitlement ID | 
 **data** | [**CreateUsageRecordGroupParams**](CreateUsageRecordGroupParams.md)| RequestBody | 

### Return type

[**MeteringUsageRecordGroup**](MeteringUsageRecordGroup.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | all the quantity of usage records are zero |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_metering_config_info**
> UsageMeteringConfigInfo update_usage_metering_config_info(org_id, data)

update usage metering config info

Update the usage metering config info of the given organization.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.usage_metering_config_info import UsageMeteringConfigInfo
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
    api_instance = openapi_client.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = openapi_client.UsageMeteringConfigInfo() # UsageMeteringConfigInfo | The usage metering config info to be updated

    try:
        # update usage metering config info
        api_response = api_instance.update_usage_metering_config_info(org_id, data)
        print("The response of MeteringApi->update_usage_metering_config_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->update_usage_metering_config_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**UsageMeteringConfigInfo**](UsageMeteringConfigInfo.md)| The usage metering config info to be updated | 

### Return type

[**UsageMeteringConfigInfo**](UsageMeteringConfigInfo.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage metering config info |  -  |
**400** | Bad request error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

