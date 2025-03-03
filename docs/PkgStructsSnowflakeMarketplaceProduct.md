# PkgStructsSnowflakeMarketplaceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**created_on** | [**DatabaseSqlNullTime**](DatabaseSqlNullTime.md) |  | [optional] 
**detailed_target_accounts** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**distribution** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**global_name** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**is_application** | [**DatabaseSqlNullBool**](DatabaseSqlNullBool.md) |  | [optional] 
**is_by_request** | [**DatabaseSqlNullBool**](DatabaseSqlNullBool.md) |  | [optional] 
**is_limited_trial** | [**DatabaseSqlNullBool**](DatabaseSqlNullBool.md) |  | [optional] 
**is_monetized** | [**DatabaseSqlNullBool**](DatabaseSqlNullBool.md) |  | [optional] 
**is_mountless_queryable** | [**DatabaseSqlNullBool**](DatabaseSqlNullBool.md) |  | [optional] 
**is_targeted** | [**DatabaseSqlNullBool**](DatabaseSqlNullBool.md) |  | [optional] 
**owner** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**owner_role_type** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**profile** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**published_on** | [**DatabaseSqlNullTime**](DatabaseSqlNullTime.md) |  | [optional] 
**regions** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**rejected_on** | [**DatabaseSqlNullTime**](DatabaseSqlNullTime.md) |  | [optional] 
**review_state** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**state** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**subtitle** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**target_accounts** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**title** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**uniform_listing_locator** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**updated_on** | [**DatabaseSqlNullTime**](DatabaseSqlNullTime.md) |  | [optional] 
**name** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 
**organization_profile_name** | [**DatabaseSqlNullString**](DatabaseSqlNullString.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.pkg_structs_snowflake_marketplace_product import PkgStructsSnowflakeMarketplaceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of PkgStructsSnowflakeMarketplaceProduct from a JSON string
pkg_structs_snowflake_marketplace_product_instance = PkgStructsSnowflakeMarketplaceProduct.from_json(json)
# print the JSON string representation of the object
print(PkgStructsSnowflakeMarketplaceProduct.to_json())

# convert the object into a dict
pkg_structs_snowflake_marketplace_product_dict = pkg_structs_snowflake_marketplace_product_instance.to_dict()
# create an instance of PkgStructsSnowflakeMarketplaceProduct from a dict
pkg_structs_snowflake_marketplace_product_from_dict = PkgStructsSnowflakeMarketplaceProduct.from_dict(pkg_structs_snowflake_marketplace_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


