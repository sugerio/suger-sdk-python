# AwsMarketplaceEventBridgeEventOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_event_bridge_event_offer import AwsMarketplaceEventBridgeEventOffer

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceEventBridgeEventOffer from a JSON string
aws_marketplace_event_bridge_event_offer_instance = AwsMarketplaceEventBridgeEventOffer.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceEventBridgeEventOffer.to_json())

# convert the object into a dict
aws_marketplace_event_bridge_event_offer_dict = aws_marketplace_event_bridge_event_offer_instance.to_dict()
# create an instance of AwsMarketplaceEventBridgeEventOffer from a dict
aws_marketplace_event_bridge_event_offer_from_dict = AwsMarketplaceEventBridgeEventOffer.from_dict(aws_marketplace_event_bridge_event_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


