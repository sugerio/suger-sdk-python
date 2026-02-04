# OperationFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | [**List[OperationFilter]**](OperationFilter.md) | Args for logical operators (and, or) | [optional] 
**var_field** | [**TemporalWorkflowAttr**](TemporalWorkflowAttr.md) | Field is temporal workflow filter field | [optional] 
**operator** | **str** | Operator: \&quot;&#x3D;\&quot;, \&quot;!&#x3D;\&quot;, \&quot;in\&quot;, \&quot;not_in\&quot;, \&quot;and\&quot;, \&quot;or\&quot; | [optional] 
**value** | **object** | Value for single value operators (&#x3D;, !&#x3D;, etc) | [optional] 
**values** | **List[object]** | Values for array operators (in, not_in) | [optional] 

## Example

```python
from suger_sdk_python.models.operation_filter import OperationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OperationFilter from a JSON string
operation_filter_instance = OperationFilter.from_json(json)
# print the JSON string representation of the object
print(OperationFilter.to_json())

# convert the object into a dict
operation_filter_dict = operation_filter_instance.to_dict()
# create an instance of OperationFilter from a dict
operation_filter_from_dict = OperationFilter.from_dict(operation_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


