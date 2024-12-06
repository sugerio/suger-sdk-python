# AzureValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**member_names** | **List[str]** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_validation_result import AzureValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AzureValidationResult from a JSON string
azure_validation_result_instance = AzureValidationResult.from_json(json)
# print the JSON string representation of the object
print(AzureValidationResult.to_json())

# convert the object into a dict
azure_validation_result_dict = azure_validation_result_instance.to_dict()
# create an instance of AzureValidationResult from a dict
azure_validation_result_from_dict = AzureValidationResult.from_dict(azure_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


