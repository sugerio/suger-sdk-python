# MeteringUsageRecordReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**entitlement_term_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**MeteringUsageRecordReportInfo**](MeteringUsageRecordReportInfo.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.metering_usage_record_report import MeteringUsageRecordReport

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecordReport from a JSON string
metering_usage_record_report_instance = MeteringUsageRecordReport.from_json(json)
# print the JSON string representation of the object
print(MeteringUsageRecordReport.to_json())

# convert the object into a dict
metering_usage_record_report_dict = metering_usage_record_report_instance.to_dict()
# create an instance of MeteringUsageRecordReport from a dict
metering_usage_record_report_from_dict = MeteringUsageRecordReport.from_dict(metering_usage_record_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


