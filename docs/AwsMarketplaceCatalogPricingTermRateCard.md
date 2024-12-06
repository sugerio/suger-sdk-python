# AwsMarketplaceCatalogPricingTermRateCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**AwsMarketplaceCatalogPricingTermRateCardConstraints**](AwsMarketplaceCatalogPricingTermRateCardConstraints.md) | Defines constraints on how the term can be configured by acceptors. Applicable only to ConfigurableUpfrontPricingTerm. | [optional] 
**rate_card** | [**List[AwsMarketplaceCatalogPricingTermRateCardItem]**](AwsMarketplaceCatalogPricingTermRateCardItem.md) |  | [optional] 
**selector** | [**AwsMarketplaceCatalogPricingTermRateCardSelector**](AwsMarketplaceCatalogPricingTermRateCardSelector.md) | Selector is used to differentiate between the mutually exclusive rate cards in the same pricing term, to be selected by the buyer. Applicable only to ConfigurableUpfrontPricingTerm. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_catalog_pricing_term_rate_card import AwsMarketplaceCatalogPricingTermRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCatalogPricingTermRateCard from a JSON string
aws_marketplace_catalog_pricing_term_rate_card_instance = AwsMarketplaceCatalogPricingTermRateCard.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCatalogPricingTermRateCard.to_json())

# convert the object into a dict
aws_marketplace_catalog_pricing_term_rate_card_dict = aws_marketplace_catalog_pricing_term_rate_card_instance.to_dict()
# create an instance of AwsMarketplaceCatalogPricingTermRateCard from a dict
aws_marketplace_catalog_pricing_term_rate_card_from_dict = AwsMarketplaceCatalogPricingTermRateCard.from_dict(aws_marketplace_catalog_pricing_term_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


