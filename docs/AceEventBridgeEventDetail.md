# AceEventBridgeEventDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **str** | \&quot;AWS\&quot; or \&quot;Sandbox\&quot; | [optional] 
**engagement_invitation** | [**AceEventEngagementInvitation**](AceEventEngagementInvitation.md) | Engagement invitation-related events | [optional] 
**opportunity** | [**AceEventOpportunity**](AceEventOpportunity.md) | Opportunity-related events | [optional] 
**schema_version** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.ace_event_bridge_event_detail import AceEventBridgeEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AceEventBridgeEventDetail from a JSON string
ace_event_bridge_event_detail_instance = AceEventBridgeEventDetail.from_json(json)
# print the JSON string representation of the object
print(AceEventBridgeEventDetail.to_json())

# convert the object into a dict
ace_event_bridge_event_detail_dict = ace_event_bridge_event_detail_instance.to_dict()
# create an instance of AceEventBridgeEventDetail from a dict
ace_event_bridge_event_detail_from_dict = AceEventBridgeEventDetail.from_dict(ace_event_bridge_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


