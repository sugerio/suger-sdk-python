# DatabaseSqlNullString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** |  | [optional] 
**valid** | **bool** | Valid is true if String is not NULL | [optional] 

## Example

```python
from suger_sdk_python.models.database_sql_null_string import DatabaseSqlNullString

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSqlNullString from a JSON string
database_sql_null_string_instance = DatabaseSqlNullString.from_json(json)
# print the JSON string representation of the object
print(DatabaseSqlNullString.to_json())

# convert the object into a dict
database_sql_null_string_dict = database_sql_null_string_instance.to_dict()
# create an instance of DatabaseSqlNullString from a dict
database_sql_null_string_from_dict = DatabaseSqlNullString.from_dict(database_sql_null_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


