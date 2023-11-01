# openapi_client.ReportApi

All URIs are relative to *https://api.suger.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_revenue_report**](ReportApi.md#get_revenue_report) | **POST** /org/{orgId}/revenueReport | get revenue report
[**list_revenue_record_details**](ReportApi.md#list_revenue_record_details) | **GET** /org/{orgId}/partner/{partner}/revenueRecordDetail | list revenue record details
[**list_revenue_records**](ReportApi.md#list_revenue_records) | **GET** /org/{orgId}/partner/{partner}/revenueRecord | list revenue records
[**list_usage_metering_daily_records**](ReportApi.md#list_usage_metering_daily_records) | **GET** /org/{orgId}/partner/{partner}/usageMeteringDailyRecord | list usage metering daily records
[**list_usage_metering_daily_verifications**](ReportApi.md#list_usage_metering_daily_verifications) | **GET** /org/{orgId}/partner/{partner}/usageMeteringDailyVerification | list usage metering daily verifications


# **get_revenue_report**
> RevenueReport get_revenue_report(org_id, data)

get revenue report

Get the revenue report of the given organization, product, entitlement, or buyer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.get_revenue_report_params import GetRevenueReportParams
from openapi_client.models.revenue_report import RevenueReport
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
    api_instance = openapi_client.ReportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    data = openapi_client.GetRevenueReportParams() # GetRevenueReportParams | Get Revenue Report Params

    try:
        # get revenue report
        api_response = api_instance.get_revenue_report(org_id, data)
        print("The response of ReportApi->get_revenue_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->get_revenue_report: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **data** | [**GetRevenueReportParams**](GetRevenueReportParams.md)| Get Revenue Report Params | 

### Return type

[**RevenueReport**](RevenueReport.md)

### Authorization

[BearerTokenAuth](../README.md#BearerTokenAuth)

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

# **list_revenue_record_details**
> ListRevenueRecordDetailsResponse list_revenue_record_details(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list revenue record details

list the raw revenue record details for the given organization, product, entitlement, or buyer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_revenue_record_details_response import ListRevenueRecordDetailsResponse
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
    api_instance = openapi_client.ReportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner
    product_id = 'product_id_example' # str | Filter revenue record details by the given product ID (optional)
    entitlement_id = 'entitlement_id_example' # str | Filter revenue record details by the given entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | Filter revenue record details by the given buyer ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list revenue record details
        api_response = api_instance.list_revenue_record_details(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of ReportApi->list_revenue_record_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->list_revenue_record_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 
 **product_id** | **str**| Filter revenue record details by the given product ID | [optional] 
 **entitlement_id** | **str**| Filter revenue record details by the given entitlement ID | [optional] 
 **buyer_id** | **str**| Filter revenue record details by the given buyer ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListRevenueRecordDetailsResponse**](ListRevenueRecordDetailsResponse.md)

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

# **list_revenue_records**
> ListRevenueRecordsResponse list_revenue_records(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list revenue records

list the revenue records for the given organization, product, entitlement, or buyer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_revenue_records_response import ListRevenueRecordsResponse
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
    api_instance = openapi_client.ReportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner
    product_id = 'product_id_example' # str | Filter revenue record details by the given product ID (optional)
    entitlement_id = 'entitlement_id_example' # str | Filter revenue record details by the given entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | Filter revenue record details by the given buyer ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list revenue records
        api_response = api_instance.list_revenue_records(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of ReportApi->list_revenue_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->list_revenue_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 
 **product_id** | **str**| Filter revenue record details by the given product ID | [optional] 
 **entitlement_id** | **str**| Filter revenue record details by the given entitlement ID | [optional] 
 **buyer_id** | **str**| Filter revenue record details by the given buyer ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListRevenueRecordsResponse**](ListRevenueRecordsResponse.md)

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

# **list_usage_metering_daily_records**
> ListUsageMeteringDailyRecordsResponse list_usage_metering_daily_records(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usage metering daily records

list the daily records of the usage metering from the cloud marketplace for the given organization, product, entitlement, or buyer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_usage_metering_daily_records_response import ListUsageMeteringDailyRecordsResponse
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
    api_instance = openapi_client.ReportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner
    product_id = 'product_id_example' # str | Filter revenue record details by the given product ID (optional)
    entitlement_id = 'entitlement_id_example' # str | Filter revenue record details by the given entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | Filter revenue record details by the given buyer ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usage metering daily records
        api_response = api_instance.list_usage_metering_daily_records(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of ReportApi->list_usage_metering_daily_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->list_usage_metering_daily_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 
 **product_id** | **str**| Filter revenue record details by the given product ID | [optional] 
 **entitlement_id** | **str**| Filter revenue record details by the given entitlement ID | [optional] 
 **buyer_id** | **str**| Filter revenue record details by the given buyer ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageMeteringDailyRecordsResponse**](ListUsageMeteringDailyRecordsResponse.md)

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

# **list_usage_metering_daily_verifications**
> ListUsageMeteringDailyVerificationsResponse list_usage_metering_daily_verifications(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

list usage metering daily verifications

list the daily verifications between the usage records reported to cloud marketplace & the usage metering from the cloud marketplace for the given organization, product, entitlement, or buyer.

### Example

* Api Key Authentication (BearerTokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_usage_metering_daily_verifications_response import ListUsageMeteringDailyVerificationsResponse
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
    api_instance = openapi_client.ReportApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    partner = 'partner_example' # str | Cloud Partner
    product_id = 'product_id_example' # str | Filter usage metering daily verifications by the given product ID (optional)
    entitlement_id = 'entitlement_id_example' # str | Filter usage metering daily verifications by the given entitlement ID (optional)
    buyer_id = 'buyer_id_example' # str | Filter usage metering daily verifications by the given buyer ID (optional)
    start_date = 'start_date_example' # str | start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate (optional)
    end_date = 'end_date_example' # str | end date (UTC) in YYYY-MM-DD format, default is today (optional)
    limit = 56 # int | List pagination size, default 20, max value is 1000 (optional)
    offset = 56 # int | List pagination offset, default 0 (optional)

    try:
        # list usage metering daily verifications
        api_response = api_instance.list_usage_metering_daily_verifications(org_id, partner, product_id=product_id, entitlement_id=entitlement_id, buyer_id=buyer_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of ReportApi->list_usage_metering_daily_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->list_usage_metering_daily_verifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **partner** | **str**| Cloud Partner | 
 **product_id** | **str**| Filter usage metering daily verifications by the given product ID | [optional] 
 **entitlement_id** | **str**| Filter usage metering daily verifications by the given entitlement ID | [optional] 
 **buyer_id** | **str**| Filter usage metering daily verifications by the given buyer ID | [optional] 
 **start_date** | **str**| start date (UTC) in YYYY-MM-DD format, default is 30 days before the endDate | [optional] 
 **end_date** | **str**| end date (UTC) in YYYY-MM-DD format, default is today | [optional] 
 **limit** | **int**| List pagination size, default 20, max value is 1000 | [optional] 
 **offset** | **int**| List pagination offset, default 0 | [optional] 

### Return type

[**ListUsageMeteringDailyVerificationsResponse**](ListUsageMeteringDailyVerificationsResponse.md)

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

