# PriceModelMatrixConfigGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[PriceModelMatrixProperty]**](PriceModelMatrixProperty.md) |  | [optional] 
**unit_amount** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_matrix_config_group import PriceModelMatrixConfigGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelMatrixConfigGroup from a JSON string
price_model_matrix_config_group_instance = PriceModelMatrixConfigGroup.from_json(json)
# print the JSON string representation of the object
print(PriceModelMatrixConfigGroup.to_json())

# convert the object into a dict
price_model_matrix_config_group_dict = price_model_matrix_config_group_instance.to_dict()
# create an instance of PriceModelMatrixConfigGroup from a dict
price_model_matrix_config_group_from_dict = PriceModelMatrixConfigGroup.from_dict(price_model_matrix_config_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


