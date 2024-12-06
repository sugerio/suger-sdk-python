# AwsMarketplaceCatalogPricingTermRateCardItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**dimension_key** | **str** |  | [optional] 
**display_name** | **str** | These fields are used for aws discovery API result. | [optional] 
**price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_catalog_pricing_term_rate_card_item import AwsMarketplaceCatalogPricingTermRateCardItem

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCatalogPricingTermRateCardItem from a JSON string
aws_marketplace_catalog_pricing_term_rate_card_item_instance = AwsMarketplaceCatalogPricingTermRateCardItem.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCatalogPricingTermRateCardItem.to_json())

# convert the object into a dict
aws_marketplace_catalog_pricing_term_rate_card_item_dict = aws_marketplace_catalog_pricing_term_rate_card_item_instance.to_dict()
# create an instance of AwsMarketplaceCatalogPricingTermRateCardItem from a dict
aws_marketplace_catalog_pricing_term_rate_card_item_from_dict = AwsMarketplaceCatalogPricingTermRateCardItem.from_dict(aws_marketplace_catalog_pricing_term_rate_card_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


