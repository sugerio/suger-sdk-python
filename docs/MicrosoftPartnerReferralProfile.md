# MicrosoftPartnerReferralProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | **object** |  | [optional] 
**address** | [**MicrosoftPartnerReferralAddress**](MicrosoftPartnerReferralAddress.md) |  | [optional] 
**ids** | [**List[MicrosoftPartnerReferralProfileId]**](MicrosoftPartnerReferralProfileId.md) |  | [optional] 
**is_macc_eligible** | **bool** |  | [optional] 
**is_matching_complete** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**team** | [**List[MicrosoftPartnerReferralPerson]**](MicrosoftPartnerReferralPerson.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_profile import MicrosoftPartnerReferralProfile

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralProfile from a JSON string
microsoft_partner_referral_profile_instance = MicrosoftPartnerReferralProfile.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralProfile.to_json()

# convert the object into a dict
microsoft_partner_referral_profile_dict = microsoft_partner_referral_profile_instance.to_dict()
# create an instance of MicrosoftPartnerReferralProfile from a dict
microsoft_partner_referral_profile_form_dict = microsoft_partner_referral_profile.from_dict(microsoft_partner_referral_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


