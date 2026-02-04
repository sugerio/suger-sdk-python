# GithubComSugerioMarketplaceServicePkgOrmGlobalCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City holds the value of the \&quot;city\&quot; field. | [optional] 
**contact_email** | **str** | ContactEmail holds the value of the \&quot;contact_email\&quot; field. | [optional] 
**country** | **str** | ISO 3166-1 alpha-3 country codes such as USA, JPN, CHN | [optional] 
**creation_time** | **str** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**domain** | **str** | Domain holds the value of the \&quot;domain\&quot; field. | [optional] 
**employee_count** | **int** | EmployeeCount holds the value of the \&quot;employee_count\&quot; field. | [optional] 
**founded_year** | **str** | Year founded (e.g. 2021) | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**industry** | **str** | Industry holds the value of the \&quot;industry\&quot; field. | [optional] 
**is_vendor** | **bool** | Indicates if this company is a vendor in the marketplace catalog | [optional] 
**last_update_time** | **str** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**linked_in** | **str** | The link to the linkedin profile | [optional] 
**meta_info** | [**CompanyMetaInfo**](CompanyMetaInfo.md) | Additional information about the company populated by Suger, such as partner engagement scores | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**partner_global_company_contact_ids** | **List[str]** | Array of unique global_company_contact.id values. Used to track partner contacts associated with this buyer company. | [optional] 
**postal_code** | **str** | PostalCode holds the value of the \&quot;postal_code\&quot; field. | [optional] 
**provider** | **str** | The data provider | [optional] 
**provider_company_id** | **str** | The external id from the provider | [optional] 
**s3_key_logo** | **str** | S3KeyLogo holds the value of the \&quot;s3_key_logo\&quot; field. | [optional] 
**s3_key_provider_data** | **str** | The normalized data from provider | [optional] 
**short_description** | **str** | ShortDescription holds the value of the \&quot;short_description\&quot; field. | [optional] 
**state_province** | **str** | State or province | [optional] 
**status** | **str** | active/stale/archived | [optional] 
**street** | **str** | Street holds the value of the \&quot;street\&quot; field. | [optional] 
**type** | **str** | Company type (e.g. Private, Public, Nonprofit, Franchise) | [optional] 
**website** | **str** | The main website | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_global_company import GithubComSugerioMarketplaceServicePkgOrmGlobalCompany

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmGlobalCompany from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_global_company_instance = GithubComSugerioMarketplaceServicePkgOrmGlobalCompany.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmGlobalCompany.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_global_company_dict = github_com_sugerio_marketplace_service_pkg_orm_global_company_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmGlobalCompany from a dict
github_com_sugerio_marketplace_service_pkg_orm_global_company_from_dict = GithubComSugerioMarketplaceServicePkgOrmGlobalCompany.from_dict(github_com_sugerio_marketplace_service_pkg_orm_global_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


