# RevenueRecordInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_revenue_records** | [**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAwsBillingEvent]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAwsBillingEvent.md) | For raw revenue records in AWS Marketplace | [optional] 
**azure_revenue_records** | [**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue.md) | For raw revenue records in Azure Marketplace | [optional] 
**credit_amount** | **float** | The credit amount used in the revenue record. | [optional] 
**disbursement_notification_sent** | **bool** | Whether the disbursement notification has been sent to the seller/ISV. | [optional] 
**gcp_revenue_records** | [**List[GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingGcpChargeUsage]**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingGcpChargeUsage.md) | For raw revenue records in GCP Marketplace | [optional] 
**id_source** | **str** | Source of the revenue record ID. | [optional] 
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


