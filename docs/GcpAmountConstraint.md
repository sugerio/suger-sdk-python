# GcpAmountConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_amount** | [**GcpAmountUnit**](GcpAmountUnit.md) |  | [optional] 
**max_amount** | [**GcpAmountUnit**](GcpAmountUnit.md) |  | [optional] 
**min_amount** | [**GcpAmountUnit**](GcpAmountUnit.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_amount_constraint import GcpAmountConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of GcpAmountConstraint from a JSON string
gcp_amount_constraint_instance = GcpAmountConstraint.from_json(json)
# print the JSON string representation of the object
print(GcpAmountConstraint.to_json())

# convert the object into a dict
gcp_amount_constraint_dict = gcp_amount_constraint_instance.to_dict()
# create an instance of GcpAmountConstraint from a dict
gcp_amount_constraint_from_dict = GcpAmountConstraint.from_dict(gcp_amount_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


