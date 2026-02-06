# PkgHandlerValidateQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**matched_record_count** | **int** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from suger_sdk_python.models.pkg_handler_validate_query_response import PkgHandlerValidateQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PkgHandlerValidateQueryResponse from a JSON string
pkg_handler_validate_query_response_instance = PkgHandlerValidateQueryResponse.from_json(json)
# print the JSON string representation of the object
print(PkgHandlerValidateQueryResponse.to_json())

# convert the object into a dict
pkg_handler_validate_query_response_dict = pkg_handler_validate_query_response_instance.to_dict()
# create an instance of PkgHandlerValidateQueryResponse from a dict
pkg_handler_validate_query_response_from_dict = PkgHandlerValidateQueryResponse.from_dict(pkg_handler_validate_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


