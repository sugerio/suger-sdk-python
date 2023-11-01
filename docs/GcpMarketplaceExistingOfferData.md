# GcpMarketplaceExistingOfferData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement** | [**GcpMarketplaceEntitlement**](GcpMarketplaceEntitlement.md) |  | [optional] 
**existing_price_model_type** | [**GcpMarketplacePrivateOfferPriceModelType**](GcpMarketplacePrivateOfferPriceModelType.md) |  | [optional] 
**has_entitlement_changed** | **bool** |  | [optional] 
**private_offer** | [**GcpMarketplaceExistingPrivateOffer**](GcpMarketplaceExistingPrivateOffer.md) |  | [optional] 
**standard_offer** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_existing_offer_data import GcpMarketplaceExistingOfferData

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceExistingOfferData from a JSON string
gcp_marketplace_existing_offer_data_instance = GcpMarketplaceExistingOfferData.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceExistingOfferData.to_json()

# convert the object into a dict
gcp_marketplace_existing_offer_data_dict = gcp_marketplace_existing_offer_data_instance.to_dict()
# create an instance of GcpMarketplaceExistingOfferData from a dict
gcp_marketplace_existing_offer_data_form_dict = gcp_marketplace_existing_offer_data.from_dict(gcp_marketplace_existing_offer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


