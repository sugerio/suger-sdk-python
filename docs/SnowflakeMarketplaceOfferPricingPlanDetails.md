# SnowflakeMarketplaceOfferPricingPlanDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the pricing plan name. Used for V2 offers with OVERRIDDEN type. | [optional] 
**overrides** | [**SnowflakeMarketplaceOfferOneTimeOverride**](SnowflakeMarketplaceOfferOneTimeOverride.md) |  | [optional] 
**type** | **str** | Type: DEFAULT for V1 private offer, INLINE for one time offer, OVERRIDDEN for V2 private offer with pricing plan | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_offer_pricing_plan_details import SnowflakeMarketplaceOfferPricingPlanDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceOfferPricingPlanDetails from a JSON string
snowflake_marketplace_offer_pricing_plan_details_instance = SnowflakeMarketplaceOfferPricingPlanDetails.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceOfferPricingPlanDetails.to_json())

# convert the object into a dict
snowflake_marketplace_offer_pricing_plan_details_dict = snowflake_marketplace_offer_pricing_plan_details_instance.to_dict()
# create an instance of SnowflakeMarketplaceOfferPricingPlanDetails from a dict
snowflake_marketplace_offer_pricing_plan_details_from_dict = SnowflakeMarketplaceOfferPricingPlanDetails.from_dict(snowflake_marketplace_offer_pricing_plan_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


