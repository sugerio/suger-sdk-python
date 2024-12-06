# AzureMarketplacePriceAndAvailabilitySystemMeterPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | default 0 | [optional] 
**price_input_option** | **str** |  | [optional] 
**prices** | [**List[AzureMarketplacePrice]**](AzureMarketplacePrice.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_system_meter_price import AzureMarketplacePriceAndAvailabilitySystemMeterPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilitySystemMeterPrice from a JSON string
azure_marketplace_price_and_availability_system_meter_price_instance = AzureMarketplacePriceAndAvailabilitySystemMeterPrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilitySystemMeterPrice.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_system_meter_price_dict = azure_marketplace_price_and_availability_system_meter_price_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilitySystemMeterPrice from a dict
azure_marketplace_price_and_availability_system_meter_price_from_dict = AzureMarketplacePriceAndAvailabilitySystemMeterPrice.from_dict(azure_marketplace_price_and_availability_system_meter_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


