# GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_template** | [**GcpPriceModelDiscountTemplate**](GcpPriceModelDiscountTemplate.md) |  | [optional] 
**sku_discount_templates** | **List[object]** |  | [optional] 
**sku_representation** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelSkuRepresentation**](GcpMarketplaceResellerPrivateOfferPlanPriceModelSkuRepresentation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_price_model_template_overage import GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage from a JSON string
gcp_marketplace_reseller_private_offer_plan_price_model_template_overage_instance = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_overage_dict = gcp_marketplace_reseller_private_offer_plan_price_model_template_overage_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage from a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_overage_from_dict = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage.from_dict(gcp_marketplace_reseller_private_offer_plan_price_model_template_overage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


