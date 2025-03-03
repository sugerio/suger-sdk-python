# RevenueRecordDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_revenue_record_detail** | [**GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAwsBillingEvent**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAwsBillingEvent.md) | For AWS Marketplace | [optional] 
**azure_revenue_record_detail** | [**GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue.md) | For Azure Marketplace | [optional] 
**gcp_revenue_record_detail** | [**GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingGcpChargeUsage**](GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingGcpChargeUsage.md) | For GCP Marketplace | [optional] 

## Example

```python
from suger_sdk_python.models.revenue_record_detail import RevenueRecordDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueRecordDetail from a JSON string
revenue_record_detail_instance = RevenueRecordDetail.from_json(json)
# print the JSON string representation of the object
print(RevenueRecordDetail.to_json())

# convert the object into a dict
revenue_record_detail_dict = revenue_record_detail_instance.to_dict()
# create an instance of RevenueRecordDetail from a dict
revenue_record_detail_from_dict = RevenueRecordDetail.from_dict(revenue_record_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


