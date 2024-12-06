# GcpMarketplacePrivateOfferPriceModelFixed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**GcpMarketplacePrivateOfferPriceModelDiscount**](GcpMarketplacePrivateOfferPriceModelDiscount.md) |  | [optional] 
**period** | [**GcpPeriodDuration**](GcpPeriodDuration.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model_fixed import GcpMarketplacePrivateOfferPriceModelFixed

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPriceModelFixed from a JSON string
gcp_marketplace_private_offer_price_model_fixed_instance = GcpMarketplacePrivateOfferPriceModelFixed.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferPriceModelFixed.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_price_model_fixed_dict = gcp_marketplace_private_offer_price_model_fixed_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPriceModelFixed from a dict
gcp_marketplace_private_offer_price_model_fixed_from_dict = GcpMarketplacePrivateOfferPriceModelFixed.from_dict(gcp_marketplace_private_offer_price_model_fixed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


