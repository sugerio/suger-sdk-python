# GithubComSugerioMarketplaceServicePkgSearchTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | API key for programmatic access (e.g., \&quot;partner\&quot;, \&quot;start_date\&quot;) | [optional] 
**title** | **str** | Display title (e.g., \&quot;Partner\&quot;, \&quot;Start Date\&quot;) | [optional] 
**type** | [**GithubComSugerioMarketplaceServicePkgSearchTagType**](GithubComSugerioMarketplaceServicePkgSearchTagType.md) | Strongly-typed tag type | [optional] 
**value** | **object** | Actual value (string, number, date, etc.) | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_search_tag import GithubComSugerioMarketplaceServicePkgSearchTag

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgSearchTag from a JSON string
github_com_sugerio_marketplace_service_pkg_search_tag_instance = GithubComSugerioMarketplaceServicePkgSearchTag.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgSearchTag.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_search_tag_dict = github_com_sugerio_marketplace_service_pkg_search_tag_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgSearchTag from a dict
github_com_sugerio_marketplace_service_pkg_search_tag_from_dict = GithubComSugerioMarketplaceServicePkgSearchTag.from_dict(github_com_sugerio_marketplace_service_pkg_search_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


