# GcpAmountUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nanos** | **int** |  | [optional] 
**units** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_amount_unit import GcpAmountUnit

# TODO update the JSON string below
json = "{}"
# create an instance of GcpAmountUnit from a JSON string
gcp_amount_unit_instance = GcpAmountUnit.from_json(json)
# print the JSON string representation of the object
print(GcpAmountUnit.to_json())

# convert the object into a dict
gcp_amount_unit_dict = gcp_amount_unit_instance.to_dict()
# create an instance of GcpAmountUnit from a dict
gcp_amount_unit_from_dict = GcpAmountUnit.from_dict(gcp_amount_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


