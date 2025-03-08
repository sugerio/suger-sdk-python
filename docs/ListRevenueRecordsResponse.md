# ListRevenueRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** |  | [optional] 
**revenue_records** | [**List[RevenueRecord]**](RevenueRecord.md) | list of revenue records. | [optional] 

## Example

```python
from suger_sdk_python.models.list_revenue_records_response import ListRevenueRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRevenueRecordsResponse from a JSON string
list_revenue_records_response_instance = ListRevenueRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(ListRevenueRecordsResponse.to_json())

# convert the object into a dict
list_revenue_records_response_dict = list_revenue_records_response_instance.to_dict()
# create an instance of ListRevenueRecordsResponse from a dict
list_revenue_records_response_from_dict = ListRevenueRecordsResponse.from_dict(list_revenue_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


