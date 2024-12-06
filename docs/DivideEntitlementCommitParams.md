# DivideEntitlementCommitParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_amount** | **float** | The amount of the commit to be divided. If it is less or equal to 0.0, the total commit of the entitlement will be divided into multiple sub entitlement terms with credit. | [optional] 
**start_dates** | **List[datetime]** | The start dates of the sub entitlement terms. The end date of the last sub entitlement term is the end date of the parent entitlement term. The first start date must be the same as the start date of the parent entitlement term. | [optional] 

## Example

```python
from suger_sdk_python.models.divide_entitlement_commit_params import DivideEntitlementCommitParams

# TODO update the JSON string below
json = "{}"
# create an instance of DivideEntitlementCommitParams from a JSON string
divide_entitlement_commit_params_instance = DivideEntitlementCommitParams.from_json(json)
# print the JSON string representation of the object
print(DivideEntitlementCommitParams.to_json())

# convert the object into a dict
divide_entitlement_commit_params_dict = divide_entitlement_commit_params_instance.to_dict()
# create an instance of DivideEntitlementCommitParams from a dict
divide_entitlement_commit_params_from_dict = DivideEntitlementCommitParams.from_dict(divide_entitlement_commit_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


