# OrbPriceMaximum


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to_price_ids** | **List[str]** | List of price_ids that this maximum amount applies to. For plan/plan phase maximums, this can be a subset of prices. | [optional] 
**maximum_amount** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.orb_price_maximum import OrbPriceMaximum

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPriceMaximum from a JSON string
orb_price_maximum_instance = OrbPriceMaximum.from_json(json)
# print the JSON string representation of the object
print OrbPriceMaximum.to_json()

# convert the object into a dict
orb_price_maximum_dict = orb_price_maximum_instance.to_dict()
# create an instance of OrbPriceMaximum from a dict
orb_price_maximum_form_dict = orb_price_maximum.from_dict(orb_price_maximum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


