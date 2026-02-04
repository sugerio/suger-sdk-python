# GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account_id** | **str** | AwsAccountId is the AWS account ID of the partner. | [optional] 
**id** | **str** | ID is the unique identifier for the partner connection. | [optional] 
**name** | **str** | Name is the display name of the partner. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result import GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult from a JSON string
github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result_instance = GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result_dict = github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult from a dict
github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result_from_dict = GithubComSugerioMarketplaceServicePkgStructsPartnerConnectionSearchResult.from_dict(github_com_sugerio_marketplace_service_pkg_structs_partner_connection_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


