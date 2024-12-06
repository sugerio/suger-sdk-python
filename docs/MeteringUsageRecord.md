# MeteringUsageRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key is the unique identifier of a billable metric. | [optional] 
**properties** | **Dict[str, object]** | Properties is the filters of a billable metric. It should be equal to the filters of the billable metric. | [optional] 
**quantity** | **float** | The quantity (or numeric value) of a billable metric. | [optional] 

## Example

```python
from suger_sdk_python.models.metering_usage_record import MeteringUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecord from a JSON string
metering_usage_record_instance = MeteringUsageRecord.from_json(json)
# print the JSON string representation of the object
print(MeteringUsageRecord.to_json())

# convert the object into a dict
metering_usage_record_dict = metering_usage_record_instance.to_dict()
# create an instance of MeteringUsageRecord from a dict
metering_usage_record_from_dict = MeteringUsageRecord.from_dict(metering_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


