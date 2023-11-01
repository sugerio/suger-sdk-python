# CosellOpp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**info** | [**CosellOppInfo**](CosellOppInfo.md) |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 

## Example

```python
from openapi_client.models.cosell_opp import CosellOpp

# TODO update the JSON string below
json = "{}"
# create an instance of CosellOpp from a JSON string
cosell_opp_instance = CosellOpp.from_json(json)
# print the JSON string representation of the object
print CosellOpp.to_json()

# convert the object into a dict
cosell_opp_dict = cosell_opp_instance.to_dict()
# create an instance of CosellOpp from a dict
cosell_opp_form_dict = cosell_opp.from_dict(cosell_opp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


