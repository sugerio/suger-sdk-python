# SqlCondition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | The column name. | [optional] 
**operator** | [**SqlOperator**](SqlOperator.md) |  | [optional] 
**value** | **object** | The value. | [optional] 
**value_type** | [**SqlValueType**](SqlValueType.md) |  | [optional] 

## Example

```python
from openapi_client.models.sql_condition import SqlCondition

# TODO update the JSON string below
json = "{}"
# create an instance of SqlCondition from a JSON string
sql_condition_instance = SqlCondition.from_json(json)
# print the JSON string representation of the object
print SqlCondition.to_json()

# convert the object into a dict
sql_condition_dict = sql_condition_instance.to_dict()
# create an instance of SqlCondition from a dict
sql_condition_form_dict = sql_condition.from_dict(sql_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


