# AzureMarketplacePriceAndAvailabilityCustomMeter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**custom_meters** | [**Dict[str, AzureMarketplacePriceAndAvailabilityCustomMeterItem]**](AzureMarketplacePriceAndAvailabilityCustomMeterItem.md) |  | [optional] 
**id** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_custom_meter import AzureMarketplacePriceAndAvailabilityCustomMeter

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeter from a JSON string
azure_marketplace_price_and_availability_custom_meter_instance = AzureMarketplacePriceAndAvailabilityCustomMeter.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityCustomMeter.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_custom_meter_dict = azure_marketplace_price_and_availability_custom_meter_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityCustomMeter from a dict
azure_marketplace_price_and_availability_custom_meter_from_dict = AzureMarketplacePriceAndAvailabilityCustomMeter.from_dict(azure_marketplace_price_and_availability_custom_meter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


