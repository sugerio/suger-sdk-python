# MicrosoftPartnerReferralConsent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_to_contact** | **bool** |  | [optional] 
**consent_to_share_referral_with_microsoft_sellers** | **bool** |  | [optional] 
**consent_to_to_share_info_with_others** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_consent import MicrosoftPartnerReferralConsent

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralConsent from a JSON string
microsoft_partner_referral_consent_instance = MicrosoftPartnerReferralConsent.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralConsent.to_json()

# convert the object into a dict
microsoft_partner_referral_consent_dict = microsoft_partner_referral_consent_instance.to_dict()
# create an instance of MicrosoftPartnerReferralConsent from a dict
microsoft_partner_referral_consent_form_dict = microsoft_partner_referral_consent.from_dict(microsoft_partner_referral_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


