# CommitDimension

The commit dimension. There may be one or more commit dimensions defined in single product, offer or entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_user_created** | **bool** | Whether this commit dimension is newly created by user, when creating AWS Marketplace Contract private offer. | [optional] 
**key** | **str** | API name of the dimension | [optional] 
**length** | **int** | The term length for the commit amount, such as 6 months, or 1 year. The length is used together with timeUnit. If the length is zero, use the TermEndTime. | [optional] 
**maximum_users** | **int** | The maximum number of users for PER_USER commit | [optional] 
**minimum_users** | **int** | The minimum number of users for PER_USER commit | [optional] 
**name** | **str** | Display name of the dimension | [optional] 
**quantity** | **int** | The quantity of this commit. | [optional] 
**rate** | **float** | The commit amount. For GCP, it is monthly commitment. | [optional] 
**term** | **str** | The term of the commit amount. It is used for front-end display only. | [optional] 
**term_end_time** | **str** | The end time of the commit term. | [optional] 
**time_unit** | [**TimeUnit**](TimeUnit.md) | The term unit for the commit amount. | [optional] 
**type** | [**CommitDimensionType**](CommitDimensionType.md) | The type of the commit dimension. Applicable only to Azure Marketplace. | [optional] 
**types** | **List[str]** | These indicate whether the dimension covers metering, entitlement, or support for external metering | [optional] 

## Example

```python
from suger_sdk_python.models.commit_dimension import CommitDimension

# TODO update the JSON string below
json = "{}"
# create an instance of CommitDimension from a JSON string
commit_dimension_instance = CommitDimension.from_json(json)
# print the JSON string representation of the object
print(CommitDimension.to_json())

# convert the object into a dict
commit_dimension_dict = commit_dimension_instance.to_dict()
# create an instance of CommitDimension from a dict
commit_dimension_from_dict = CommitDimension.from_dict(commit_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


