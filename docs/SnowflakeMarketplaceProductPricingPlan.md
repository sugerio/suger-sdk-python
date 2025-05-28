# SnowflakeMarketplaceProductPricingPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **float** |  | [optional] 
**billing_duration_months** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**contract_duration_months** | **str** |  | [optional] 
**contract_type** | **str** | PAY_AS_YOU_GO, LIMITED_TIME | [optional] 
**currency** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** | For pricing display purpose. eg: {\&quot;price\&quot;:\&quot;10\&quot;,\&quot;button_text\&quot;:\&quot;starter plan\&quot;} | [optional] 
**name** | **str** |  | [optional] 
**pricing_model** | **str** | pricing model: USAGE_BASED, FLAT_FEE | [optional] 
**sales_motion** | **str** | SELF_SERVE, PROACTIVE | [optional] 
**state** | **str** | state of pricing plan | [optional] 
**updated_on** | **str** |  | [optional] 
**usage_details** | [**SnowflakeMarketplacePricingPlanUsageDetails**](SnowflakeMarketplacePricingPlanUsageDetails.md) |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_product_pricing_plan import SnowflakeMarketplaceProductPricingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceProductPricingPlan from a JSON string
snowflake_marketplace_product_pricing_plan_instance = SnowflakeMarketplaceProductPricingPlan.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceProductPricingPlan.to_json())

# convert the object into a dict
snowflake_marketplace_product_pricing_plan_dict = snowflake_marketplace_product_pricing_plan_instance.to_dict()
# create an instance of SnowflakeMarketplaceProductPricingPlan from a dict
snowflake_marketplace_product_pricing_plan_from_dict = SnowflakeMarketplaceProductPricingPlan.from_dict(snowflake_marketplace_product_pricing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


