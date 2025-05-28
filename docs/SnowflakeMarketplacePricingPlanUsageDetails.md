# SnowflakeMarketplacePricingPlanUsageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_unit_kind** | **str** |  | [optional] 
**free_units** | **float** |  | [optional] 
**max_fee** | **float** |  | [optional] 
**usage_unit_kind** | **str** |  | [optional] 
**usage_unit_price** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_pricing_plan_usage_details import SnowflakeMarketplacePricingPlanUsageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplacePricingPlanUsageDetails from a JSON string
snowflake_marketplace_pricing_plan_usage_details_instance = SnowflakeMarketplacePricingPlanUsageDetails.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplacePricingPlanUsageDetails.to_json())

# convert the object into a dict
snowflake_marketplace_pricing_plan_usage_details_dict = snowflake_marketplace_pricing_plan_usage_details_instance.to_dict()
# create an instance of SnowflakeMarketplacePricingPlanUsageDetails from a dict
snowflake_marketplace_pricing_plan_usage_details_from_dict = SnowflakeMarketplacePricingPlanUsageDetails.from_dict(snowflake_marketplace_pricing_plan_usage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


