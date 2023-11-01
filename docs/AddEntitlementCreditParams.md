# AddEntitlementCreditParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_amount_increment** | **float** | The amount to be added to the credit amount. | 
**entitlement_id** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from openapi_client.models.add_entitlement_credit_params import AddEntitlementCreditParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntitlementCreditParams from a JSON string
add_entitlement_credit_params_instance = AddEntitlementCreditParams.from_json(json)
# print the JSON string representation of the object
print AddEntitlementCreditParams.to_json()

# convert the object into a dict
add_entitlement_credit_params_dict = add_entitlement_credit_params_instance.to_dict()
# create an instance of AddEntitlementCreditParams from a dict
add_entitlement_credit_params_form_dict = add_entitlement_credit_params.from_dict(add_entitlement_credit_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


