# AlibabaMarketplaceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AlibabaMarketplaceAction**](AlibabaMarketplaceAction.md) |  | [optional] 
**ali_uid** | **str** | The Alibaba UID of the buyer&#39;s Alibaba Account. | [optional] 
**expired_on** | **datetime** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**is_refund** | **bool** |  | [optional] 
**order_biz_id** | **str** | Used as the Instance ID, and as the external ID for the Suger Entitlement. | [optional] 
**order_id** | **str** |  | [optional] 
**product_code** | **str** |  | [optional] 
**sku_id** | **str** |  | [optional] 
**suger_organization_id** | **str** | Suger organization ID of this event. Populated by Suger Service. | [optional] 
**template** | **str** |  | [optional] 
**time_stamp** | **datetime** | When the event was received by the Suger. | [optional] 
**token** | **str** | SPI security token. | [optional] 
**trial** | **bool** | If true, the event is for a trial. | [optional] 

## Example

```python
from suger_sdk_python.models.alibaba_marketplace_event import AlibabaMarketplaceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaMarketplaceEvent from a JSON string
alibaba_marketplace_event_instance = AlibabaMarketplaceEvent.from_json(json)
# print the JSON string representation of the object
print(AlibabaMarketplaceEvent.to_json())

# convert the object into a dict
alibaba_marketplace_event_dict = alibaba_marketplace_event_instance.to_dict()
# create an instance of AlibabaMarketplaceEvent from a dict
alibaba_marketplace_event_from_dict = AlibabaMarketplaceEvent.from_dict(alibaba_marketplace_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


