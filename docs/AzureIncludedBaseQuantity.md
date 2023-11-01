# AzureIncludedBaseQuantity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_infinite** | **bool** |  | [optional] 
**quantity** | **float** |  | [optional] 
**recurring_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_included_base_quantity import AzureIncludedBaseQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of AzureIncludedBaseQuantity from a JSON string
azure_included_base_quantity_instance = AzureIncludedBaseQuantity.from_json(json)
# print the JSON string representation of the object
print AzureIncludedBaseQuantity.to_json()

# convert the object into a dict
azure_included_base_quantity_dict = azure_included_base_quantity_instance.to_dict()
# create an instance of AzureIncludedBaseQuantity from a dict
azure_included_base_quantity_form_dict = azure_included_base_quantity.from_dict(azure_included_base_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


