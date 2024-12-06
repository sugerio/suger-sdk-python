# GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_template** | [**GcpPriceModelDiscountTemplate**](GcpPriceModelDiscountTemplate.md) |  | [optional] 
**period** | [**GcpPeriodDuration**](GcpPeriodDuration.md) |  | [optional] 
**sku_discount_templates** | **List[object]** |  | [optional] 
**sku_representation** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelSkuRepresentation**](GcpMarketplaceResellerPrivateOfferPlanPriceModelSkuRepresentation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_price_model_template_payg import GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg from a JSON string
gcp_marketplace_reseller_private_offer_plan_price_model_template_payg_instance = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_payg_dict = gcp_marketplace_reseller_private_offer_plan_price_model_template_payg_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg from a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_payg_from_dict = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg.from_dict(gcp_marketplace_reseller_private_offer_plan_price_model_template_payg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


