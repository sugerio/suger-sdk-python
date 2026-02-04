# GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | CompanyID holds the value of the \&quot;company_id\&quot; field. | [optional] 
**contact_ids** | **List[str]** | ContactIds holds the value of the \&quot;contact_ids\&quot; field. | [optional] 
**creation_time** | **datetime** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**description** | **str** | Description holds the value of the \&quot;description\&quot; field. | [optional] 
**external_id** | **str** | ExternalID holds the value of the \&quot;external_id\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**BuyerInfo**](BuyerInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**last_update_time** | **datetime** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**partner** | **str** | Partner holds the value of the \&quot;partner\&quot; field. | [optional] 
**s3_key_logo** | **str** | S3KeyLogo holds the value of the \&quot;s3_key_logo\&quot; field. | [optional] 
**tags** | **List[str]** | Tags holds the value of the \&quot;tags\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_identity_buyer import GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_identity_buyer_instance = GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_identity_buyer_dict = github_com_sugerio_marketplace_service_pkg_orm_identity_buyer_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer from a dict
github_com_sugerio_marketplace_service_pkg_orm_identity_buyer_from_dict = GithubComSugerioMarketplaceServicePkgOrmIdentityBuyer.from_dict(github_com_sugerio_marketplace_service_pkg_orm_identity_buyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


