# GcpMarketplaceResellerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_account_id** | **str** |  | [optional] 
**billing_account_nickname** | **str** |  | [optional] 
**billing_account_org_display_name** | **str** |  | [optional] 
**billing_account_type** | **str** |  | [optional] 
**notes_to_reseller** | **str** |  | [optional] 
**partner_account_name** | **str** | In the format of \&quot;\&quot;organizations/{GcpOrganizationID}/partnerAccounts/{partnerAccountID}\&quot; | [optional] 
**resell_offer_template_id** | **str** |  | [optional] 
**reseller_contact_email** | **str** |  | [optional] 
**reseller_contact_name** | **str** |  | [optional] 
**reseller_private_offer_plan_id** | **str** |  | [optional] 
**reseller_private_offer_plan_scope** | **str** |  | [optional] 
**sub_billing_account** | **str** | In the format of \&quot;billingAccounts/...\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_reseller_info import GcpMarketplaceResellerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceResellerInfo from a JSON string
gcp_marketplace_reseller_info_instance = GcpMarketplaceResellerInfo.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceResellerInfo.to_json())

# convert the object into a dict
gcp_marketplace_reseller_info_dict = gcp_marketplace_reseller_info_instance.to_dict()
# create an instance of GcpMarketplaceResellerInfo from a dict
gcp_marketplace_reseller_info_from_dict = GcpMarketplaceResellerInfo.from_dict(gcp_marketplace_reseller_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


