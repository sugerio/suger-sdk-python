# CosellOppReferral


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **str** |  | [optional] 
**destination** | [**CosellOpp**](CosellOpp.md) |  | [optional] 
**destination_id** | **str** |  | [optional] 
**destination_partner** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_update_time** | **str** |  | [optional] 
**meta_info** | [**CosellOppMeta**](CosellOppMeta.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**source** | [**CosellOpp**](CosellOpp.md) |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_partner** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cosell_opp_referral import CosellOppReferral

# TODO update the JSON string below
json = "{}"
# create an instance of CosellOppReferral from a JSON string
cosell_opp_referral_instance = CosellOppReferral.from_json(json)
# print the JSON string representation of the object
print CosellOppReferral.to_json()

# convert the object into a dict
cosell_opp_referral_dict = cosell_opp_referral_instance.to_dict()
# create an instance of CosellOppReferral from a dict
cosell_opp_referral_form_dict = cosell_opp_referral.from_dict(cosell_opp_referral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


