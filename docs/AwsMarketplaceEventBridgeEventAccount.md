# AwsMarketplaceEventBridgeEventAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_event_bridge_event_account import AwsMarketplaceEventBridgeEventAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceEventBridgeEventAccount from a JSON string
aws_marketplace_event_bridge_event_account_instance = AwsMarketplaceEventBridgeEventAccount.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceEventBridgeEventAccount.to_json())

# convert the object into a dict
aws_marketplace_event_bridge_event_account_dict = aws_marketplace_event_bridge_event_account_instance.to_dict()
# create an instance of AwsMarketplaceEventBridgeEventAccount from a dict
aws_marketplace_event_bridge_event_account_from_dict = AwsMarketplaceEventBridgeEventAccount.from_dict(aws_marketplace_event_bridge_event_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


