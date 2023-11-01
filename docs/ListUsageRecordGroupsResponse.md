# ListUsageRecordGroupsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** |  | [optional] 
**usage_record_groups** | [**List[MeteringUsageRecordGroup]**](MeteringUsageRecordGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_usage_record_groups_response import ListUsageRecordGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsageRecordGroupsResponse from a JSON string
list_usage_record_groups_response_instance = ListUsageRecordGroupsResponse.from_json(json)
# print the JSON string representation of the object
print ListUsageRecordGroupsResponse.to_json()

# convert the object into a dict
list_usage_record_groups_response_dict = list_usage_record_groups_response_instance.to_dict()
# create an instance of ListUsageRecordGroupsResponse from a dict
list_usage_record_groups_response_form_dict = list_usage_record_groups_response.from_dict(list_usage_record_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


