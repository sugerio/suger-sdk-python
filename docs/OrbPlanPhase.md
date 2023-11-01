# OrbPlanPhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**discount** | [**OrbPriceDiscount**](OrbPriceDiscount.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**duration_unit** | [**OrbCadence**](OrbCadence.md) |  | [optional] 
**maximum** | [**OrbPriceMaximum**](OrbPriceMaximum.md) |  | [optional] 
**minimum** | [**OrbPriceMinimum**](OrbPriceMinimum.md) |  | [optional] 
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.orb_plan_phase import OrbPlanPhase

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPlanPhase from a JSON string
orb_plan_phase_instance = OrbPlanPhase.from_json(json)
# print the JSON string representation of the object
print OrbPlanPhase.to_json()

# convert the object into a dict
orb_plan_phase_dict = orb_plan_phase_instance.to_dict()
# create an instance of OrbPlanPhase from a dict
orb_plan_phase_form_dict = orb_plan_phase.from_dict(orb_plan_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


