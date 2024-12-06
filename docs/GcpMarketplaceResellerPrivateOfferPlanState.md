# GcpMarketplaceResellerPrivateOfferPlanState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_reason** | **object** |  | [optional] 
**comment** | **str** |  | [optional] 
**rejection_reason** | **object** |  | [optional] 
**state_type** | [**GcpMarketplaceResellerPrivateOfferPlanStateType**](GcpMarketplaceResellerPrivateOfferPlanStateType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_state import GcpMarketplaceResellerPrivateOfferPlanState

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanState from a JSON string
gcp_marketplace_reseller_private_offer_plan_state_instance = GcpMarketplaceResellerPrivateOfferPlanState.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanState.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_state_dict = gcp_marketplace_reseller_private_offer_plan_state_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanState from a dict
gcp_marketplace_reseller_private_offer_plan_state_from_dict = GcpMarketplaceResellerPrivateOfferPlanState.from_dict(gcp_marketplace_reseller_private_offer_plan_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


