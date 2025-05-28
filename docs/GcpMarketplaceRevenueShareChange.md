# GcpMarketplaceRevenueShareChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revenue_share** | [**GcpMarketplaceRevenueShareValue**](GcpMarketplaceRevenueShareValue.md) |  | [optional] 
**revenue_share_type** | [**GcpMarketplaceRevenueShareType**](GcpMarketplaceRevenueShareType.md) |  | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_revenue_share_change import GcpMarketplaceRevenueShareChange

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceRevenueShareChange from a JSON string
gcp_marketplace_revenue_share_change_instance = GcpMarketplaceRevenueShareChange.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceRevenueShareChange.to_json())

# convert the object into a dict
gcp_marketplace_revenue_share_change_dict = gcp_marketplace_revenue_share_change_instance.to_dict()
# create an instance of GcpMarketplaceRevenueShareChange from a dict
gcp_marketplace_revenue_share_change_from_dict = GcpMarketplaceRevenueShareChange.from_dict(gcp_marketplace_revenue_share_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


