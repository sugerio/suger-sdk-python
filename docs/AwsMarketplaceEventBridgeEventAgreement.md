# AwsMarketplaceEventBridgeEventAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptance_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**intent** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_event_bridge_event_agreement import AwsMarketplaceEventBridgeEventAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceEventBridgeEventAgreement from a JSON string
aws_marketplace_event_bridge_event_agreement_instance = AwsMarketplaceEventBridgeEventAgreement.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceEventBridgeEventAgreement.to_json())

# convert the object into a dict
aws_marketplace_event_bridge_event_agreement_dict = aws_marketplace_event_bridge_event_agreement_instance.to_dict()
# create an instance of AwsMarketplaceEventBridgeEventAgreement from a dict
aws_marketplace_event_bridge_event_agreement_from_dict = AwsMarketplaceEventBridgeEventAgreement.from_dict(aws_marketplace_event_bridge_event_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


