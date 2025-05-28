# GcpMarketplacePrivateOfferRevenueShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew_revenue_share** | [**GcpMarketplaceRevenueShareValue**](GcpMarketplaceRevenueShareValue.md) |  | [optional] 
**revenue_share** | [**GcpMarketplaceRevenueShareValue**](GcpMarketplaceRevenueShareValue.md) |  | [optional] 
**revenue_share_changes** | [**List[GcpMarketplaceRevenueShareChange]**](GcpMarketplaceRevenueShareChange.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_revenue_share import GcpMarketplacePrivateOfferRevenueShare

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferRevenueShare from a JSON string
gcp_marketplace_private_offer_revenue_share_instance = GcpMarketplacePrivateOfferRevenueShare.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferRevenueShare.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_revenue_share_dict = gcp_marketplace_private_offer_revenue_share_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferRevenueShare from a dict
gcp_marketplace_private_offer_revenue_share_from_dict = GcpMarketplacePrivateOfferRevenueShare.from_dict(gcp_marketplace_private_offer_revenue_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


