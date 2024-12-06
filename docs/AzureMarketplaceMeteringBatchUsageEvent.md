# AzureMarketplaceMeteringBatchUsageEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**List[AzureMarketplaceMeteringUsageEvent]**](AzureMarketplaceMeteringUsageEvent.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_metering_batch_usage_event import AzureMarketplaceMeteringBatchUsageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceMeteringBatchUsageEvent from a JSON string
azure_marketplace_metering_batch_usage_event_instance = AzureMarketplaceMeteringBatchUsageEvent.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceMeteringBatchUsageEvent.to_json())

# convert the object into a dict
azure_marketplace_metering_batch_usage_event_dict = azure_marketplace_metering_batch_usage_event_instance.to_dict()
# create an instance of AzureMarketplaceMeteringBatchUsageEvent from a dict
azure_marketplace_metering_batch_usage_event_from_dict = AzureMarketplaceMeteringBatchUsageEvent.from_dict(azure_marketplace_metering_batch_usage_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


