# AzureMarketplacePriceFlexibleSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_schedule** | [**List[AzureMarketplacePriceBillingSchedule]**](AzureMarketplacePriceBillingSchedule.md) |  | [optional] 
**initial_charge** | [**AzureMarketplacePriceInitialCharge**](AzureMarketplacePriceInitialCharge.md) |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_flexible_schedule import AzureMarketplacePriceFlexibleSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceFlexibleSchedule from a JSON string
azure_marketplace_price_flexible_schedule_instance = AzureMarketplacePriceFlexibleSchedule.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceFlexibleSchedule.to_json())

# convert the object into a dict
azure_marketplace_price_flexible_schedule_dict = azure_marketplace_price_flexible_schedule_instance.to_dict()
# create an instance of AzureMarketplacePriceFlexibleSchedule from a dict
azure_marketplace_price_flexible_schedule_from_dict = AzureMarketplacePriceFlexibleSchedule.from_dict(azure_marketplace_price_flexible_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


