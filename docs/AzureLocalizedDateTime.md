# AzureLocalizedDateTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time_in_utc** | **str** |  | [optional] 
**localize_per_market** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.azure_localized_date_time import AzureLocalizedDateTime

# TODO update the JSON string below
json = "{}"
# create an instance of AzureLocalizedDateTime from a JSON string
azure_localized_date_time_instance = AzureLocalizedDateTime.from_json(json)
# print the JSON string representation of the object
print AzureLocalizedDateTime.to_json()

# convert the object into a dict
azure_localized_date_time_dict = azure_localized_date_time_instance.to_dict()
# create an instance of AzureLocalizedDateTime from a dict
azure_localized_date_time_form_dict = azure_localized_date_time.from_dict(azure_localized_date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


