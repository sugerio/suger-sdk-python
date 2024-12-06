# PriceModelVolumeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat_fee** | **float** |  | [optional] 
**maximum_units** | **float** | Upper bound for this tier | [optional] 
**unit_amount** | **float** | Amount per unit | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_volume_config import PriceModelVolumeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelVolumeConfig from a JSON string
price_model_volume_config_instance = PriceModelVolumeConfig.from_json(json)
# print the JSON string representation of the object
print(PriceModelVolumeConfig.to_json())

# convert the object into a dict
price_model_volume_config_dict = price_model_volume_config_instance.to_dict()
# create an instance of PriceModelVolumeConfig from a dict
price_model_volume_config_from_dict = PriceModelVolumeConfig.from_dict(price_model_volume_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


