# IdentityContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**id** | **str** | This is generated by Suger. When you create a new contact, do not provide. | [optional] 
**info** | [**IdentityConctactInfo**](IdentityConctactInfo.md) |  | [optional] 
**last_update_time** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.identity_contact import IdentityContact

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityContact from a JSON string
identity_contact_instance = IdentityContact.from_json(json)
# print the JSON string representation of the object
print IdentityContact.to_json()

# convert the object into a dict
identity_contact_dict = identity_contact_instance.to_dict()
# create an instance of IdentityContact from a dict
identity_contact_form_dict = identity_contact.from_dict(identity_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

