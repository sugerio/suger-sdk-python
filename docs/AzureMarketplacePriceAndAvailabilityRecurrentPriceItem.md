# AzureMarketplacePriceAndAvailabilityRecurrentPriceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_frequency** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) | billingFrequency defines the frequency of the billing for recurring price. | [optional] 
**billing_term** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**contract_duration** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) | contractDuration defines the duration of the contract, should always be “year” with value 1 or 2 or 3 | [optional] 
**flexible_schedule** | [**AzureMarketplacePriceFlexibleSchedule**](AzureMarketplacePriceFlexibleSchedule.md) | flexibleSchedule defines the payment installments for flexible billing. | [optional] 
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


