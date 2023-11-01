# GcpMarketplacePurchaseChannel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace** | **bool** |  | [optional] 
**reseller** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_purchase_channel import GcpMarketplacePurchaseChannel

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePurchaseChannel from a JSON string
gcp_marketplace_purchase_channel_instance = GcpMarketplacePurchaseChannel.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePurchaseChannel.to_json()

# convert the object into a dict
gcp_marketplace_purchase_channel_dict = gcp_marketplace_purchase_channel_instance.to_dict()
# create an instance of GcpMarketplacePurchaseChannel from a dict
gcp_marketplace_purchase_channel_form_dict = gcp_marketplace_purchase_channel.from_dict(gcp_marketplace_purchase_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


