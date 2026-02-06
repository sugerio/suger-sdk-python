# ListOperationsV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**OperationFilter**](OperationFilter.md) | Filter expression for querying workflows. Supports nested logical operators (and/or) and comparison operators (&#x3D;, !&#x3D;, in, not_in). Example: {\&quot;operator\&quot;: \&quot;and\&quot;, \&quot;args\&quot;: [{\&quot;operator\&quot;: \&quot;&#x3D;\&quot;, \&quot;field\&quot;: \&quot;SugerService\&quot;, \&quot;value\&quot;: \&quot;Marketplace\&quot;}, {\&quot;operator\&quot;: \&quot;&#x3D;\&quot;, \&quot;field\&quot;: \&quot;SugerPartner\&quot;, \&quot;value\&quot;: \&quot;AWS\&quot;}]} | [optional] 
**limit** | **int** | Limit the number of results returned (1-100), default 100 | [optional] 
**offset_token** | **str** | OffsetToken for pagination, use nextOffsetToken from previous response | [optional] 

## Example

```python
from suger_sdk_python.models.list_operations_v2_request import ListOperationsV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of ListOperationsV2Request from a JSON string
list_operations_v2_request_instance = ListOperationsV2Request.from_json(json)
# print the JSON string representation of the object
print(ListOperationsV2Request.to_json())

# convert the object into a dict
list_operations_v2_request_dict = list_operations_v2_request_instance.to_dict()
# create an instance of ListOperationsV2Request from a dict
list_operations_v2_request_from_dict = ListOperationsV2Request.from_dict(list_operations_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


