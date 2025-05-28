# AzureMarketplacePriceBillingSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_date** | **str** | In format of YYYY-MM-DD. | [optional] 
**note** | **str** |  | [optional] 
**price_per_payment_in_usd** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_billing_schedule import AzureMarketplacePriceBillingSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceBillingSchedule from a JSON string
azure_marketplace_price_billing_schedule_instance = AzureMarketplacePriceBillingSchedule.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceBillingSchedule.to_json())

# convert the object into a dict
azure_marketplace_price_billing_schedule_dict = azure_marketplace_price_billing_schedule_instance.to_dict()
# create an instance of AzureMarketplacePriceBillingSchedule from a dict
azure_marketplace_price_billing_schedule_from_dict = AzureMarketplacePriceBillingSchedule.from_dict(azure_marketplace_price_billing_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


