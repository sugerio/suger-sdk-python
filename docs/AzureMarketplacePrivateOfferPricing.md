# AzureMarketplacePrivateOfferPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_plan** | **str** | required for SaasNewCustomizedPlans | [optional] 
**discount_percentage** | **float** | between 0.01 to 100 | [optional] 
**discount_type** | [**PrivateOfferDiscountType**](PrivateOfferDiscountType.md) |  | [optional] 
**markup_percentage** | **float** | between 0.00000001 to 100 | [optional] 
**new_plan_details** | [**AzureMarketplacePrivateOfferPricingNewPlanDetails**](AzureMarketplacePrivateOfferPricingNewPlanDetails.md) | required for SaasNewCustomizedPlans | [optional] 
**original_plan** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlan**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) | the pricing plan of the original plan. | [optional] 
**plan** | **str** | The base/original/default plan of the private offer, in format of \&quot;plan/product-durable-id/plan-durable-id\&quot; | [optional] 
**plan_id** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**plan_type** | **str** | The type of the plan, FLAT_RATE or PER_USER. | [optional] 
**price_details** | **object** |  | [optional] 
**private_offer_plan** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlan**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) | the pricing plan of the private offer | [optional] 
**product** | **str** | in format of \&quot;product/product-durable-id\&quot; | [optional] 
**product_name** | **str** |  | [optional] 
**suger_offer_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_private_offer_pricing import AzureMarketplacePrivateOfferPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferPricing from a JSON string
azure_marketplace_private_offer_pricing_instance = AzureMarketplacePrivateOfferPricing.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePrivateOfferPricing.to_json())

# convert the object into a dict
azure_marketplace_private_offer_pricing_dict = azure_marketplace_private_offer_pricing_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferPricing from a dict
azure_marketplace_private_offer_pricing_from_dict = AzureMarketplacePrivateOfferPricing.from_dict(azure_marketplace_private_offer_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


