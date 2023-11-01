# MicrosoftPartnerReferralDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closing_date_time** | **str** | in UTC date time format | [optional] 
**currency** | **str** | ISO 4217 currency symbol | [optional] 
**customer_action** | **object** |  | [optional] 
**customer_requested_contact** | **object** |  | [optional] 
**deal_value** | **float** |  | [optional] 
**incentive_level** | **object** |  | [optional] 
**notes** | **str** |  | [optional] 
**requirements** | [**MicrosoftPartnerReferralRequirements**](MicrosoftPartnerReferralRequirements.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_detail import MicrosoftPartnerReferralDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralDetail from a JSON string
microsoft_partner_referral_detail_instance = MicrosoftPartnerReferralDetail.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralDetail.to_json()

# convert the object into a dict
microsoft_partner_referral_detail_dict = microsoft_partner_referral_detail_instance.to_dict()
# create an instance of MicrosoftPartnerReferralDetail from a dict
microsoft_partner_referral_detail_form_dict = microsoft_partner_referral_detail.from_dict(microsoft_partner_referral_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


