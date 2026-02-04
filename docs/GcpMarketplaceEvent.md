# GcpMarketplaceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**GcpMarketplaceUserAccount**](GcpMarketplaceUserAccount.md) |  | [optional] 
**entitlement** | [**GcpMarketplaceEntitlement**](GcpMarketplaceEntitlement.md) |  | [optional] 
**event_id** | **str** |  | [optional] 
**event_type** | [**GcpMarketplacceEventType**](GcpMarketplacceEventType.md) |  | [optional] 
**provider_id** | **str** | GCP Partner ID of the SaaS Seller. | [optional] 
**publish_time** | **datetime** | The Publish Time of the event. | [optional] 
**suger_organization_id** | **str** | Populated by Suger Service. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_event import GcpMarketplaceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceEvent from a JSON string
gcp_marketplace_event_instance = GcpMarketplaceEvent.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceEvent.to_json())

# convert the object into a dict
gcp_marketplace_event_dict = gcp_marketplace_event_instance.to_dict()
# create an instance of GcpMarketplaceEvent from a dict
gcp_marketplace_event_from_dict = GcpMarketplaceEvent.from_dict(gcp_marketplace_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


