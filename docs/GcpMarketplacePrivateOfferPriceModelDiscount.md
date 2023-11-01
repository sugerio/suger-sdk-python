# GcpMarketplacePrivateOfferPriceModelDiscount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_percentage** | [**GcpDiscountPercentage**](GcpDiscountPercentage.md) |  | [optional] 
**discounted_price** | [**GcpPriceValue**](GcpPriceValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer_price_model_discount import GcpMarketplacePrivateOfferPriceModelDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPriceModelDiscount from a JSON string
gcp_marketplace_private_offer_price_model_discount_instance = GcpMarketplacePrivateOfferPriceModelDiscount.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOfferPriceModelDiscount.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_price_model_discount_dict = gcp_marketplace_private_offer_price_model_discount_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPriceModelDiscount from a dict
gcp_marketplace_private_offer_price_model_discount_form_dict = gcp_marketplace_private_offer_price_model_discount.from_dict(gcp_marketplace_private_offer_price_model_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


