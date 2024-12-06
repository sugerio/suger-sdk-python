# PriceModelTieredPercentage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiers** | [**List[PriceModelTieredPercentageConfig]**](PriceModelTieredPercentageConfig.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_tiered_percentage import PriceModelTieredPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelTieredPercentage from a JSON string
price_model_tiered_percentage_instance = PriceModelTieredPercentage.from_json(json)
# print the JSON string representation of the object
print(PriceModelTieredPercentage.to_json())

# convert the object into a dict
price_model_tiered_percentage_dict = price_model_tiered_percentage_instance.to_dict()
# create an instance of PriceModelTieredPercentage from a dict
price_model_tiered_percentage_from_dict = PriceModelTieredPercentage.from_dict(price_model_tiered_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


