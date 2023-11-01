# OrbPriceTier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bps** | **float** |  | [optional] 
**first_unit** | **str** | The following fields applicable only to UNIT price model | [optional] 
**last_unit** | **str** |  | [optional] 
**maximum_amount** | **str** |  | [optional] 
**maximum_units** | **float** | The following fields applicable only to BULK price model | [optional] 
**minimum_amount** | **str** | The following fields applicable only to BPS price model | [optional] 
**per_unit_maximum** | **str** |  | [optional] 
**unit_amount** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.orb_price_tier import OrbPriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPriceTier from a JSON string
orb_price_tier_instance = OrbPriceTier.from_json(json)
# print the JSON string representation of the object
print OrbPriceTier.to_json()

# convert the object into a dict
orb_price_tier_dict = orb_price_tier_instance.to_dict()
# create an instance of OrbPriceTier from a dict
orb_price_tier_form_dict = orb_price_tier.from_dict(orb_price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


