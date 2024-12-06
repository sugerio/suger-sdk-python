# AwsMarketplaceCatalogPricingTermRateCardConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_dimension_selection** | **str** | Determines if buyers are allowed to select multiple dimensions in the rate card. Possible values are \&quot;Allowed\&quot; and \&quot;Disallowed\&quot;. Default value is \&quot;Allowed\&quot;. | [optional] 
**quantity_configuration** | **str** | Determines if acceptors are allowed to configure quantity for each dimension in rate card. Possible values are \&quot;Allowed\&quot; and \&quot;Disallowed\&quot;. Default value is \&quot;Allowed\&quot;. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_catalog_pricing_term_rate_card_constraints import AwsMarketplaceCatalogPricingTermRateCardConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCatalogPricingTermRateCardConstraints from a JSON string
aws_marketplace_catalog_pricing_term_rate_card_constraints_instance = AwsMarketplaceCatalogPricingTermRateCardConstraints.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCatalogPricingTermRateCardConstraints.to_json())

# convert the object into a dict
aws_marketplace_catalog_pricing_term_rate_card_constraints_dict = aws_marketplace_catalog_pricing_term_rate_card_constraints_instance.to_dict()
# create an instance of AwsMarketplaceCatalogPricingTermRateCardConstraints from a dict
aws_marketplace_catalog_pricing_term_rate_card_constraints_from_dict = AwsMarketplaceCatalogPricingTermRateCardConstraints.from_dict(aws_marketplace_catalog_pricing_term_rate_card_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


