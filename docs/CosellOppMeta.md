# CosellOppMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archived** | **bool** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**salesforce_referral_id** | **str** |  | [optional] 
**status** | [**CosellReferralStatus**](CosellReferralStatus.md) |  | [optional] 
**sync_record** | [**CosellSyncRecord**](CosellSyncRecord.md) |  | [optional] 

## Example

```python
from openapi_client.models.cosell_opp_meta import CosellOppMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CosellOppMeta from a JSON string
cosell_opp_meta_instance = CosellOppMeta.from_json(json)
# print the JSON string representation of the object
print CosellOppMeta.to_json()

# convert the object into a dict
cosell_opp_meta_dict = cosell_opp_meta_instance.to_dict()
# create an instance of CosellOppMeta from a dict
cosell_opp_meta_form_dict = cosell_opp_meta.from_dict(cosell_opp_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


