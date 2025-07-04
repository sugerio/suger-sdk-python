# RevenueRecordInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_revenue_records** | [**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAwsBillingEvent]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAwsBillingEvent.md) | For raw revenue records in AWS Marketplace | [optional] 
**azure_revenue_records** | [**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue.md) | For raw revenue records in Azure Marketplace | [optional] 
**bank_trace_id** | **str** | The bank trace ID of the revenue record if applicable | [optional] 
**billing_model** | [**RevenueBillingModel**](RevenueBillingModel.md) | The billing model of the revenue record if applicable The value is one of the following: - SubscriptionBased: The revenue record is from a subscription or recurring commitment. - UsageBased: The revenue record is from a usage-based metering. | [optional] 
**channel** | [**RevenueChannel**](RevenueChannel.md) | The channel of revenue record. | [optional] 
**credit_amount** | **float** | The credit amount used in the revenue record. | [optional] 
**disbursement_billing_event_id** | **str** | The disbursement ID of the revenue record if applicable | [optional] 
**disbursement_notification_sent** | **bool** | Whether the disbursement notification has been sent to the seller/ISV. | [optional] 
**earning_id** | **str** | The earning ID of the revenue record if applicable | [optional] 
**gcp_revenue_records** | [**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingGcpChargeUsage]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingGcpChargeUsage.md) | For raw revenue records in GCP Marketplace | [optional] 
**id_source** | **str** | Source of the revenue record ID. | [optional] 
**invoice_id** | **str** | The invoice ID of the revenue record if applicable | [optional] 
**payment_id** | **str** | The payment  ID of the revenue record if applicable | [optional] 
**reseller_id** | **str** | The reseller ID of the revenue record if applicable | [optional] 
**reseller_name** | **str** | The reseller name of the revenue record if application | [optional] 
**resource** | **str** | Resource name for the revenue record. Applicable only to GCP Marketplace. | [optional] 

## Example

```python
from suger_sdk_python.models.revenue_record_info import RevenueRecordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueRecordInfo from a JSON string
revenue_record_info_instance = RevenueRecordInfo.from_json(json)
# print the JSON string representation of the object
print(RevenueRecordInfo.to_json())

# convert the object into a dict
revenue_record_info_dict = revenue_record_info_instance.to_dict()
# create an instance of RevenueRecordInfo from a dict
revenue_record_info_from_dict = RevenueRecordInfo.from_dict(revenue_record_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


