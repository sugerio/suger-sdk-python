# AzureMarketplacePriceAndAvailabilityRecurrentPriceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_term** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**payment_option** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**price_per_payment_in_usd** | **float** |  | [optional] 
**prices** | [**List[AzureMarketplacePrice]**](AzureMarketplacePrice.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_recurrent_price_item import AzureMarketplacePriceAndAvailabilityRecurrentPriceItem

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityRecurrentPriceItem from a JSON string
azure_marketplace_price_and_availability_recurrent_price_item_instance = AzureMarketplacePriceAndAvailabilityRecurrentPriceItem.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityRecurrentPriceItem.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_recurrent_price_item_dict = azure_marketplace_price_and_availability_recurrent_price_item_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityRecurrentPriceItem from a dict
azure_marketplace_price_and_availability_recurrent_price_item_from_dict = AzureMarketplacePriceAndAvailabilityRecurrentPriceItem.from_dict(azure_marketplace_price_and_availability_recurrent_price_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


