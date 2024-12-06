# GcpMarketplaceOfferTemplatePolicies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_renewal** | **bool** |  | [optional] 
**allow_scheduled_start_date** | **bool** |  | [optional] 
**max_renewal_times** | **str** | such as \&quot;3\&quot; | [optional] 
**proration** | [**GcpMarketplaceOfferProration**](GcpMarketplaceOfferProration.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_offer_template_policies import GcpMarketplaceOfferTemplatePolicies

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceOfferTemplatePolicies from a JSON string
gcp_marketplace_offer_template_policies_instance = GcpMarketplaceOfferTemplatePolicies.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceOfferTemplatePolicies.to_json())

# convert the object into a dict
gcp_marketplace_offer_template_policies_dict = gcp_marketplace_offer_template_policies_instance.to_dict()
# create an instance of GcpMarketplaceOfferTemplatePolicies from a dict
gcp_marketplace_offer_template_policies_from_dict = GcpMarketplaceOfferTemplatePolicies.from_dict(gcp_marketplace_offer_template_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


