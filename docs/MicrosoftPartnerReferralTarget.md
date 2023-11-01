# MicrosoftPartnerReferralTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**MicrosoftPartnerReferralTargetType**](MicrosoftPartnerReferralTargetType.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_target import MicrosoftPartnerReferralTarget

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralTarget from a JSON string
microsoft_partner_referral_target_instance = MicrosoftPartnerReferralTarget.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralTarget.to_json()

# convert the object into a dict
microsoft_partner_referral_target_dict = microsoft_partner_referral_target_instance.to_dict()
# create an instance of MicrosoftPartnerReferralTarget from a dict
microsoft_partner_referral_target_form_dict = microsoft_partner_referral_target.from_dict(microsoft_partner_referral_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


