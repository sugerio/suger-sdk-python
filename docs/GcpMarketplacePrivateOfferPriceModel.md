# GcpMarketplacePrivateOfferPriceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_offer** | **str** | in format of \&quot;projects/{projectNumber}/services/service-name.endpoints.gcp-project-id.cloud.goog/standardOffers/base-offer-id\&quot; | [optional] 
**commitment** | [**GcpMarketplacePrivateOfferPriceModelCommitment**](GcpMarketplacePrivateOfferPriceModelCommitment.md) |  | [optional] 
**fixed_price** | [**GcpMarketplacePrivateOfferPriceModelFixed**](GcpMarketplacePrivateOfferPriceModelFixed.md) |  | [optional] 
**one_time_credit** | [**GcpPriceValue**](GcpPriceValue.md) | The one time credit in amount of money | [optional] 
**overage** | [**GcpMarketplacePrivateOfferPriceModelOverage**](GcpMarketplacePrivateOfferPriceModelOverage.md) |  | [optional] 
**payg** | [**GcpMarketplacePrivateOfferPriceModelPayg**](GcpMarketplacePrivateOfferPriceModelPayg.md) | Pay as you go. | [optional] 
**previous_credit_balance_policy** | **str** | such as \&quot;PREVIOUS_CREDIT_BALANCE_POLICY_UNSPECIFIED\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model import GcpMarketplacePrivateOfferPriceModel

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPriceModel from a JSON string
gcp_marketplace_private_offer_price_model_instance = GcpMarketplacePrivateOfferPriceModel.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferPriceModel.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_price_model_dict = gcp_marketplace_private_offer_price_model_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPriceModel from a dict
gcp_marketplace_private_offer_price_model_from_dict = GcpMarketplacePrivateOfferPriceModel.from_dict(gcp_marketplace_private_offer_price_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


