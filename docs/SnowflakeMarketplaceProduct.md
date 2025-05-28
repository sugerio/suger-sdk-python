# SnowflakeMarketplaceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_regions** | **str** |  | [optional] 
**application_package_name** | **str** |  | [optional] 
**attached_share** | **str** |  | [optional] 
**autofulfillment** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**customized_contact_info** | **str** |  | [optional] 
**default_pricing_plan** | [**SnowflakeMarketplaceProductDefaultPricingPlan**](SnowflakeMarketplaceProductDefaultPricingPlan.md) |  | [optional] 
**detailed_target_accounts** | [**List[SnowflakeMarketplaceProductDetailedTargetAccount]**](SnowflakeMarketplaceProductDetailedTargetAccount.md) |  | [optional] 
**distribution** | **str** |  | [optional] 
**evaluation_plan** | **str** |  | [optional] 
**first_published_on** | **str** |  | [optional] 
**flags** | **str** |  | [optional] 
**fulfillment_type** | **str** |  | [optional] 
**global_name** | **str** |  | [optional] 
**is_mountless_queryable** | **bool** |  | [optional] 
**last_approved_on** | **str** |  | [optional] 
**last_published_on** | **str** |  | [optional] 
**last_submitted_on** | **str** |  | [optional] 
**listing_type** | **str** |  | [optional] 
**metadata** | [**SnowflakeMarketplaceProductMetadata**](SnowflakeMarketplaceProductMetadata.md) |  | [optional] 
**name** | **str** |  | [optional] 
**pricing_plans** | [**List[SnowflakeMarketplaceProductPricingPlan]**](SnowflakeMarketplaceProductPricingPlan.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**publish_on_approval** | **bool** |  | [optional] 
**regions** | **str** |  | [optional] 
**rejected_on** | **str** |  | [optional] 
**rejected_reason** | **str** |  | [optional] 
**replication_schedule** | **str** |  | [optional] 
**retired_on** | **str** |  | [optional] 
**scheduled_drop_time** | **str** |  | [optional] 
**share_type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**target_accounts** | **str** |  | [optional] 
**trial_details** | [**SnowflakeMarketplaceTrialDetails**](SnowflakeMarketplaceTrialDetails.md) |  | [optional] 
**unpublished_by_admin_reason** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_product import SnowflakeMarketplaceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceProduct from a JSON string
snowflake_marketplace_product_instance = SnowflakeMarketplaceProduct.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceProduct.to_json())

# convert the object into a dict
snowflake_marketplace_product_dict = snowflake_marketplace_product_instance.to_dict()
# create an instance of SnowflakeMarketplaceProduct from a dict
snowflake_marketplace_product_from_dict = SnowflakeMarketplaceProduct.from_dict(snowflake_marketplace_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


