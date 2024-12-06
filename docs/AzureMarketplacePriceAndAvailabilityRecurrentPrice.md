# AzureMarketplacePriceAndAvailabilityRecurrentPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_input_option** | **str** | default \&quot;usd\&quot; | [optional] 
**prices** | [**List[AzureMarketplacePriceAndAvailabilityRecurrentPriceItem]**](AzureMarketplacePriceAndAvailabilityRecurrentPriceItem.md) |  | [optional] 
**recurrent_price_mode** | **str** | default \&quot;flatRate\&quot; | [optional] 
**user_limits** | [**AzureMarketplacePriceAndAvailabilityRecurrentPriceUserLimit**](AzureMarketplacePriceAndAvailabilityRecurrentPriceUserLimit.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_recurrent_price import AzureMarketplacePriceAndAvailabilityRecurrentPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityRecurrentPrice from a JSON string
azure_marketplace_price_and_availability_recurrent_price_instance = AzureMarketplacePriceAndAvailabilityRecurrentPrice.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityRecurrentPrice.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_recurrent_price_dict = azure_marketplace_price_and_availability_recurrent_price_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityRecurrentPrice from a dict
azure_marketplace_price_and_availability_recurrent_price_from_dict = AzureMarketplacePriceAndAvailabilityRecurrentPrice.from_dict(azure_marketplace_price_and_availability_recurrent_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


