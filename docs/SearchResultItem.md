# SearchResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**tags** | [**List[GithubComSugerioMarketplaceServicePkgSearchTag]**](GithubComSugerioMarketplaceServicePkgSearchTag.md) | Tags provides structured tags for the search result | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.search_result_item import SearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultItem from a JSON string
search_result_item_instance = SearchResultItem.from_json(json)
# print the JSON string representation of the object
print(SearchResultItem.to_json())

# convert the object into a dict
search_result_item_dict = search_result_item_instance.to_dict()
# create an instance of SearchResultItem from a dict
search_result_item_from_dict = SearchResultItem.from_dict(search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


