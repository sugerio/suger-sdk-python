# MicrosoftPartnerReferralSolution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closing_date_time** | **object** |  | [optional] 
**currency** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **object** |  | [optional] 
**publisher_name** | **str** |  | [optional] 
**quantity** | **object** |  | [optional] 
**solution_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_partner_referral_solution import MicrosoftPartnerReferralSolution

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPartnerReferralSolution from a JSON string
microsoft_partner_referral_solution_instance = MicrosoftPartnerReferralSolution.from_json(json)
# print the JSON string representation of the object
print MicrosoftPartnerReferralSolution.to_json()

# convert the object into a dict
microsoft_partner_referral_solution_dict = microsoft_partner_referral_solution_instance.to_dict()
# create an instance of MicrosoftPartnerReferralSolution from a dict
microsoft_partner_referral_solution_form_dict = microsoft_partner_referral_solution.from_dict(microsoft_partner_referral_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


