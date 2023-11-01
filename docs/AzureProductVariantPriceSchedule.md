# AzureProductVariantPriceSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time_range** | [**AzureLocalizedTimeRange**](AzureLocalizedTimeRange.md) |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**is_base_schedule** | **bool** | There is only one base schedule. | [optional] 
**market_codes** | **List[str]** | ISO country code | [optional] 
**schedules** | [**List[AzurePriceSchedule]**](AzurePriceSchedule.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_product_variant_price_schedule import AzureProductVariantPriceSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductVariantPriceSchedule from a JSON string
azure_product_variant_price_schedule_instance = AzureProductVariantPriceSchedule.from_json(json)
# print the JSON string representation of the object
print AzureProductVariantPriceSchedule.to_json()

# convert the object into a dict
azure_product_variant_price_schedule_dict = azure_product_variant_price_schedule_instance.to_dict()
# create an instance of AzureProductVariantPriceSchedule from a dict
azure_product_variant_price_schedule_form_dict = azure_product_variant_price_schedule.from_dict(azure_product_variant_price_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


