# PriceModelPercentage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat_fee** | **float** |  | [optional] 
**percentage_rate** | **float** | Basis point take rate per event | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_percentage import PriceModelPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelPercentage from a JSON string
price_model_percentage_instance = PriceModelPercentage.from_json(json)
# print the JSON string representation of the object
print(PriceModelPercentage.to_json())

# convert the object into a dict
price_model_percentage_dict = price_model_percentage_instance.to_dict()
# create an instance of PriceModelPercentage from a dict
price_model_percentage_from_dict = PriceModelPercentage.from_dict(price_model_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


