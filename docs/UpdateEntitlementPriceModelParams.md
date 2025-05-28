# UpdateEntitlementPriceModelParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_time** | **str** |  | [optional] 
**billable_dimensions** | [**List[BillableDimension]**](BillableDimension.md) |  | [optional] 
**commits** | [**List[CommitDimension]**](CommitDimension.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.update_entitlement_price_model_params import UpdateEntitlementPriceModelParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntitlementPriceModelParams from a JSON string
update_entitlement_price_model_params_instance = UpdateEntitlementPriceModelParams.from_json(json)
# print the JSON string representation of the object
print(UpdateEntitlementPriceModelParams.to_json())

# convert the object into a dict
update_entitlement_price_model_params_dict = update_entitlement_price_model_params_instance.to_dict()
# create an instance of UpdateEntitlementPriceModelParams from a dict
update_entitlement_price_model_params_from_dict = UpdateEntitlementPriceModelParams.from_dict(update_entitlement_price_model_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


