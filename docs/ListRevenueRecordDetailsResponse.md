# ListRevenueRecordDetailsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** |  | [optional] 
**revenue_record_details** | [**List[RevenueRecordDetail]**](RevenueRecordDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_revenue_record_details_response import ListRevenueRecordDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRevenueRecordDetailsResponse from a JSON string
list_revenue_record_details_response_instance = ListRevenueRecordDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ListRevenueRecordDetailsResponse.to_json()

# convert the object into a dict
list_revenue_record_details_response_dict = list_revenue_record_details_response_instance.to_dict()
# create an instance of ListRevenueRecordDetailsResponse from a dict
list_revenue_record_details_response_form_dict = list_revenue_record_details_response.from_dict(list_revenue_record_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


