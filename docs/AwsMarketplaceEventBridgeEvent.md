# AwsMarketplaceEventBridgeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The seller/ISV AWS Account Id. | [optional] 
**detail** | [**AwsMarketplaceEventBridgeEventDetail**](AwsMarketplaceEventBridgeEventDetail.md) |  | [optional] 
**detail_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**resources** | **List[str]** |  | [optional] 
**source** | **str** | \&quot;aws.marketplacecatalog\&quot; | [optional] 
**time** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_event_bridge_event import AwsMarketplaceEventBridgeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceEventBridgeEvent from a JSON string
aws_marketplace_event_bridge_event_instance = AwsMarketplaceEventBridgeEvent.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceEventBridgeEvent.to_json())

# convert the object into a dict
aws_marketplace_event_bridge_event_dict = aws_marketplace_event_bridge_event_instance.to_dict()
# create an instance of AwsMarketplaceEventBridgeEvent from a dict
aws_marketplace_event_bridge_event_from_dict = AwsMarketplaceEventBridgeEvent.from_dict(aws_marketplace_event_bridge_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


