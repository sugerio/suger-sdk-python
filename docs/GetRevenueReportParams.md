# GetRevenueReportParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** | Optional, if available, return the report for the Buyer. | [optional] 
**entitlement_id** | **str** | Optional, if available, return the report for the Entitlement. | [optional] 
**organization_id** | **str** | Required. If the productID &amp; entitlementID are emtpy, return the report for the entire Organization. | 
**partner** | **str** |  | 
**product_id** | **str** | Optional, if available, return the report for the Product. | [optional] 
**report_type** | [**RevenueReportType**](RevenueReportType.md) |  | 
**service** | **str** |  | 

## Example

```python
from suger_sdk_python.models.get_revenue_report_params import GetRevenueReportParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetRevenueReportParams from a JSON string
get_revenue_report_params_instance = GetRevenueReportParams.from_json(json)
# print the JSON string representation of the object
print(GetRevenueReportParams.to_json())

# convert the object into a dict
get_revenue_report_params_dict = get_revenue_report_params_instance.to_dict()
# create an instance of GetRevenueReportParams from a dict
get_revenue_report_params_from_dict = GetRevenueReportParams.from_dict(get_revenue_report_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


