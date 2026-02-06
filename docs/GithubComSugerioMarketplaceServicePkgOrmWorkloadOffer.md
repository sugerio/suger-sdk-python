# GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** | BuyerID holds the value of the \&quot;buyer_id\&quot; field. | [optional] 
**contact_ids** | **List[str]** | ContactIds holds the value of the \&quot;contact_ids\&quot; field. | [optional] 
**created_by** | **str** | CreatedBy holds the value of the \&quot;created_by\&quot; field. | [optional] 
**creation_time** | **datetime** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**end_time** | **datetime** | EndTime holds the value of the \&quot;end_time\&quot; field. | [optional] 
**expire_time** | **datetime** | ExpireTime holds the value of the \&quot;expire_time\&quot; field. | [optional] 
**external_id** | **str** | ExternalID holds the value of the \&quot;external_id\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**OfferInfo**](OfferInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**last_update_time** | **datetime** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**last_updated_by** | **str** | LastUpdatedBy holds the value of the \&quot;last_updated_by\&quot; field. | [optional] 
**meta_info** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md) | MetaInfo holds the value of the \&quot;meta_info\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**offer_type** | **str** | OfferType holds the value of the \&quot;offer_type\&quot; field. | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**partner** | **str** | Partner holds the value of the \&quot;partner\&quot; field. | [optional] 
**partner_id** | **str** | PartnerID holds the value of the \&quot;partner_id\&quot; field. | [optional] 
**product_id** | **str** | ProductID holds the value of the \&quot;product_id\&quot; field. | [optional] 
**service** | **str** | Service holds the value of the \&quot;service\&quot; field. | [optional] 
**status** | **str** | Status holds the value of the \&quot;status\&quot; field. | [optional] 
**sub_status** | **str** | SubStatus holds the value of the \&quot;sub_status\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_workload_offer import GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_workload_offer_instance = GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_workload_offer_dict = github_com_sugerio_marketplace_service_pkg_orm_workload_offer_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer from a dict
github_com_sugerio_marketplace_service_pkg_orm_workload_offer_from_dict = GithubComSugerioMarketplaceServicePkgOrmWorkloadOffer.from_dict(github_com_sugerio_marketplace_service_pkg_orm_workload_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


