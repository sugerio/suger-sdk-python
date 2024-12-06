# MeteringUsageRecordGroupByKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_bys_expression** | **str** | GroupBysExpression is string expression of array of group bys. | [optional] 
**id** | **str** | ID is billableMetric ID (Key) | [optional] 

## Example

```python
from suger_sdk_python.models.metering_usage_record_group_by_key import MeteringUsageRecordGroupByKey

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecordGroupByKey from a JSON string
metering_usage_record_group_by_key_instance = MeteringUsageRecordGroupByKey.from_json(json)
# print the JSON string representation of the object
print(MeteringUsageRecordGroupByKey.to_json())

# convert the object into a dict
metering_usage_record_group_by_key_dict = metering_usage_record_group_by_key_instance.to_dict()
# create an instance of MeteringUsageRecordGroupByKey from a dict
metering_usage_record_group_by_key_from_dict = MeteringUsageRecordGroupByKey.from_dict(metering_usage_record_group_by_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


