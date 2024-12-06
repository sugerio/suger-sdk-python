# PriceModelMatrix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_unit_amount** | **float** |  | [optional] 
**matrix** | [**List[PriceModelMatrixConfigGroup]**](PriceModelMatrixConfigGroup.md) | The matrix of the pricing model | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_matrix import PriceModelMatrix

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelMatrix from a JSON string
price_model_matrix_instance = PriceModelMatrix.from_json(json)
# print the JSON string representation of the object
print(PriceModelMatrix.to_json())

# convert the object into a dict
price_model_matrix_dict = price_model_matrix_instance.to_dict()
# create an instance of PriceModelMatrix from a dict
price_model_matrix_from_dict = PriceModelMatrix.from_dict(price_model_matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


