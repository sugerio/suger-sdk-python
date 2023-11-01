# GcpUserInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** | An array of strings representing the user&#39;s roles. Right now, it can be either: ** account_admin, which indicates that the user is a Billing Account Administrator of the billing account that purchased the product, or ** project_editor, which indicates that the user is a Project Editor, but not a Billing Administrator, of the project under that billing account. | [optional] 
**user_identity** | **str** | The user&#39;s obfuscated GAIA ID, which can be used to initiate Open ID Connect. | [optional] 

## Example

```python
from openapi_client.models.gcp_user_info import GcpUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpUserInfo from a JSON string
gcp_user_info_instance = GcpUserInfo.from_json(json)
# print the JSON string representation of the object
print GcpUserInfo.to_json()

# convert the object into a dict
gcp_user_info_dict = gcp_user_info_instance.to_dict()
# create an instance of GcpUserInfo from a dict
gcp_user_info_form_dict = gcp_user_info.from_dict(gcp_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


