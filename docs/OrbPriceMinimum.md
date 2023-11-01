# OrbPriceMinimum


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to_price_ids** | **List[str]** | List of price_ids that this minimum amount applies to. For plan/plan phase minimums, this can be a subset of prices. | [optional] 
**minimum_amount** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.orb_price_minimum import OrbPriceMinimum

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPriceMinimum from a JSON string
orb_price_minimum_instance = OrbPriceMinimum.from_json(json)
# print the JSON string representation of the object
print OrbPriceMinimum.to_json()

# convert the object into a dict
orb_price_minimum_dict = orb_price_minimum_instance.to_dict()
# create an instance of OrbPriceMinimum from a dict
orb_price_minimum_form_dict = orb_price_minimum.from_dict(orb_price_minimum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


