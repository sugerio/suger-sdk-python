# GcpMarketplacePrivateOfferPriceModelCommitment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment_amount_per_period** | [**GcpPriceValue**](GcpPriceValue.md) |  | [optional] 
**discount** | [**GcpMarketplacePrivateOfferPriceModelDiscount**](GcpMarketplacePrivateOfferPriceModelDiscount.md) |  | [optional] 
**period** | [**GcpPeriodDuration**](GcpPeriodDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer_price_model_commitment import GcpMarketplacePrivateOfferPriceModelCommitment

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPriceModelCommitment from a JSON string
gcp_marketplace_private_offer_price_model_commitment_instance = GcpMarketplacePrivateOfferPriceModelCommitment.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOfferPriceModelCommitment.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_price_model_commitment_dict = gcp_marketplace_private_offer_price_model_commitment_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPriceModelCommitment from a dict
gcp_marketplace_private_offer_price_model_commitment_form_dict = gcp_marketplace_private_offer_price_model_commitment.from_dict(gcp_marketplace_private_offer_price_model_commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


