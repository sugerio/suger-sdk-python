# AuditingEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ace_event_bridge_event** | [**AceEventBridgeEvent**](AceEventBridgeEvent.md) | Nullable, applicable when eventType &#x3D; AWS_ACE_EVENT_BRIDGE. | [optional] 
**alibaba_marketplace_event** | [**AlibabaMarketplaceEvent**](AlibabaMarketplaceEvent.md) | Nullable, applicable when eventType &#x3D; ALIBABA_MARKETPLACE. | [optional] 
**aws_marketplace_event** | [**AwsMarketplaceEvent**](AwsMarketplaceEvent.md) | Nullable, applicable when eventType &#x3D; AWS_MARKETPLACE. | [optional] 
**aws_marketplace_event_bridge_event** | [**AwsMarketplaceEventBridgeEvent**](AwsMarketplaceEventBridgeEvent.md) | Nullable, applicable when eventType &#x3D; AWS_EVENT_BRIDGE. | [optional] 
**azure_marketplace_event** | [**AzureMarketplaceEvent**](AzureMarketplaceEvent.md) | Nullable, applicable when eventType &#x3D; AZURE_MARKETPLACE. | [optional] 
**creation_time** | **datetime** | When the event is received and audited. | [optional] 
**event_type** | **str** |  | [optional] 
**gcp_marketplace_event** | [**GcpMarketplaceEvent**](GcpMarketplaceEvent.md) | Nullable, applicable when eventType &#x3D; GCP_MARKETPLACE. | [optional] 
**id** | **str** |  | [optional] 
**last_update_time** | **datetime** | when the event is updated. | [optional] 
**organization_id** | **str** |  | [optional] 
**other_type_event** | **object** | Nullable, applicable when eventType is other types. | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.auditing_event import AuditingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuditingEvent from a JSON string
auditing_event_instance = AuditingEvent.from_json(json)
# print the JSON string representation of the object
print(AuditingEvent.to_json())

# convert the object into a dict
auditing_event_dict = auditing_event_instance.to_dict()
# create an instance of AuditingEvent from a dict
auditing_event_from_dict = AuditingEvent.from_dict(auditing_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


