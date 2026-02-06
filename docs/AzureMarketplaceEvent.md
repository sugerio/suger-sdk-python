# AzureMarketplaceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AzureMarketplaceEventAction**](AzureMarketplaceEventAction.md) |  | [optional] 
**activity_id** | **str** |  | [optional] 
**id** | **str** | The Operation Id. | [optional] 
**offer_id** | **str** |  | [optional] 
**operation_request_source** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**purchase_token** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**subscription** | [**AzureMarketplaceSubscription**](AzureMarketplaceSubscription.md) |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**suger_organization_id** | **str** | Populated by Suger Service. | [optional] 
**time_stamp** | **datetime** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_event import AzureMarketplaceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceEvent from a JSON string
azure_marketplace_event_instance = AzureMarketplaceEvent.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceEvent.to_json())

# convert the object into a dict
azure_marketplace_event_dict = azure_marketplace_event_instance.to_dict()
# create an instance of AzureMarketplaceEvent from a dict
azure_marketplace_event_from_dict = AzureMarketplaceEvent.from_dict(azure_marketplace_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


