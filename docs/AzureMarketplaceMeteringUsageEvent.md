# AzureMarketplaceMeteringUsageEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | Dimension identifier | [optional] 
**effective_start_time** | **str** | Time in UTC when the usage event occurred | [optional] 
**plan_id** | **str** | Plan associated with the purchased offer | [optional] 
**quantity** | **float** | Number of units consumed | [optional] 
**resource_id** | **str** | subscriptionId property value for SaaS offer subscriptions; resourceUsageId property on the managed application resource for managed application offers. For managed applications, only use one of resourceId or resourceUri. | [optional] 
**resource_uri** | **str** | Resource URI for the managed app. Used with managed applications. Only use resourceUri or resourceId, but never both. | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_metering_usage_event import AzureMarketplaceMeteringUsageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceMeteringUsageEvent from a JSON string
azure_marketplace_metering_usage_event_instance = AzureMarketplaceMeteringUsageEvent.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceMeteringUsageEvent.to_json())

# convert the object into a dict
azure_marketplace_metering_usage_event_dict = azure_marketplace_metering_usage_event_instance.to_dict()
# create an instance of AzureMarketplaceMeteringUsageEvent from a dict
azure_marketplace_metering_usage_event_from_dict = AzureMarketplaceMeteringUsageEvent.from_dict(azure_marketplace_metering_usage_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


