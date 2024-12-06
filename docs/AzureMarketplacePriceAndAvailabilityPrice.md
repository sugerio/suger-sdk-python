# AzureMarketplacePriceAndAvailabilityPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_pricing** | [**AzureMarketplacePriceAndAvailabilityCorePrice**](AzureMarketplacePriceAndAvailabilityCorePrice.md) |  | [optional] 
**custom_meters** | [**AzureMarketplacePriceAndAvailabilityCustomMeterPrice**](AzureMarketplacePriceAndAvailabilityCustomMeterPrice.md) |  | [optional] 
**license_model** | **str** |  | [optional] 
**recurrent_price** | [**AzureMarketplacePriceAndAvailabilityRecurrentPrice**](AzureMarketplacePriceAndAvailabilityRecurrentPrice.md) |  | [optional] 
**system_meter_pricing** | [**AzureMarketplacePriceAndAvailabilitySystemMeterPrice**](AzureMarketplacePriceAndAvailabilitySystemMeterPrice.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_price import AzureMarketplacePriceAndAvailabilityPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPrice from a JSON string
azure_marketplace_price_and_availability_price_instance = AzureMarketplacePriceAndAvailabilityPrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityPrice.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_price_dict = azure_marketplace_price_and_availability_price_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPrice from a dict
azure_marketplace_price_and_availability_price_from_dict = AzureMarketplacePriceAndAvailabilityPrice.from_dict(azure_marketplace_price_and_availability_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


