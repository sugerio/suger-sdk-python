# OrbPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_metric** | [**OrbBillableMetric**](OrbBillableMetric.md) |  | [optional] 
**bps_config** | [**OrbPriceModelConfigBPS**](OrbPriceModelConfigBPS.md) |  | [optional] 
**bulk_bps_config** | [**OrbPriceModelConfigBULKBPS**](OrbPriceModelConfigBULKBPS.md) |  | [optional] 
**bulk_config** | [**OrbPriceModelConfigBULK**](OrbPriceModelConfigBULK.md) |  | [optional] 
**cadence** | [**OrbCadence**](OrbCadence.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**discount** | [**OrbPriceDiscount**](OrbPriceDiscount.md) |  | [optional] 
**fixed_price_quantity** | **int** | If the Price represents a fixed cost, this represents the quantity of units applied. Mutually exclusive with billable_metric. | [optional] 
**id** | **str** |  | [optional] 
**item** | [**OrbItem**](OrbItem.md) |  | [optional] 
**matrix_config** | [**OrbPriceModelConfigMATRIX**](OrbPriceModelConfigMATRIX.md) |  | [optional] 
**maximum** | [**OrbPriceMaximum**](OrbPriceMaximum.md) |  | [optional] 
**minimum** | [**OrbPriceMinimum**](OrbPriceMinimum.md) |  | [optional] 
**model_type** | [**OrbPriceModelType**](OrbPriceModelType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**package_config** | [**OrbPriceModelConfigPACKAGE**](OrbPriceModelConfigPACKAGE.md) |  | [optional] 
**plan_phase_order** | **int** | The phase order which includes this price, only applicable to a plan with phases. | [optional] 
**tiered_bps_config** | [**OrbPriceModelConfigTIEREDBPS**](OrbPriceModelConfigTIEREDBPS.md) |  | [optional] 
**tiered_config** | [**OrbPriceModelConfigTIERED**](OrbPriceModelConfigTIERED.md) |  | [optional] 
**unit_config** | [**OrbPriceModelConfigUNIT**](OrbPriceModelConfigUNIT.md) |  | [optional] 

## Example

```python
from openapi_client.models.orb_price import OrbPrice

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPrice from a JSON string
orb_price_instance = OrbPrice.from_json(json)
# print the JSON string representation of the object
print OrbPrice.to_json()

# convert the object into a dict
orb_price_dict = orb_price_instance.to_dict()
# create an instance of OrbPrice from a dict
orb_price_form_dict = orb_price.from_dict(orb_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


