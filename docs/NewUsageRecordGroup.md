# NewUsageRecordGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_records** | [**List[MeteringUsageRecord]**](MeteringUsageRecord.md) | for usage metering API v2, don&#39;t use it together with the records v1. | [optional] 
**entitlement_id** | **str** |  | 
**meta_info** | [**MeteringUsageRecordGroupMetaInfo**](MeteringUsageRecordGroupMetaInfo.md) | read-only, don&#39;t set it when validating or reporting the usage record group. | [optional] 
**records** | **Dict[str, float]** | for usage metering API v1, don&#39;t use it together with the billableRecords v2. | 
**timestamp** | **datetime** | The timestamp of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. This is not the timestamp of when the usage records were reported to Suger. | [optional] 

## Example

```python
from suger_sdk_python.models.new_usage_record_group import NewUsageRecordGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NewUsageRecordGroup from a JSON string
new_usage_record_group_instance = NewUsageRecordGroup.from_json(json)
# print the JSON string representation of the object
print(NewUsageRecordGroup.to_json())

# convert the object into a dict
new_usage_record_group_dict = new_usage_record_group_instance.to_dict()
# create an instance of NewUsageRecordGroup from a dict
new_usage_record_group_from_dict = NewUsageRecordGroup.from_dict(new_usage_record_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


