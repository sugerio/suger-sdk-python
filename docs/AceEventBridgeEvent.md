# AceEventBridgeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**detail** | [**AceEventBridgeEventDetail**](AceEventBridgeEventDetail.md) |  | [optional] 
**detail_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**resources** | **List[str]** |  | [optional] 
**source** | **str** | \&quot;aws.partnercentral-selling\&quot; | [optional] 
**time** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.ace_event_bridge_event import AceEventBridgeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AceEventBridgeEvent from a JSON string
ace_event_bridge_event_instance = AceEventBridgeEvent.from_json(json)
# print the JSON string representation of the object
print(AceEventBridgeEvent.to_json())

# convert the object into a dict
ace_event_bridge_event_dict = ace_event_bridge_event_instance.to_dict()
# create an instance of AceEventBridgeEvent from a dict
ace_event_bridge_event_from_dict = AceEventBridgeEvent.from_dict(ace_event_bridge_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


