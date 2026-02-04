# GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Categories holds the value of the \&quot;categories\&quot; field. | [optional] 
**company_description** | **str** | CompanyDescription holds the value of the \&quot;company_description\&quot; field. | [optional] 
**company_domain** | **str** | CompanyDomain holds the value of the \&quot;company_domain\&quot; field. | [optional] 
**company_id** | **str** | Reference to Company.id where is_vendor&#x3D;true | [optional] 
**company_name** | **str** | CompanyName holds the value of the \&quot;company_name\&quot; field. | [optional] 
**creation_time** | **str** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**delivery_method** | **str** | DeliveryMethod holds the value of the \&quot;delivery_method\&quot; field. | [optional] 
**has_free_trial** | **bool** | HasFreeTrial holds the value of the \&quot;has_free_trial\&quot; field. | [optional] 
**has_usage_metering** | **bool** | HasUsageMetering holds the value of the \&quot;has_usage_metering\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**GithubComSugerioMarketplaceServicePkgStructsMarketplaceListingInfo**](GithubComSugerioMarketplaceServicePkgStructsMarketplaceListingInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**last_update_time** | **str** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**link** | **str** | Link holds the value of the \&quot;link\&quot; field. | [optional] 
**listing_id** | **str** | ListingID holds the value of the \&quot;listing_id\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**partner** | **str** | Partner holds the value of the \&quot;partner\&quot; field. | [optional] 
**review_count** | **int** | ReviewCount holds the value of the \&quot;review_count\&quot; field. | [optional] 
**review_score** | **float** | ReviewScore holds the value of the \&quot;review_score\&quot; field. | [optional] 
**short_description** | **str** | ShortDescription holds the value of the \&quot;short_description\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing import GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing_instance = GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing_dict = github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing from a dict
github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing_from_dict = GithubComSugerioMarketplaceServicePkgOrmMarketplaceListing.from_dict(github_com_sugerio_marketplace_service_pkg_orm_marketplace_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


