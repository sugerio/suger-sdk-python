# GcpMarketplacePrivateOfferPriceModelDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_percentage** | [**GcpAmountUnit**](GcpAmountUnit.md) | such as {\&quot;units\&quot;: \&quot;0\&quot;, \&quot;nanos\&quot;: 0} as no discount, or {\&quot;units\&quot;: \&quot;10\&quot;, \&quot;nanos\&quot;: 0} as 10% off discount | [optional] 
**discounted_price** | [**GcpPriceValue**](GcpPriceValue.md) | The discounted price of the private offer. If the discount is 10% off, and the original price is $100, then the discounted price is $90. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model_discount import GcpMarketplacePrivateOfferPriceModelDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPriceModelDiscount from a JSON string
gcp_marketplace_private_offer_price_model_discount_instance = GcpMarketplacePrivateOfferPriceModelDiscount.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferPriceModelDiscount.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_price_model_discount_dict = gcp_marketplace_private_offer_price_model_discount_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPriceModelDiscount from a dict
gcp_marketplace_private_offer_price_model_discount_from_dict = GcpMarketplacePrivateOfferPriceModelDiscount.from_dict(gcp_marketplace_private_offer_price_model_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


