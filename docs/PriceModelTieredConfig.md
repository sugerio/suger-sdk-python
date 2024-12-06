# PriceModelTieredConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_unit** | **float** | Inclusive tier starting value | [optional] 
**flat_fee** | **float** |  | [optional] 
**last_unit** | **float** | Exclusive tier ending value. If null, this is treated as the last tier | [optional] 
**unit_amount** | **float** | Amount per unit | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_tiered_config import PriceModelTieredConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelTieredConfig from a JSON string
price_model_tiered_config_instance = PriceModelTieredConfig.from_json(json)
# print the JSON string representation of the object
print(PriceModelTieredConfig.to_json())

# convert the object into a dict
price_model_tiered_config_dict = price_model_tiered_config_instance.to_dict()
# create an instance of PriceModelTieredConfig from a dict
price_model_tiered_config_from_dict = PriceModelTieredConfig.from_dict(price_model_tiered_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


