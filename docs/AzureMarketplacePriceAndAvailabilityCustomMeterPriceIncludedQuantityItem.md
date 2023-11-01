# AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_term** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**is_infinite** | **bool** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item import AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem from a JSON string
azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item_instance = AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item_dict = azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeterPriceIncludedQuantityItem from a dict
azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item_form_dict = azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item.from_dict(azure_marketplace_price_and_availability_custom_meter_price_included_quantity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


