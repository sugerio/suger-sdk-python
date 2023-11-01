# GcpMarketplacePrivateOfferTerm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_scheduled_start_times** | **bool** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**start_policy** | **str** | such as \&quot;OFFER_START_POLICY_IMMEDIATE\&quot; | [optional] 
**start_time** | **datetime** |  | [optional] 
**term_duration** | [**GcpPeriodDuration**](GcpPeriodDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer_term import GcpMarketplacePrivateOfferTerm

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferTerm from a JSON string
gcp_marketplace_private_offer_term_instance = GcpMarketplacePrivateOfferTerm.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOfferTerm.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_term_dict = gcp_marketplace_private_offer_term_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferTerm from a dict
gcp_marketplace_private_offer_term_form_dict = gcp_marketplace_private_offer_term.from_dict(gcp_marketplace_private_offer_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


