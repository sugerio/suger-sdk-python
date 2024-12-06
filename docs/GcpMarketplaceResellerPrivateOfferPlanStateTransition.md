# GcpMarketplaceResellerPrivateOfferPlanStateTransition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_state** | [**GcpMarketplaceResellerPrivateOfferPlanNewState**](GcpMarketplaceResellerPrivateOfferPlanNewState.md) |  | [optional] 
**transition_time** | **datetime** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_private_offer_plan_state_transition import GcpMarketplaceResellerPrivateOfferPlanStateTransition

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerPrivateOfferPlanStateTransition from a JSON string
gcp_marketplace_reseller_private_offer_plan_state_transition_instance = GcpMarketplaceResellerPrivateOfferPlanStateTransition.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerPrivateOfferPlanStateTransition.to_json())

# convert the object into a dict
gcp_marketplace_reseller_private_offer_plan_state_transition_dict = gcp_marketplace_reseller_private_offer_plan_state_transition_instance.to_dict()
# create an instance of GcpMarketplaceResellerPrivateOfferPlanStateTransition from a dict
gcp_marketplace_reseller_private_offer_plan_state_transition_from_dict = GcpMarketplaceResellerPrivateOfferPlanStateTransition.from_dict(gcp_marketplace_reseller_private_offer_plan_state_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


