# GcpMarketplaceExistingPrivateOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement** | **str** |  | [optional] 
**custom_eula** | [**GcpMarketplaceDocument**](GcpMarketplaceDocument.md) |  | [optional] 
**installment_timeline** | [**GcpMarketplacePrivateOfferInstallmentTimeline**](GcpMarketplacePrivateOfferInstallmentTimeline.md) |  | [optional] 
**name** | **str** | GCP private offer resource name. | [optional] 
**offer_term** | [**GcpMarketplacePrivateOfferTerm**](GcpMarketplacePrivateOfferTerm.md) |  | [optional] 
**payment_schedule** | [**PaymentScheduleType**](PaymentScheduleType.md) |  | [optional] 
**price_model** | [**GcpMarketplacePrivateOfferPriceModel**](GcpMarketplacePrivateOfferPriceModel.md) | Nill if the offer has payment installments. | [optional] 
**service_level** | **str** | The Plan of the offer. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_existing_private_offer import GcpMarketplaceExistingPrivateOffer

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceExistingPrivateOffer from a JSON string
gcp_marketplace_existing_private_offer_instance = GcpMarketplaceExistingPrivateOffer.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceExistingPrivateOffer.to_json())

# convert the object into a dict
gcp_marketplace_existing_private_offer_dict = gcp_marketplace_existing_private_offer_instance.to_dict()
# create an instance of GcpMarketplaceExistingPrivateOffer from a dict
gcp_marketplace_existing_private_offer_from_dict = GcpMarketplaceExistingPrivateOffer.from_dict(gcp_marketplace_existing_private_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


