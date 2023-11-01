# AzurePriceSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_cadence** | [**AzurePriceCadence**](AzurePriceCadence.md) |  | [optional] 
**pricing_model** | **str** |  | [optional] 
**pricing_units** | [**List[AzurePricingUnit]**](AzurePricingUnit.md) |  | [optional] 
**retail_price** | [**AzurePrice**](AzurePrice.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_price_schedule import AzurePriceSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePriceSchedule from a JSON string
azure_price_schedule_instance = AzurePriceSchedule.from_json(json)
# print the JSON string representation of the object
print AzurePriceSchedule.to_json()

# convert the object into a dict
azure_price_schedule_dict = azure_price_schedule_instance.to_dict()
# create an instance of AzurePriceSchedule from a dict
azure_price_schedule_form_dict = azure_price_schedule.from_dict(azure_price_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


