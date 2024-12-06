# AzureMarketplacePriceAndAvailabilityCustomMeterItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**price** | **float** | Suger&#39;s custom field, for Suger internal use only. Not from Microsoft official schema. | [optional] 
**unit_of_measure** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_custom_meter_item import AzureMarketplacePriceAndAvailabilityCustomMeterItem

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterItem from a JSON string
azure_marketplace_price_and_availability_custom_meter_item_instance = AzureMarketplacePriceAndAvailabilityCustomMeterItem.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityCustomMeterItem.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_custom_meter_item_dict = azure_marketplace_price_and_availability_custom_meter_item_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterItem from a dict
azure_marketplace_price_and_availability_custom_meter_item_from_dict = AzureMarketplacePriceAndAvailabilityCustomMeterItem.from_dict(azure_marketplace_price_and_availability_custom_meter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


