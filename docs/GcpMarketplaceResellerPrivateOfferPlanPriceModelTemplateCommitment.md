# GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment_amount_per_period_template** | [**GcpCommitmentAmountPerPeriodTemplate**](GcpCommitmentAmountPerPeriodTemplate.md) |  | [optional] 
**discount_template** | [**GcpPriceModelDiscountTemplate**](GcpPriceModelDiscountTemplate.md) |  | [optional] 
**period** | [**GcpPeriodDuration**](GcpPeriodDuration.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_price_model_template_commitment import GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment from a JSON string
gcp_marketplace_reseller_private_offer_plan_price_model_template_commitment_instance = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_commitment_dict = gcp_marketplace_reseller_private_offer_plan_price_model_template_commitment_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment from a dict
gcp_marketplace_reseller_private_offer_plan_price_model_template_commitment_from_dict = GcpMarketplaceResellerPrivateOfferPlanPriceModelTemplateCommitment.from_dict(gcp_marketplace_reseller_private_offer_plan_price_model_template_commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


