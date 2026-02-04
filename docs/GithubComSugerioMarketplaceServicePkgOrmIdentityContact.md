# GithubComSugerioMarketplaceServicePkgOrmIdentityContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_contact_id** | **str** | CompanyContactID holds the value of the \&quot;company_contact_id\&quot; field. | [optional] 
**creation_time** | **datetime** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**email_address** | **str** | EmailAddress holds the value of the \&quot;email_address\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**IdentityConctactInfo**](IdentityConctactInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**last_update_time** | **datetime** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**tags** | **List[str]** | Tags holds the value of the \&quot;tags\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_identity_contact import GithubComSugerioMarketplaceServicePkgOrmIdentityContact

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmIdentityContact from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_identity_contact_instance = GithubComSugerioMarketplaceServicePkgOrmIdentityContact.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmIdentityContact.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_identity_contact_dict = github_com_sugerio_marketplace_service_pkg_orm_identity_contact_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmIdentityContact from a dict
github_com_sugerio_marketplace_service_pkg_orm_identity_contact_from_dict = GithubComSugerioMarketplaceServicePkgOrmIdentityContact.from_dict(github_com_sugerio_marketplace_service_pkg_orm_identity_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


