# MicrosoftPartnerReferralPerson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_preference** | [**MicrosoftPartnerReferralContactPreference**](MicrosoftPartnerReferralContactPreference.md) |  | [optional] 
**email** | **str** |  | [optional] 
**email_validation_status** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**linked_in_profile_url** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**phone_validation_status** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_person import MicrosoftPartnerReferralPerson

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralPerson from a JSON string
microsoft_partner_referral_person_instance = MicrosoftPartnerReferralPerson.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralPerson.to_json()

# convert the object into a dict
microsoft_partner_referral_person_dict = microsoft_partner_referral_person_instance.to_dict()
# create an instance of MicrosoftPartnerReferralPerson from a dict
microsoft_partner_referral_person_form_dict = microsoft_partner_referral_person.from_dict(microsoft_partner_referral_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


