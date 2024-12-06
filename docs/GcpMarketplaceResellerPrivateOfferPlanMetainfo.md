# GcpMarketplaceResellerPrivateOfferPlanMetainfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_organization_id** | **str** | Gcp Organiztion ID from integration with GCP Marketplace. | [optional] 
**gcp_project_number** | **str** | Gcp Project Number from integration with GCP Marketplace. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_metainfo import GcpMarketplaceResellerPrivateOfferPlanMetainfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanMetainfo from a JSON string
gcp_marketplace_reseller_private_offer_plan_metainfo_instance = GcpMarketplaceResellerPrivateOfferPlanMetainfo.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanMetainfo.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_metainfo_dict = gcp_marketplace_reseller_private_offer_plan_metainfo_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanMetainfo from a dict
gcp_marketplace_reseller_private_offer_plan_metainfo_from_dict = GcpMarketplaceResellerPrivateOfferPlanMetainfo.from_dict(gcp_marketplace_reseller_private_offer_plan_metainfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


