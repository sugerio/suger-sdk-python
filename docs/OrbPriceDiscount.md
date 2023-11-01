# OrbPriceDiscount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_discount** | **str** | Only available if discount_type is amount. | [optional] 
**applies_to_price_ids** | **List[str]** |  | [optional] 
**discount_type** | [**OrbPriceDiscountType**](OrbPriceDiscountType.md) |  | [optional] 
**percentage_discount** | **float** | Only available if discount_type is percentage.This is a number between 0 and 1. | [optional] 
**trial_amount_discount** | **str** | Only available if discount_type is trial | [optional] 
**usage_discount** | **str** | Only available if discount_type is usage. Number of usage units that this discount is for | [optional] 

## Example

```python
from openapi_client.models.orb_price_discount import OrbPriceDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPriceDiscount from a JSON string
orb_price_discount_instance = OrbPriceDiscount.from_json(json)
# print the JSON string representation of the object
print OrbPriceDiscount.to_json()

# convert the object into a dict
orb_price_discount_dict = orb_price_discount_instance.to_dict()
# create an instance of OrbPriceDiscount from a dict
orb_price_discount_form_dict = orb_price_discount.from_dict(orb_price_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


