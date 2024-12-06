# TypesEntitlementValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolean_value** | **bool** | The BooleanValue field will be populated with a boolean value when the entitlement is a boolean type. Otherwise, the field will not be set. | [optional] 
**double_value** | **float** | The DoubleValue field will be populated with a double value when the entitlement is a double type. Otherwise, the field will not be set. | [optional] 
**integer_value** | **int** | The IntegerValue field will be populated with an integer value when the entitlement is an integer type. Otherwise, the field will not be set. | [optional] 
**string_value** | **str** | The StringValue field will be populated with a string value when the entitlement is a string type. Otherwise, the field will not be set. | [optional] 

## Example

```python
from suger_sdk_python.models.types_entitlement_value import TypesEntitlementValue

# TODO update the JSON string below
json = "{}"
# create an instance of TypesEntitlementValue from a JSON string
types_entitlement_value_instance = TypesEntitlementValue.from_json(json)
# print the JSON string representation of the object
print(TypesEntitlementValue.to_json())

# convert the object into a dict
types_entitlement_value_dict = types_entitlement_value_instance.to_dict()
# create an instance of TypesEntitlementValue from a dict
types_entitlement_value_from_dict = TypesEntitlementValue.from_dict(types_entitlement_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


