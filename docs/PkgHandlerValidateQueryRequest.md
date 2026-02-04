# PkgHandlerValidateQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_query** | **str** |  | 
**record_type** | **str** |  | 

## Example

```python
from suger_sdk_python.models.pkg_handler_validate_query_request import PkgHandlerValidateQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PkgHandlerValidateQueryRequest from a JSON string
pkg_handler_validate_query_request_instance = PkgHandlerValidateQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PkgHandlerValidateQueryRequest.to_json())

# convert the object into a dict
pkg_handler_validate_query_request_dict = pkg_handler_validate_query_request_instance.to_dict()
# create an instance of PkgHandlerValidateQueryRequest from a dict
pkg_handler_validate_query_request_from_dict = PkgHandlerValidateQueryRequest.from_dict(pkg_handler_validate_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


