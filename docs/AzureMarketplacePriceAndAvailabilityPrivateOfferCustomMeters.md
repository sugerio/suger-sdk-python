# AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meters** | **object** | One of PriceAndAvailabilityCustomMeter_USD or PriceAndAvailabilityCustomMeter_PerMarket | [optional] 
**price_input_option** | **str** | default \&quot;usd\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_private_offer_custom_meters import AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters from a JSON string
azure_marketplace_price_and_availability_private_offer_custom_meters_instance = AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_private_offer_custom_meters_dict = azure_marketplace_price_and_availability_private_offer_custom_meters_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters from a dict
azure_marketplace_price_and_availability_private_offer_custom_meters_from_dict = AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters.from_dict(azure_marketplace_price_and_availability_private_offer_custom_meters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


