# UniqueCountAggregationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_items** | **Dict[str, object]** | Unique property values of current hour that are new of today. Leave the value as interface{} to save space. | [optional] 

## Example

```python
from suger_sdk_python.models.unique_count_aggregation_result import UniqueCountAggregationResult

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueCountAggregationResult from a JSON string
unique_count_aggregation_result_instance = UniqueCountAggregationResult.from_json(json)
# print the JSON string representation of the object
print(UniqueCountAggregationResult.to_json())

# convert the object into a dict
unique_count_aggregation_result_dict = unique_count_aggregation_result_instance.to_dict()
# create an instance of UniqueCountAggregationResult from a dict
unique_count_aggregation_result_from_dict = UniqueCountAggregationResult.from_dict(unique_count_aggregation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


