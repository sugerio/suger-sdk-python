# AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_term** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**included_quantities** | [**List[AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem]**](AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem.md) |  | [optional] 
**payment_option** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**price_per_payment_in_usd** | **float** |  | [optional] 
**prices** | [**List[AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem]**](AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItemPriceItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_custom_meter_price_meter_item import AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem from a JSON string
azure_marketplace_price_and_availability_custom_meter_price_meter_item_instance = AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_custom_meter_price_meter_item_dict = azure_marketplace_price_and_availability_custom_meter_price_meter_item_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPriceMeterItem from a dict
azure_marketplace_price_and_availability_custom_meter_price_meter_item_form_dict = azure_marketplace_price_and_availability_custom_meter_price_meter_item.from_dict(azure_marketplace_price_and_availability_custom_meter_price_meter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


