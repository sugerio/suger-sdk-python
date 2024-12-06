# AzureTypeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_type_value import AzureTypeValue

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTypeValue from a JSON string
azure_type_value_instance = AzureTypeValue.from_json(json)
# print the JSON string representation of the object
print(AzureTypeValue.to_json())

# convert the object into a dict
azure_type_value_dict = azure_type_value_instance.to_dict()
# create an instance of AzureTypeValue from a dict
azure_type_value_from_dict = AzureTypeValue.from_dict(azure_type_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


