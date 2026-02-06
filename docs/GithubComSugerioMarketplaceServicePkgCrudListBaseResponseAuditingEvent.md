# GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditingEvent]**](AuditingEvent.md) |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event import GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent from a JSON string
github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event_instance = GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event_dict = github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent from a dict
github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event_from_dict = GithubComSugerioMarketplaceServicePkgCrudListBaseResponseAuditingEvent.from_dict(github_com_sugerio_marketplace_service_pkg_crud_list_base_response_auditing_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


