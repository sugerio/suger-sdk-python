# CosellOppInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **Dict[str, object]** |  | [optional] 
**contact** | **Dict[str, object]** |  | [optional] 
**creation_time** | **str** |  | [optional] 
**last_modified_time** | **str** |  | [optional] 
**microsoft_partner_referral** | [**MicrosoftPartnerReferral**](MicrosoftPartnerReferral.md) |  | [optional] 
**opportunity** | **Dict[str, object]** |  | [optional] 
**owner** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.cosell_opp_info import CosellOppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CosellOppInfo from a JSON string
cosell_opp_info_instance = CosellOppInfo.from_json(json)
# print the JSON string representation of the object
print CosellOppInfo.to_json()

# convert the object into a dict
cosell_opp_info_dict = cosell_opp_info_instance.to_dict()
# create an instance of CosellOppInfo from a dict
cosell_opp_info_form_dict = cosell_opp_info.from_dict(cosell_opp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


