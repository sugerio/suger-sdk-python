# PriceModelVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiers** | [**List[PriceModelVolumeConfig]**](PriceModelVolumeConfig.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_volume import PriceModelVolume

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelVolume from a JSON string
price_model_volume_instance = PriceModelVolume.from_json(json)
# print the JSON string representation of the object
print(PriceModelVolume.to_json())

# convert the object into a dict
price_model_volume_dict = price_model_volume_instance.to_dict()
# create an instance of PriceModelVolume from a dict
price_model_volume_from_dict = PriceModelVolume.from_dict(price_model_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


