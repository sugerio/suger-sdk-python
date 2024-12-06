# GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_offer** | **str** | in format of \&quot;projects/{projectNumber}/services/service-name.endpoints.gcp-project-id.cloud.goog/standardOffers/base-offer-id\&quot; | [optional] 
**commitment** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment**](GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment.md) |  | [optional] 
**consumption** | **str** |  | [optional] 
**fixed_price** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateFixedPrice**](GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateFixedPrice.md) |  | [optional] 
**overage** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage**](GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateOverage.md) |  | [optional] 
**payg** | [**GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg**](GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplatePayg.md) |  | [optional] 
**subscription** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_price_model_template import GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate from a JSON string
gcp_marketplace_reseller_private_offer_plan_price_model_template_instance = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_dict = gcp_marketplace_reseller_private_offer_plan_price_model_template_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate from a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_from_dict = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplate.from_dict(gcp_marketplace_reseller_private_offer_plan_price_model_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


