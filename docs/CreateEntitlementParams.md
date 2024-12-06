# CreateEntitlementParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**end_date** | **str** | The end date of the entitlement. If it is null, the entitlement will ends based on the offer. If it is in the past, the entitlement will be created as CANCELLED status. | [optional] 
**offer_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**start_date** | **str** | The start date of the entitlement. If it is null, the entitlement starts immediately. It can be in the future or in the past. | [optional] 

## Example

```python
from suger_sdk_python.models.create_entitlement_params import CreateEntitlementParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntitlementParams from a JSON string
create_entitlement_params_instance = CreateEntitlementParams.from_json(json)
# print the JSON string representation of the object
print(CreateEntitlementParams.to_json())

# convert the object into a dict
create_entitlement_params_dict = create_entitlement_params_instance.to_dict()
# create an instance of CreateEntitlementParams from a dict
create_entitlement_params_from_dict = CreateEntitlementParams.from_dict(create_entitlement_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


