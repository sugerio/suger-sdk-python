# SnowflakeMarketplaceProductDefaultPricingPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_early_access** | **bool** | If true, consumers can access the listing before making a payment. You&#39;ll need to remind them to pay. | [optional] 
**base_fee** | **float** |  | [optional] 
**billing_duration** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**free_unit_kind** | **str** |  | [optional] 
**free_units** | **float** |  | [optional] 
**installment_schedule** | [**SnowflakeMarketplacePlanInstallmentSchedule**](SnowflakeMarketplacePlanInstallmentSchedule.md) |  | [optional] 
**is_auto_renewable** | **bool** | IsAutoRenewable is true if the product is auto renewable. | [optional] 
**max_fee** | **float** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**trial_usage_limit** | **float** |  | [optional] 
**trial_usage_unit** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**usage_unit_kind** | **str** |  | [optional] 
**usage_unit_price** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_product_default_pricing_plan import SnowflakeMarketplaceProductDefaultPricingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceProductDefaultPricingPlan from a JSON string
snowflake_marketplace_product_default_pricing_plan_instance = SnowflakeMarketplaceProductDefaultPricingPlan.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceProductDefaultPricingPlan.to_json())

# convert the object into a dict
snowflake_marketplace_product_default_pricing_plan_dict = snowflake_marketplace_product_default_pricing_plan_instance.to_dict()
# create an instance of SnowflakeMarketplaceProductDefaultPricingPlan from a dict
snowflake_marketplace_product_default_pricing_plan_from_dict = SnowflakeMarketplaceProductDefaultPricingPlan.from_dict(snowflake_marketplace_product_default_pricing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


