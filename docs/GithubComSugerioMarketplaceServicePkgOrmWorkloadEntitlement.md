# GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** | BuyerID holds the value of the \&quot;buyer_id\&quot; field. | [optional] 
**creation_time** | **datetime** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**end_time** | **datetime** | EndTime holds the value of the \&quot;end_time\&quot; field. | [optional] 
**entitlement_term_id** | **str** | EntitlementTermID holds the value of the \&quot;entitlement_term_id\&quot; field. | [optional] 
**external_buyer_id** | **str** | ExternalBuyerID holds the value of the \&quot;external_buyer_id\&quot; field. | [optional] 
**external_id** | **str** | ExternalID holds the value of the \&quot;external_id\&quot; field. | [optional] 
**external_product_id** | **str** | ExternalProductID holds the value of the \&quot;external_product_id\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**EntitlementInfo**](EntitlementInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**last_update_time** | **datetime** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**meta_info** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md) | MetaInfo holds the value of the \&quot;meta_info\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**offer_id** | **str** | OfferID holds the value of the \&quot;offer_id\&quot; field. | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**partner** | **str** | Partner holds the value of the \&quot;partner\&quot; field. | [optional] 
**partner_id** | **str** | PartnerID holds the value of the \&quot;partner_id\&quot; field. | [optional] 
**product_id** | **str** | ProductID holds the value of the \&quot;product_id\&quot; field. | [optional] 
**service** | **str** | Service holds the value of the \&quot;service\&quot; field. | [optional] 
**start_time** | **datetime** | StartTime holds the value of the \&quot;start_time\&quot; field. | [optional] 
**status** | **str** | Status holds the value of the \&quot;status\&quot; field. | [optional] 
**type** | **str** | Type holds the value of the \&quot;type\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_workload_entitlement import GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_workload_entitlement_instance = GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_workload_entitlement_dict = github_com_sugerio_marketplace_service_pkg_orm_workload_entitlement_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement from a dict
github_com_sugerio_marketplace_service_pkg_orm_workload_entitlement_from_dict = GithubComSugerioMarketplaceServicePkgOrmWorkloadEntitlement.from_dict(github_com_sugerio_marketplace_service_pkg_orm_workload_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


