# RevenueReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**report_date** | **datetime** |  | [optional] 
**report_type** | [**RevenueReportType**](RevenueReportType.md) |  | [optional] 
**revenue_records** | [**List[RevenueRecord]**](RevenueRecord.md) |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.revenue_report import RevenueReport

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueReport from a JSON string
revenue_report_instance = RevenueReport.from_json(json)
# print the JSON string representation of the object
print RevenueReport.to_json()

# convert the object into a dict
revenue_report_dict = revenue_report_instance.to_dict()
# create an instance of RevenueReport from a dict
revenue_report_form_dict = revenue_report.from_dict(revenue_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


