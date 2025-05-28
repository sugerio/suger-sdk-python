# GcpMarketplacePrivateOfferPolicies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy** | **str** | The cancellation policy of the offer. | [optional] 
**default_renewal_policy** | **str** | The default renewal policy of the offer. | [optional] 
**downgrade_policy** | **str** | The downgrade policy of the offer. | [optional] 
**max_renewal_times** | **str** | The max renewal times of the offer. | [optional] 
**offer_deal_type** | [**GcpMarketplaceOfferDealType**](GcpMarketplaceOfferDealType.md) | The offer deal type of the offer. | [optional] 
**purchase_approval** | **str** | The purchase approval of the offer. | [optional] 
**purchase_approval_override** | **str** | The purchase approval override of the offer. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_policies import GcpMarketplacePrivateOfferPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferPolicies from a JSON string
gcp_marketplace_private_offer_policies_instance = GcpMarketplacePrivateOfferPolicies.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferPolicies.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_policies_dict = gcp_marketplace_private_offer_policies_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferPolicies from a dict
gcp_marketplace_private_offer_policies_from_dict = GcpMarketplacePrivateOfferPolicies.from_dict(gcp_marketplace_private_offer_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


