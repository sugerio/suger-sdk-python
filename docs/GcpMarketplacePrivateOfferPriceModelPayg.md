# GcpMarketplacePrivateOfferPriceModelPayg


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**GcpMarketplacePrivateOfferPriceModelDiscount**](GcpMarketplacePrivateOfferPriceModelDiscount.md) |  | [optional] 
**sku_discounts** | **List[object]** | TODO: need to define the type | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer_price_model_payg import GcpMarketplacePrivateOfferPriceModelPayg

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPriceModelPayg from a JSON string
gcp_marketplace_private_offer_price_model_payg_instance = GcpMarketplacePrivateOfferPriceModelPayg.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOfferPriceModelPayg.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_price_model_payg_dict = gcp_marketplace_private_offer_price_model_payg_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPriceModelPayg from a dict
gcp_marketplace_private_offer_price_model_payg_form_dict = gcp_marketplace_private_offer_price_model_payg.from_dict(gcp_marketplace_private_offer_price_model_payg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


