# DatabaseSqlNullBool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | **bool** |  | [optional] 
**valid** | **bool** | Valid is true if Bool is not NULL | [optional] 

## Example

```python
from suger_sdk_python.models.database_sql_null_bool import DatabaseSqlNullBool

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSqlNullBool from a JSON string
database_sql_null_bool_instance = DatabaseSqlNullBool.from_json(json)
# print the JSON string representation of the object
print(DatabaseSqlNullBool.to_json())

# convert the object into a dict
database_sql_null_bool_dict = database_sql_null_bool_instance.to_dict()
# create an instance of DatabaseSqlNullBool from a dict
database_sql_null_bool_from_dict = DatabaseSqlNullBool.from_dict(database_sql_null_bool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


