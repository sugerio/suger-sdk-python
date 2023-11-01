# AzurePricingUnit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_unlimited_unit** | **bool** |  | [optional] 
**lower_unit** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_type** | **str** |  | [optional] 
**upper_unit** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.azure_pricing_unit import AzurePricingUnit

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePricingUnit from a JSON string
azure_pricing_unit_instance = AzurePricingUnit.from_json(json)
# print the JSON string representation of the object
print AzurePricingUnit.to_json()

# convert the object into a dict
azure_pricing_unit_dict = azure_pricing_unit_instance.to_dict()
# create an instance of AzurePricingUnit from a dict
azure_pricing_unit_form_dict = azure_pricing_unit.from_dict(azure_pricing_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


