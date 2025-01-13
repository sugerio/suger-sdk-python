# MeteringUsageRecordGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**meta_info** | [**MeteringUsageRecordGroupMetaInfo**](MeteringUsageRecordGroupMetaInfo.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 
**records** | **Dict[str, float]** |  | [optional] 
**reported_time** | **datetime** | nullable | [optional] 
**serial_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**usage_record_report_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.metering_usage_record_group import MeteringUsageRecordGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecordGroup from a JSON string
metering_usage_record_group_instance = MeteringUsageRecordGroup.from_json(json)
# print the JSON string representation of the object
print(MeteringUsageRecordGroup.to_json())

# convert the object into a dict
metering_usage_record_group_dict = metering_usage_record_group_instance.to_dict()
# create an instance of MeteringUsageRecordGroup from a dict
metering_usage_record_group_from_dict = MeteringUsageRecordGroup.from_dict(metering_usage_record_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


