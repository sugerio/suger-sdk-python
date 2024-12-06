# AddEntitlementCreditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_amount_increment** | **float** | The amount to be added to the credit amount. | [optional] 
**entitlement_id** | **str** |  | [optional] 
**entitlement_term_id** | **str** |  | [optional] 
**new_credit_amount** | **float** | The new credit amount after the increment. | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.add_entitlement_credit_response import AddEntitlementCreditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntitlementCreditResponse from a JSON string
add_entitlement_credit_response_instance = AddEntitlementCreditResponse.from_json(json)
# print the JSON string representation of the object
print(AddEntitlementCreditResponse.to_json())

# convert the object into a dict
add_entitlement_credit_response_dict = add_entitlement_credit_response_instance.to_dict()
# create an instance of AddEntitlementCreditResponse from a dict
add_entitlement_credit_response_from_dict = AddEntitlementCreditResponse.from_dict(add_entitlement_credit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


