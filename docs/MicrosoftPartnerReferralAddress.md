# MicrosoftPartnerReferralAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **object** |  | [optional] 
**region** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_address import MicrosoftPartnerReferralAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralAddress from a JSON string
microsoft_partner_referral_address_instance = MicrosoftPartnerReferralAddress.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralAddress.to_json()

# convert the object into a dict
microsoft_partner_referral_address_dict = microsoft_partner_referral_address_instance.to_dict()
# create an instance of MicrosoftPartnerReferralAddress from a dict
microsoft_partner_referral_address_form_dict = microsoft_partner_referral_address.from_dict(microsoft_partner_referral_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


