# GcpMarketplacePrivateOfferMetricDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | such as \&quot;CPU\&quot; | [optional] 
**parent_commerce_service** | **str** | in format of \&quot;projects/{projectNumber}/services/service-name.endpoints.gcp-project-id.cloud.goog\&quot; | [optional] 
**sku_id** | **str** | such as \&quot;BC1B-6259-BF57\&quot; | [optional] 
**tiers** | [**List[GcpPriceTier]**](GcpPriceTier.md) | Price tiers for this metric. | [optional] 
**unit_description** | **str** | such as \&quot;minute\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_metric_detail import GcpMarketplacePrivateOfferMetricDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferMetricDetail from a JSON string
gcp_marketplace_private_offer_metric_detail_instance = GcpMarketplacePrivateOfferMetricDetail.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferMetricDetail.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_metric_detail_dict = gcp_marketplace_private_offer_metric_detail_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferMetricDetail from a dict
gcp_marketplace_private_offer_metric_detail_from_dict = GcpMarketplacePrivateOfferMetricDetail.from_dict(gcp_marketplace_private_offer_metric_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


