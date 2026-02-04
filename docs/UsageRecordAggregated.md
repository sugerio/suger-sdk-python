# UsageRecordAggregated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**dimension_key** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.usage_record_aggregated import UsageRecordAggregated

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRecordAggregated from a JSON string
usage_record_aggregated_instance = UsageRecordAggregated.from_json(json)
# print the JSON string representation of the object
print(UsageRecordAggregated.to_json())

# convert the object into a dict
usage_record_aggregated_dict = usage_record_aggregated_instance.to_dict()
# create an instance of UsageRecordAggregated from a dict
usage_record_aggregated_from_dict = UsageRecordAggregated.from_dict(usage_record_aggregated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


