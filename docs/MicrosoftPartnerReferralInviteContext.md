# MicrosoftPartnerReferralInviteContext


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistance_request_code** | **str** |  | [optional] 
**invited_by** | [**MicrosoftPartnerReferralInvitedInfo**](MicrosoftPartnerReferralInvitedInfo.md) |  | [optional] 
**invited_mpn_id** | **str** |  | [optional] 
**notes** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_invite_context import MicrosoftPartnerReferralInviteContext

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralInviteContext from a JSON string
microsoft_partner_referral_invite_context_instance = MicrosoftPartnerReferralInviteContext.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralInviteContext.to_json()

# convert the object into a dict
microsoft_partner_referral_invite_context_dict = microsoft_partner_referral_invite_context_instance.to_dict()
# create an instance of MicrosoftPartnerReferralInviteContext from a dict
microsoft_partner_referral_invite_context_form_dict = microsoft_partner_referral_invite_context.from_dict(microsoft_partner_referral_invite_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


