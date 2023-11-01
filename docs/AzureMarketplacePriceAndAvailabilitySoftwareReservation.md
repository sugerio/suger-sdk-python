# AzureMarketplacePriceAndAvailabilitySoftwareReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage_save** | **float** | default 0 | [optional] 
**term** | **float** | default 0 | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_software_reservation import AzureMarketplacePriceAndAvailabilitySoftwareReservation

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilitySoftwareReservation from a JSON string
azure_marketplace_price_and_availability_software_reservation_instance = AzureMarketplacePriceAndAvailabilitySoftwareReservation.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilitySoftwareReservation.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_software_reservation_dict = azure_marketplace_price_and_availability_software_reservation_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilitySoftwareReservation from a dict
azure_marketplace_price_and_availability_software_reservation_form_dict = azure_marketplace_price_and_availability_software_reservation.from_dict(azure_marketplace_price_and_availability_software_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


