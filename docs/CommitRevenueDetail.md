# CommitRevenueDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The total amount of the commit revenue. | [optional] 
**description** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**quantity** | **int** | The quantity of the commit dimension. Default is 1. | [optional] 
**rate** | **float** | The unit price of the commit dimension. | [optional] 

## Example

```python
from suger_sdk_python.models.commit_revenue_detail import CommitRevenueDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CommitRevenueDetail from a JSON string
commit_revenue_detail_instance = CommitRevenueDetail.from_json(json)
# print the JSON string representation of the object
print(CommitRevenueDetail.to_json())

# convert the object into a dict
commit_revenue_detail_dict = commit_revenue_detail_instance.to_dict()
# create an instance of CommitRevenueDetail from a dict
commit_revenue_detail_from_dict = CommitRevenueDetail.from_dict(commit_revenue_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


