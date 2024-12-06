# AzureMarketplacePriceAndAvailabilityCustomMeterPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meters** | [**Dict[str, AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem]**](AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem.md) |  | [optional] 
**price_input_option** | **str** | default \&quot;usd\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_custom_meter_price import AzureMarketplacePriceAndAvailabilityCustomMeterPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPrice from a JSON string
azure_marketplace_price_and_availability_custom_meter_price_instance = AzureMarketplacePriceAndAvailabilityCustomMeterPrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityCustomMeterPrice.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_custom_meter_price_dict = azure_marketplace_price_and_availability_custom_meter_price_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPrice from a dict
azure_marketplace_price_and_availability_custom_meter_price_from_dict = AzureMarketplacePriceAndAvailabilityCustomMeterPrice.from_dict(azure_marketplace_price_and_availability_custom_meter_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


