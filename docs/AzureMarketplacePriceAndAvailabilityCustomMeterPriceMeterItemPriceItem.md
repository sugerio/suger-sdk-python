# AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_per_payment_in_usd** | **float** |  | [optional] 
**prices** | [**List[AzureMarketplacePrice]**](AzureMarketplacePrice.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_custom_meter_price_meter_item_price_item import AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem from a JSON string
azure_marketplace_price_and_availability_custom_meter_price_meter_item_price_item_instance = AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_custom_meter_price_meter_item_price_item_dict = azure_marketplace_price_and_availability_custom_meter_price_meter_item_price_item_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem from a dict
azure_marketplace_price_and_availability_custom_meter_price_meter_item_price_item_from_dict = AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem.from_dict(azure_marketplace_price_and_availability_custom_meter_price_meter_item_price_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


