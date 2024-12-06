# AwsMarketplaceCppoOpportunityTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**documents** | [**List[AwsMarketplaceCatalogLegalTermDocument]**](AwsMarketplaceCatalogLegalTermDocument.md) |  | [optional] 
**duration** | **str** | ISO 8601 duration format. For example, \&quot;P12M\&quot; represents 12 months. | [optional] 
**grants** | [**List[AwsMarketplaceCppoOpportunityUpfrontPriceGrant]**](AwsMarketplaceCppoOpportunityUpfrontPriceGrant.md) |  | [optional] 
**id** | **str** |  | [optional] 
**maximum_agreement_start_date** | **str** |  | [optional] 
**positive_targeting** | [**AwsMarketplaceCppoOpportunityPositiveTargeting**](AwsMarketplaceCppoOpportunityPositiveTargeting.md) |  | [optional] 
**price** | **str** | For ResaleFixedUpfrontPricingTerm | [optional] 
**rate_cards** | [**List[AwsMarketplaceCatalogPricingTermRateCard]**](AwsMarketplaceCatalogPricingTermRateCard.md) |  | [optional] 
**schedule** | [**List[AwsMarketplaceCppoOpportunityPaymentSchedule]**](AwsMarketplaceCppoOpportunityPaymentSchedule.md) | For ResalePaymentScheduleTerm | [optional] 
**type** | [**AwsMarketplaceCppoOpportunityTermType**](AwsMarketplaceCppoOpportunityTermType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_cppo_opportunity_term import AwsMarketplaceCppoOpportunityTerm

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoOpportunityTerm from a JSON string
aws_marketplace_cppo_opportunity_term_instance = AwsMarketplaceCppoOpportunityTerm.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCppoOpportunityTerm.to_json())

# convert the object into a dict
aws_marketplace_cppo_opportunity_term_dict = aws_marketplace_cppo_opportunity_term_instance.to_dict()
# create an instance of AwsMarketplaceCppoOpportunityTerm from a dict
aws_marketplace_cppo_opportunity_term_from_dict = AwsMarketplaceCppoOpportunityTerm.from_dict(aws_marketplace_cppo_opportunity_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


