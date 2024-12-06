# PriceModelBulk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_amount** | **float** | A currency amount to rate usage by | [optional] 
**bulk_size** | **int** | An integer amount to represent package size. For example, 1000 here would divide usage by 1000 before multiplying by package_amount in rating | [optional] 

## Example

```python
from suger_sdk_python.models.price_model_bulk import PriceModelBulk

# TODO update the JSON string below
json = "{}"
# create an instance of PriceModelBulk from a JSON string
price_model_bulk_instance = PriceModelBulk.from_json(json)
# print the JSON string representation of the object
print(PriceModelBulk.to_json())

# convert the object into a dict
price_model_bulk_dict = price_model_bulk_instance.to_dict()
# create an instance of PriceModelBulk from a dict
price_model_bulk_from_dict = PriceModelBulk.from_dict(price_model_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


