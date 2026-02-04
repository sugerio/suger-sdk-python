# GithubComSugerioMarketplaceServicePkgOrmProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | CreatedBy holds the value of the \&quot;created_by\&quot; field. | [optional] 
**creation_time** | **datetime** | CreationTime holds the value of the \&quot;creation_time\&quot; field. | [optional] 
**external_id** | **str** | ExternalID holds the value of the \&quot;external_id\&quot; field. | [optional] 
**fulfillment_url** | **str** | FulfillmentURL holds the value of the \&quot;fulfillment_url\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**info** | [**ProductInfo**](ProductInfo.md) | Info holds the value of the \&quot;info\&quot; field. | [optional] 
**last_update_time** | **datetime** | LastUpdateTime holds the value of the \&quot;last_update_time\&quot; field. | [optional] 
**last_updated_by** | **str** | LastUpdatedBy holds the value of the \&quot;last_updated_by\&quot; field. | [optional] 
**meta_info** | [**WorkloadMetaInfo**](WorkloadMetaInfo.md) | MetaInfo holds the value of the \&quot;meta_info\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**partner** | **str** | Partner holds the value of the \&quot;partner\&quot; field. | [optional] 
**partner_id** | **str** | PartnerID holds the value of the \&quot;partner_id\&quot; field. | [optional] 
**product_type** | [**GithubComSugerioMarketplaceServicePkgOrmProductProductType**](GithubComSugerioMarketplaceServicePkgOrmProductProductType.md) | ProductType holds the value of the \&quot;product_type\&quot; field. | [optional] 
**seller_id** | **str** | SellerID holds the value of the \&quot;seller_id\&quot; field. | [optional] 
**service** | **str** | Service holds the value of the \&quot;service\&quot; field. | [optional] 
**status** | **str** | Status holds the value of the \&quot;status\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_orm_product import GithubComSugerioMarketplaceServicePkgOrmProduct

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComSugerioMarketplaceServicePkgOrmProduct from a JSON string
github_com_sugerio_marketplace_service_pkg_orm_product_instance = GithubComSugerioMarketplaceServicePkgOrmProduct.from_json(json)
# print the JSON string representation of the object
print(GithubComSugerioMarketplaceServicePkgOrmProduct.to_json())

# convert the object into a dict
github_com_sugerio_marketplace_service_pkg_orm_product_dict = github_com_sugerio_marketplace_service_pkg_orm_product_instance.to_dict()
# create an instance of GithubComSugerioMarketplaceServicePkgOrmProduct from a dict
github_com_sugerio_marketplace_service_pkg_orm_product_from_dict = GithubComSugerioMarketplaceServicePkgOrmProduct.from_dict(github_com_sugerio_marketplace_service_pkg_orm_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


