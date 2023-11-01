# MicrosoftPartnerReferral


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_date_time** | **str** |  | [optional] 
**call_to_action** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**closed_date_time** | **str** |  | [optional] 
**consent** | [**MicrosoftPartnerReferralConsent**](MicrosoftPartnerReferralConsent.md) |  | [optional] 
**created_date_time** | **str** |  | [optional] 
**created_via** | **str** |  | [optional] 
**customer_profile** | [**MicrosoftPartnerReferralProfile**](MicrosoftPartnerReferralProfile.md) |  | [optional] 
**deal_sensitivity** | **str** |  | [optional] 
**details** | [**MicrosoftPartnerReferralDetail**](MicrosoftPartnerReferralDetail.md) |  | [optional] 
**direction** | **str** |  | [optional] 
**e_tag** | **str** |  | [optional] 
**engagement_id** | **str** |  | [optional] 
**exception** | **object** |  | [optional] 
**expiration_date_time** | **str** |  | [optional] 
**external_reference_id** | **str** |  | [optional] 
**favorite** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**invite_context** | [**MicrosoftPartnerReferralInviteContext**](MicrosoftPartnerReferralInviteContext.md) |  | [optional] 
**is_auto_registration_enabled** | **bool** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**last_modified_via** | **str** |  | [optional] 
**links** | [**MicrosoftPartnerReferralLink**](MicrosoftPartnerReferralLink.md) |  | [optional] 
**mpn_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**qualification** | [**MicrosoftPartnerReferralQualification**](MicrosoftPartnerReferralQualification.md) |  | [optional] 
**quality** | **str** |  | [optional] 
**referral_program** | **object** |  | [optional] 
**referral_source** | **object** |  | [optional] 
**registration_status** | **str** |  | [optional] 
**registrations** | **List[object]** |  | [optional] 
**sales_stage** | **object** |  | [optional] 
**status** | [**MicrosoftPartnerReferralStatus**](MicrosoftPartnerReferralStatus.md) |  | [optional] 
**status_reason** | **str** |  | [optional] 
**substatus** | [**MicrosoftPartnerReferralSubStatus**](MicrosoftPartnerReferralSubStatus.md) |  | [optional] 
**tags** | **List[object]** |  | [optional] 
**target** | [**List[MicrosoftPartnerReferralTarget]**](MicrosoftPartnerReferralTarget.md) |  | [optional] 
**team** | [**List[MicrosoftPartnerReferralPerson]**](MicrosoftPartnerReferralPerson.md) |  | [optional] 
**tracking_info** | [**MicrosoftPartnerReferralTrackingInfo**](MicrosoftPartnerReferralTrackingInfo.md) |  | [optional] 
**type** | [**MicrosoftPartnerReferralType**](MicrosoftPartnerReferralType.md) |  | [optional] 
**updated_date_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral import MicrosoftPartnerReferral

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferral from a JSON string
microsoft_partner_referral_instance = MicrosoftPartnerReferral.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferral.to_json()

# convert the object into a dict
microsoft_partner_referral_dict = microsoft_partner_referral_instance.to_dict()
# create an instance of MicrosoftPartnerReferral from a dict
microsoft_partner_referral_form_dict = microsoft_partner_referral.from_dict(microsoft_partner_referral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


