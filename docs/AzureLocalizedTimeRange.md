# AzureLocalizedTimeRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_at** | [**AzureLocalizedDateTime**](AzureLocalizedDateTime.md) |  | [optional] 
**start_at** | [**AzureLocalizedDateTime**](AzureLocalizedDateTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_localized_time_range import AzureLocalizedTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of AzureLocalizedTimeRange from a JSON string
azure_localized_time_range_instance = AzureLocalizedTimeRange.from_json(json)
# print the JSON string representation of the object
print AzureLocalizedTimeRange.to_json()

# convert the object into a dict
azure_localized_time_range_dict = azure_localized_time_range_instance.to_dict()
# create an instance of AzureLocalizedTimeRange from a dict
azure_localized_time_range_form_dict = azure_localized_time_range.from_dict(azure_localized_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


