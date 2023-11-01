# IdentityBuyer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **List[str]** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**BuyerInfo**](BuyerInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.identity_buyer import IdentityBuyer

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityBuyer from a JSON string
identity_buyer_instance = IdentityBuyer.from_json(json)
# print the JSON string representation of the object
print IdentityBuyer.to_json()

# convert the object into a dict
identity_buyer_dict = identity_buyer_instance.to_dict()
# create an instance of IdentityBuyer from a dict
identity_buyer_form_dict = identity_buyer.from_dict(identity_buyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


