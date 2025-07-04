# IdentityConctactInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_location** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.identity_conctact_info import IdentityConctactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityConctactInfo from a JSON string
identity_conctact_info_instance = IdentityConctactInfo.from_json(json)
# print the JSON string representation of the object
print(IdentityConctactInfo.to_json())

# convert the object into a dict
identity_conctact_info_dict = identity_conctact_info_instance.to_dict()
# create an instance of IdentityConctactInfo from a dict
identity_conctact_info_from_dict = IdentityConctactInfo.from_dict(identity_conctact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


