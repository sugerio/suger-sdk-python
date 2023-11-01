# AzureMarketplacePriceAndAvailabilityPrivateOfferPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_meters** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters**](AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters.md) |  | [optional] 
**recurrent_price** | [**AzureMarketplacePriceAndAvailabilityRecurrentPrice**](AzureMarketplacePriceAndAvailabilityRecurrentPrice.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_private_offer_price import AzureMarketplacePriceAndAvailabilityPrivateOfferPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPrice from a JSON string
azure_marketplace_price_and_availability_private_offer_price_instance = AzureMarketplacePriceAndAvailabilityPrivateOfferPrice.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilityPrivateOfferPrice.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_private_offer_price_dict = azure_marketplace_price_and_availability_private_offer_price_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPrice from a dict
azure_marketplace_price_and_availability_private_offer_price_form_dict = azure_marketplace_price_and_availability_private_offer_price.from_dict(azure_marketplace_price_and_availability_private_offer_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


