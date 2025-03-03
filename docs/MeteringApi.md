# suger_sdk_python.MeteringApi

All URIs are relative to *http://https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_report_usage_record_groups**](MeteringApi.md#batch_report_usage_record_groups) | **POST** /org/{orgId}/batchCreateUsageRecordGroups | batch report usageRecordGroups
[**batch_validate_usage_record_groups**](MeteringApi.md#batch_validate_usage_record_groups) | **POST** /org/{orgId}/batchValidateUsageRecordGroups | batch validate usageRecordGroups
[**create_billable_metric**](MeteringApi.md#create_billable_metric) | **POST** /org/{orgId}/billableMetric | create billable metric
[**delete_usage_record_group**](MeteringApi.md#delete_usage_record_group) | **DELETE** /org/{orgId}/usageRecordGroup/{usageRecordGroupId} | delete usageRecordGroup
[**get_billable_metric**](MeteringApi.md#get_billable_metric) | **GET** /org/{orgId}/billableMetric/{billableMetricId} | get billable metric
[**get_usage_metering_config_info**](MeteringApi.md#get_usage_metering_config_info) | **GET** /org/{orgId}/usageMeteringConfigInfo | get usage metering config info
[**list_billable_metrics**](MeteringApi.md#list_billable_metrics) | **GET** /org/{orgId}/billableMetric | list billable metrics
[**list_usage_record_groups**](MeteringApi.md#list_usage_record_groups) | **GET** /org/{orgId}/usageRecordGroup | list usageRecordGroups
[**list_usage_record_reports**](MeteringApi.md#list_usage_record_reports) | **GET** /org/{orgId}/usageRecordReport | list usageRecordReports
[**report_usage_record_group**](MeteringApi.md#report_usage_record_group) | **POST** /org/{orgId}/entitlement/{entitlementId}/usageRecordGroup | report usageRecordGroup
[**retry_usage_record_group**](MeteringApi.md#retry_usage_record_group) | **POST** /org/{orgId}/usageRecordGroup/{usageRecordGroupId}/retry | retry usageRecordGroup
[**update_billable_metric**](MeteringApi.md#update_billable_metric) | **PATCH** /org/{orgId}/billableMetric/{billableMetricId} | update billable metric
[**update_usage_metering_config_info**](MeteringApi.md#update_usage_metering_config_info) | **PATCH** /org/{orgId}/usageMeteringConfigInfo | update usage metering config info


# **batch_report_usage_record_groups**
> List[MeteringUsageRecordGroup] batch_report_usage_record_groups(org_id, usage_record_groups)

batch report usageRecordGroups

Batch report new usage record groups.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.metering_usage_record_group import MeteringUsageRecordGroup
from suger_sdk_python.models.new_usage_record_group import NewUsageRecordGroup
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_groups = [suger_sdk_python.NewUsageRecordGroup()] # List[NewUsageRecordGroup] | Array of new usage record groups to report

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

[APIKeyAuth](../README.md#APIKeyAuth)

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

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.new_usage_record_group import NewUsageRecordGroup
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = [suger_sdk_python.NewUsageRecordGroup()] # List[NewUsageRecordGroup] | Array of usage record groups to be validated

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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **create_billable_metric**
> BillableMetric create_billable_metric(org_id, data)

create billable metric

Create a new billable metric for the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billable_metric import BillableMetric
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.BillableMetric() # BillableMetric | RequestBody

    try:
        # create billable metric
        api_response = api_instance.create_billable_metric(org_id, data)
        print("The response of MeteringApi->create_billable_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->create_billable_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**BillableMetric**](BillableMetric.md)| RequestBody | 

### Return type

[**BillableMetric**](BillableMetric.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request params |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage_record_group**
> MeteringUsageRecordGroup delete_usage_record_group(org_id, usage_record_group_id, creation_date=creation_date)

delete usageRecordGroup

delete the UsageRecordGroup for the given organization and usageRecordGroup ID. Only usageRecordGroup with status \"CREATED\" or \"INVALID\" can be deleted.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.metering_usage_record_group import MeteringUsageRecordGroup
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_group_id = 'usage_record_group_id_example' # str | UsageRecordGroup ID
    creation_date = 'creation_date_example' # str | UsageRecordGroup's creation date (UTC) in YYYY-MM-DD format (optional)

    try:
        # delete usageRecordGroup
        api_response = api_instance.delete_usage_record_group(org_id, usage_record_group_id, creation_date=creation_date)
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
 **creation_date** | **str**| UsageRecordGroup&#39;s creation date (UTC) in YYYY-MM-DD format | [optional] 

### Return type

[**MeteringUsageRecordGroup**](MeteringUsageRecordGroup.md)

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
**404** | usageRecordGroup not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billable_metric**
> BillableMetric get_billable_metric(org_id, billable_metric_id)

get billable metric

Get the billable metric for the given organization and billable metric ID.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billable_metric import BillableMetric
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    billable_metric_id = 'billable_metric_id_example' # str | Billable Metric ID

    try:
        # get billable metric
        api_response = api_instance.get_billable_metric(org_id, billable_metric_id)
        print("The response of MeteringApi->get_billable_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->get_billable_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **billable_metric_id** | **str**| Billable Metric ID | 

### Return type

[**BillableMetric**](BillableMetric.md)

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
**404** | billable metric not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_metering_config_info**
> UsageMeteringConfigInfo get_usage_metering_config_info(org_id)

get usage metering config info

Get the usage metering config info of the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.usage_metering_config_info import UsageMeteringConfigInfo
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **list_billable_metrics**
> List[BillableMetric] list_billable_metrics(org_id, status=status)

list billable metrics

list billable metrics for the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billable_metric import BillableMetric
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    status = 'status_example' # str | Status of the billable metric (optional)

    try:
        # list billable metrics
        api_response = api_instance.list_billable_metrics(org_id, status=status)
        print("The response of MeteringApi->list_billable_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->list_billable_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **status** | **str**| Status of the billable metric | [optional] 

### Return type

[**List[BillableMetric]**](BillableMetric.md)

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

# **list_usage_record_groups**
> ListUsageRecordGroupsResponse list_usage_record_groups(org_id, partner=partner, buyer_id=buyer_id, entitlement_id=entitlement_id, status=status, source=source, meta_info=meta_info, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usageRecordGroups

List UsageRecordGroups by the given organization, partner, product, entitlement or buyer. Only provide one or none of the optional query parameters: partner, productId, entitlementId & buyerId .

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_usage_record_groups_response import ListUsageRecordGroupsResponse
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner (optional)
    buyer_id = 'buyer_id_example' # str | filter by buyer ID, default no filter by buyerId if not provided (optional)
    entitlement_id = 'entitlement_id_example' # str | filter by entitlement ID, default no filter by entitlementId if not provided (optional)
    status = 'status_example' # str | The status of the usage record group, default no filter by status if not provided (optional)
    source = 'source_example' # str | The source of the usage record group, default no filter by source if not provided (optional)
    meta_info = 'meta_info_example' # str | metaInfo filter (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usageRecordGroups
        api_response = api_instance.list_usage_record_groups(org_id, partner=partner, buyer_id=buyer_id, entitlement_id=entitlement_id, status=status, source=source, meta_info=meta_info, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
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
 **buyer_id** | **str**| filter by buyer ID, default no filter by buyerId if not provided | [optional] 
 **entitlement_id** | **str**| filter by entitlement ID, default no filter by entitlementId if not provided | [optional] 
 **status** | **str**| The status of the usage record group, default no filter by status if not provided | [optional] 
 **source** | **str**| The source of the usage record group, default no filter by source if not provided | [optional] 
 **meta_info** | **str**| metaInfo filter | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageRecordGroupsResponse**](ListUsageRecordGroupsResponse.md)

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

# **list_usage_record_reports**
> ListUsageRecordReportsResponse list_usage_record_reports(org_id, partner=partner, buyer_id=buyer_id, entitlement_id=entitlement_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usageRecordReports

List usageRecordReports under the given organization, partner, entitlement or buyer, within the given time range and pagination.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.list_usage_record_reports_response import ListUsageRecordReportsResponse
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner (optional)
    buyer_id = 'buyer_id_example' # str | buyer ID (optional)
    entitlement_id = 'entitlement_id_example' # str | entitlement ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 1000, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usageRecordReports
        api_response = api_instance.list_usage_record_reports(org_id, partner=partner, buyer_id=buyer_id, entitlement_id=entitlement_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
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
 **buyer_id** | **str**| buyer ID | [optional] 
 **entitlement_id** | **str**| entitlement ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 1000, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageRecordReportsResponse**](ListUsageRecordReportsResponse.md)

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

# **report_usage_record_group**
> MeteringUsageRecordGroup report_usage_record_group(org_id, entitlement_id, data)

report usageRecordGroup

It is recommended to provide the ID in the request body CreateUsageRecordGroupParams, so the report can be deduplicated. All duplicate report will return error code 409.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.create_usage_record_group_params import CreateUsageRecordGroupParams
from suger_sdk_python.models.metering_usage_record_group import MeteringUsageRecordGroup
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    entitlement_id = 'entitlement_id_example' # str | Entitlement ID
    data = suger_sdk_python.CreateUsageRecordGroupParams() # CreateUsageRecordGroupParams | RequestBody

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

[APIKeyAuth](../README.md#APIKeyAuth)

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

# **retry_usage_record_group**
> MeteringUsageRecordGroup retry_usage_record_group(org_id, usage_record_group_id, creation_date=creation_date)

retry usageRecordGroup

Retry the given UsageRecordGroup by setting from status \"REPORT_FAILED\" to \"CREATED\", and it will be ready for the next hourly report. Only usageRecordGroup with status \"REPORT_FAILED\" can be retried.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.metering_usage_record_group import MeteringUsageRecordGroup
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    usage_record_group_id = 'usage_record_group_id_example' # str | UsageRecordGroup ID
    creation_date = 'creation_date_example' # str | UsageRecordGroup's creation date (UTC) in YYYY-MM-DD format (optional)

    try:
        # retry usageRecordGroup
        api_response = api_instance.retry_usage_record_group(org_id, usage_record_group_id, creation_date=creation_date)
        print("The response of MeteringApi->retry_usage_record_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->retry_usage_record_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **usage_record_group_id** | **str**| UsageRecordGroup ID | 
 **creation_date** | **str**| UsageRecordGroup&#39;s creation date (UTC) in YYYY-MM-DD format | [optional] 

### Return type

[**MeteringUsageRecordGroup**](MeteringUsageRecordGroup.md)

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
**404** | usageRecordGroup not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billable_metric**
> BillableMetric update_billable_metric(org_id, billable_metric_id, data)

update billable metric

Update the name, description and status of the billable metric for the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.billable_metric import BillableMetric
from suger_sdk_python.models.update_billable_metric_params import UpdateBillableMetricParams
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    billable_metric_id = 'billable_metric_id_example' # str | Billable Metric ID
    data = suger_sdk_python.UpdateBillableMetricParams() # UpdateBillableMetricParams | RequestBody

    try:
        # update billable metric
        api_response = api_instance.update_billable_metric(org_id, billable_metric_id, data)
        print("The response of MeteringApi->update_billable_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteringApi->update_billable_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **billable_metric_id** | **str**| Billable Metric ID | 
 **data** | [**UpdateBillableMetricParams**](UpdateBillableMetricParams.md)| RequestBody | 

### Return type

[**BillableMetric**](BillableMetric.md)

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
**404** | billable metric not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_metering_config_info**
> UsageMeteringConfigInfo update_usage_metering_config_info(org_id, data)

update usage metering config info

Update the usage metering config info of the given organization.

### Example

* Api Key Authentication (APIKeyAuth):

```python
import suger_sdk_python
from suger_sdk_python.models.usage_metering_config_info import UsageMeteringConfigInfo
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
    api_instance = suger_sdk_python.MeteringApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = suger_sdk_python.UsageMeteringConfigInfo() # UsageMeteringConfigInfo | The usage metering config info to be updated

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

[APIKeyAuth](../README.md#APIKeyAuth)

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

