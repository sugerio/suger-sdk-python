# MeteringUsageRecordGroupMetaInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metronome_daily_cost_amount** | **float** | The metronome daily cost amount (in dollars) of the customer. | [optional] 
**origin_records** | **Dict[str, float]** | The original records reported by the customer before convertion. If no dimension mapping is applied, this field is the same as the records field. | [optional] 
**source** | [**UsageRecordGroupSource**](UsageRecordGroupSource.md) |  | [optional] 
**timestamp** | **datetime** | The timestamp (UTC)) of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. | [optional] 

## Example

```python
from openapi_client.models.metering_usage_record_group_meta_info import MeteringUsageRecordGroupMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecordGroupMetaInfo from a JSON string
metering_usage_record_group_meta_info_instance = MeteringUsageRecordGroupMetaInfo.from_json(json)
# print the JSON string representation of the object
print MeteringUsageRecordGroupMetaInfo.to_json()

# convert the object into a dict
metering_usage_record_group_meta_info_dict = metering_usage_record_group_meta_info_instance.to_dict()
# create an instance of MeteringUsageRecordGroupMetaInfo from a dict
metering_usage_record_group_meta_info_form_dict = metering_usage_record_group_meta_info.from_dict(metering_usage_record_group_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


