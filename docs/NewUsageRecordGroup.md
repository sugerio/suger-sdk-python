# NewUsageRecordGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_id** | **str** |  | 
**meta_info** | [**MeteringUsageRecordGroupMetaInfo**](MeteringUsageRecordGroupMetaInfo.md) |  | [optional] 
**records** | **Dict[str, float]** |  | 
**timestamp** | **datetime** | The timestamp of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. This is not the timestamp of when the usage records were reported to Suger. | [optional] 

## Example

```python
from openapi_client.models.new_usage_record_group import NewUsageRecordGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NewUsageRecordGroup from a JSON string
new_usage_record_group_instance = NewUsageRecordGroup.from_json(json)
# print the JSON string representation of the object
print NewUsageRecordGroup.to_json()

# convert the object into a dict
new_usage_record_group_dict = new_usage_record_group_instance.to_dict()
# create an instance of NewUsageRecordGroup from a dict
new_usage_record_group_form_dict = new_usage_record_group.from_dict(new_usage_record_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


