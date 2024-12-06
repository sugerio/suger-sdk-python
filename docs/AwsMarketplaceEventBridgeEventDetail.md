# AwsMarketplaceEventBridgeEventDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **str** |  | [optional] 
**event_category** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**event_source** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**event_version** | **str** |  | [optional] 
**management_event** | **bool** |  | [optional] 
**manufacturer** | [**AwsMarketplaceEventBridgeEventAccount**](AwsMarketplaceEventBridgeEventAccount.md) | The seller/ISV&#39;s AWS Account Id. | [optional] 
**offer** | [**AwsMarketplaceEventBridgeEventOffer**](AwsMarketplaceEventBridgeEventOffer.md) |  | [optional] 
**product** | [**AwsMarketplaceEventBridgeEventProduct**](AwsMarketplaceEventBridgeEventProduct.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**request_parameters** | **object** |  | [optional] 
**response_elements** | **object** |  | [optional] 
**seller_of_record** | [**AwsMarketplaceEventBridgeEventAccount**](AwsMarketplaceEventBridgeEventAccount.md) | For private offer created by a channel partner, this is the channel partner&#39;s AWS Account Id. For private offer created by a seller/ISV, this is the seller/ISV&#39;s AWS Account Id. | [optional] 
**targeted_buyer_account_ids** | **List[str]** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_event_bridge_event_detail import AwsMarketplaceEventBridgeEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceEventBridgeEventDetail from a JSON string
aws_marketplace_event_bridge_event_detail_instance = AwsMarketplaceEventBridgeEventDetail.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceEventBridgeEventDetail.to_json())

# convert the object into a dict
aws_marketplace_event_bridge_event_detail_dict = aws_marketplace_event_bridge_event_detail_instance.to_dict()
# create an instance of AwsMarketplaceEventBridgeEventDetail from a dict
aws_marketplace_event_bridge_event_detail_from_dict = AwsMarketplaceEventBridgeEventDetail.from_dict(aws_marketplace_event_bridge_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


