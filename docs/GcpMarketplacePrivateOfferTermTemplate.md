# GcpMarketplacePrivateOfferTermTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_scheduled_start_times** | **bool** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**payment_recurrence** | **str** |  | [optional] 
**start_policy** | [**GcpMarketplaceOfferStartPolicy**](GcpMarketplaceOfferStartPolicy.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**term_duration** | [**GcpPeriodDuration**](GcpPeriodDuration.md) |  | [optional] 
**term_duration_constraint** | [**GcpMarketplacePrivateOfferTermDurationConstraint**](GcpMarketplacePrivateOfferTermDurationConstraint.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_term_template import GcpMarketplacePrivateOfferTermTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferTermTemplate from a JSON string
gcp_marketplace_private_offer_term_template_instance = GcpMarketplacePrivateOfferTermTemplate.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferTermTemplate.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_term_template_dict = gcp_marketplace_private_offer_term_template_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferTermTemplate from a dict
gcp_marketplace_private_offer_term_template_from_dict = GcpMarketplacePrivateOfferTermTemplate.from_dict(gcp_marketplace_private_offer_term_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


