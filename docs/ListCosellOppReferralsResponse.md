# ListCosellOppReferralsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cosell_opp_referrals** | [**List[CosellOppReferral]**](CosellOppReferral.md) |  | [optional] 
**next_offset** | **int** | If it is nil, it means there is no more records. | [optional] 
**total_count** | **int** | Only available when the request is made with offset&#x3D;0. | [optional] 

## Example

```python
from openapi_client.models.list_cosell_opp_referrals_response import ListCosellOppReferralsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCosellOppReferralsResponse from a JSON string
list_cosell_opp_referrals_response_instance = ListCosellOppReferralsResponse.from_json(json)
# print the JSON string representation of the object
print ListCosellOppReferralsResponse.to_json()

# convert the object into a dict
list_cosell_opp_referrals_response_dict = list_cosell_opp_referrals_response_instance.to_dict()
# create an instance of ListCosellOppReferralsResponse from a dict
list_cosell_opp_referrals_response_form_dict = list_cosell_opp_referrals_response.from_dict(list_cosell_opp_referrals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


