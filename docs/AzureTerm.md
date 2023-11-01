# AzureTerm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_duration** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**term_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_term import AzureTerm

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTerm from a JSON string
azure_term_instance = AzureTerm.from_json(json)
# print the JSON string representation of the object
print AzureTerm.to_json()

# convert the object into a dict
azure_term_dict = azure_term_instance.to_dict()
# create an instance of AzureTerm from a dict
azure_term_form_dict = azure_term.from_dict(azure_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


