# UsageMeteringDimensionMappingValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convertion_multiplier** | **float** | The convertion multiplier when mapping to the DimensionKey. | [optional] 
**dimension_key** | **str** | The dimension key of the usage metering. | [optional] 

## Example

```python
from openapi_client.models.usage_metering_dimension_mapping_value import UsageMeteringDimensionMappingValue

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeteringDimensionMappingValue from a JSON string
usage_metering_dimension_mapping_value_instance = UsageMeteringDimensionMappingValue.from_json(json)
# print the JSON string representation of the object
print UsageMeteringDimensionMappingValue.to_json()

# convert the object into a dict
usage_metering_dimension_mapping_value_dict = usage_metering_dimension_mapping_value_instance.to_dict()
# create an instance of UsageMeteringDimensionMappingValue from a dict
usage_metering_dimension_mapping_value_form_dict = usage_metering_dimension_mapping_value.from_dict(usage_metering_dimension_mapping_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


