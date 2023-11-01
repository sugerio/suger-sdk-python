# MicrosoftPartnerReferralRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_requirements** | [**MicrosoftPartnerReferralAdditionalRequirements**](MicrosoftPartnerReferralAdditionalRequirements.md) |  | [optional] 
**industries** | [**List[MicrosoftPartnerReferralTag]**](MicrosoftPartnerReferralTag.md) |  | [optional] 
**offers** | [**List[MicrosoftPartnerReferralTag]**](MicrosoftPartnerReferralTag.md) |  | [optional] 
**products** | [**List[MicrosoftPartnerReferralTag]**](MicrosoftPartnerReferralTag.md) |  | [optional] 
**sales_plays** | [**List[MicrosoftPartnerReferralTag]**](MicrosoftPartnerReferralTag.md) |  | [optional] 
**services** | [**List[MicrosoftPartnerReferralTag]**](MicrosoftPartnerReferralTag.md) |  | [optional] 
**solutions** | [**List[MicrosoftPartnerReferralSolution]**](MicrosoftPartnerReferralSolution.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_requirements import MicrosoftPartnerReferralRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralRequirements from a JSON string
microsoft_partner_referral_requirements_instance = MicrosoftPartnerReferralRequirements.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralRequirements.to_json()

# convert the object into a dict
microsoft_partner_referral_requirements_dict = microsoft_partner_referral_requirements_instance.to_dict()
# create an instance of MicrosoftPartnerReferralRequirements from a dict
microsoft_partner_referral_requirements_form_dict = microsoft_partner_referral_requirements.from_dict(microsoft_partner_referral_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


