# AzureMarketplaceDeprecationSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**alternative** | [**AzureMarketplaceDeprecationScheduleAlternative**](AzureMarketplaceDeprecationScheduleAlternative.md) |  | [optional] 
**var_date** | **str** | format: date-time | [optional] 
**date_offset** | **str** | format: duration | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_deprecation_schedule import AzureMarketplaceDeprecationSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceDeprecationSchedule from a JSON string
azure_marketplace_deprecation_schedule_instance = AzureMarketplaceDeprecationSchedule.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceDeprecationSchedule.to_json())

# convert the object into a dict
azure_marketplace_deprecation_schedule_dict = azure_marketplace_deprecation_schedule_instance.to_dict()
# create an instance of AzureMarketplaceDeprecationSchedule from a dict
azure_marketplace_deprecation_schedule_from_dict = AzureMarketplaceDeprecationSchedule.from_dict(azure_marketplace_deprecation_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


