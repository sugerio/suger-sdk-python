# MicrosoftPartnerReferralAdditionalRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[MicrosoftPartnerReferralRequirementAttribute]**](MicrosoftPartnerReferralRequirementAttribute.md) |  | [optional] 
**iot** | [**MicrosoftPartnerReferralIot**](MicrosoftPartnerReferralIot.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_additional_requirements import MicrosoftPartnerReferralAdditionalRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralAdditionalRequirements from a JSON string
microsoft_partner_referral_additional_requirements_instance = MicrosoftPartnerReferralAdditionalRequirements.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralAdditionalRequirements.to_json()

# convert the object into a dict
microsoft_partner_referral_additional_requirements_dict = microsoft_partner_referral_additional_requirements_instance.to_dict()
# create an instance of MicrosoftPartnerReferralAdditionalRequirements from a dict
microsoft_partner_referral_additional_requirements_form_dict = microsoft_partner_referral_additional_requirements.from_dict(microsoft_partner_referral_additional_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


