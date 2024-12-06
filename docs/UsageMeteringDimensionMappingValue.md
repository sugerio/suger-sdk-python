# UsageMeteringDimensionMappingValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convertion_multiplier** | **float** | The convertion multiplier when mapping from the source dimension key to the destination dimensionKey by quantity mode. Not required if the mapping mode is AMOUNT. | [optional] 
**dimension_key** | **str** | The destination dimension key of the usage metering mapping. | [optional] 
**mapping_mode** | [**UsageMeteringDimensionMappingMode**](UsageMeteringDimensionMappingMode.md) | The conversion mode of UsageMeteringDimensionMapping. The default is QUANTITY if not available. | [optional] 

## Example

```python
from suger_sdk_python.models.usage_metering_dimension_mapping_value import UsageMeteringDimensionMappingValue

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeteringDimensionMappingValue from a JSON string
usage_metering_dimension_mapping_value_instance = UsageMeteringDimensionMappingValue.from_json(json)
# print the JSON string representation of the object
print(UsageMeteringDimensionMappingValue.to_json())

# convert the object into a dict
usage_metering_dimension_mapping_value_dict = usage_metering_dimension_mapping_value_instance.to_dict()
# create an instance of UsageMeteringDimensionMappingValue from a dict
usage_metering_dimension_mapping_value_from_dict = UsageMeteringDimensionMappingValue.from_dict(usage_metering_dimension_mapping_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


