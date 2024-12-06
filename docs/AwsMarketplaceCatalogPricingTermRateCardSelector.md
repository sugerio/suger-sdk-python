# AwsMarketplaceCatalogPricingTermRateCardSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | At this time, only \&quot;Duration\&quot; is supported. | [optional] 
**value** | **str** | ISO 8601 duration format. For example, \&quot;P1M\&quot; represents one month. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_catalog_pricing_term_rate_card_selector import AwsMarketplaceCatalogPricingTermRateCardSelector

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCatalogPricingTermRateCardSelector from a JSON string
aws_marketplace_catalog_pricing_term_rate_card_selector_instance = AwsMarketplaceCatalogPricingTermRateCardSelector.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCatalogPricingTermRateCardSelector.to_json())

# convert the object into a dict
aws_marketplace_catalog_pricing_term_rate_card_selector_dict = aws_marketplace_catalog_pricing_term_rate_card_selector_instance.to_dict()
# create an instance of AwsMarketplaceCatalogPricingTermRateCardSelector from a dict
aws_marketplace_catalog_pricing_term_rate_card_selector_from_dict = AwsMarketplaceCatalogPricingTermRateCardSelector.from_dict(aws_marketplace_catalog_pricing_term_rate_card_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


