# OrbPriceModelConfigMATRIX


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_unit_amount** | **str** |  | [optional] 
**dimensions** | **List[str]** | First and (optional) second dimension grouping keys | [optional] 
**matrix_values** | [**List[OrbMatrixPriceValue]**](OrbMatrixPriceValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.orb_price_model_config_matrix import OrbPriceModelConfigMATRIX

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPriceModelConfigMATRIX from a JSON string
orb_price_model_config_matrix_instance = OrbPriceModelConfigMATRIX.from_json(json)
# print the JSON string representation of the object
print OrbPriceModelConfigMATRIX.to_json()

# convert the object into a dict
orb_price_model_config_matrix_dict = orb_price_model_config_matrix_instance.to_dict()
# create an instance of OrbPriceModelConfigMATRIX from a dict
orb_price_model_config_matrix_form_dict = orb_price_model_config_matrix.from_dict(orb_price_model_config_matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


