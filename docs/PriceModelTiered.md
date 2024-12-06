# PriceModelTiered


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiers** | [**List[PriceModelTieredConfig]**](PriceModelTieredConfig.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_tiered import PriceModelTiered

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelTiered from a JSON string
price_model_tiered_instance = PriceModelTiered.from_json(json)
# print the JSON string representation of the object
print(PriceModelTiered.to_json())

# convert the object into a dict
price_model_tiered_dict = price_model_tiered_instance.to_dict()
# create an instance of PriceModelTiered from a dict
price_model_tiered_from_dict = PriceModelTiered.from_dict(price_model_tiered_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


