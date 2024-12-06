# DatabaseSqlNullTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**valid** | **bool** | Valid is true if Time is not NULL | [optional] 

## Example

```python
from suger_sdk_python.models.database_sql_null_time import DatabaseSqlNullTime

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSqlNullTime from a JSON string
database_sql_null_time_instance = DatabaseSqlNullTime.from_json(json)
# print the JSON string representation of the object
print(DatabaseSqlNullTime.to_json())

# convert the object into a dict
database_sql_null_time_dict = database_sql_null_time_instance.to_dict()
# create an instance of DatabaseSqlNullTime from a dict
database_sql_null_time_from_dict = DatabaseSqlNullTime.from_dict(database_sql_null_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


