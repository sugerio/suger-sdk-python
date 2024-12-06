# AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_schedule** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**reservation_duration** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**vm_prices** | [**AzureMarketplaceVmPrice**](AzureMarketplaceVmPrice.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_private_offer_plan_software_reservation import AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation from a JSON string
azure_marketplace_price_and_availability_private_offer_plan_software_reservation_instance = AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_private_offer_plan_software_reservation_dict = azure_marketplace_price_and_availability_private_offer_plan_software_reservation_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation from a dict
azure_marketplace_price_and_availability_private_offer_plan_software_reservation_from_dict = AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation.from_dict(azure_marketplace_price_and_availability_private_offer_plan_software_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


