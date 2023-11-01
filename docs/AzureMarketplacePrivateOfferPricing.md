# AzureMarketplacePrivateOfferPricing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_percentage** | **float** | between 0.01 to 100 | [optional] 
**discount_type** | [**PrivateOfferDiscountType**](PrivateOfferDiscountType.md) |  | [optional] 
**markup_percentage** | **float** | between 0.00000001 to 100 | [optional] 
**original_plan** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlan**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) |  | [optional] 
**plan** | **str** | in format of \&quot;plan/product-durable-id/plan-durable-id\&quot; | [optional] 
**plan_id** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**plan_type** | **str** | The type of the plan, FLAT_RATE or PER_USER. | [optional] 
**price_details** | **str** |  | [optional] 
**private_offer_plan** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlan**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) |  | [optional] 
**product** | **str** | in format of \&quot;product/product-durable-id\&quot; | [optional] 
**product_name** | **str** |  | [optional] 
**suger_offer_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_private_offer_pricing import AzureMarketplacePrivateOfferPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferPricing from a JSON string
azure_marketplace_private_offer_pricing_instance = AzureMarketplacePrivateOfferPricing.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePrivateOfferPricing.to_json()

# convert the object into a dict
azure_marketplace_private_offer_pricing_dict = azure_marketplace_private_offer_pricing_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferPricing from a dict
azure_marketplace_private_offer_pricing_form_dict = azure_marketplace_private_offer_pricing.from_dict(azure_marketplace_private_offer_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


