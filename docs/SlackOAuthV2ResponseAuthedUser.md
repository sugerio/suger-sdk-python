# SlackOAuthV2ResponseAuthedUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.slack_o_auth_v2_response_authed_user import SlackOAuthV2ResponseAuthedUser

# TODO update the JSON string below
json = "{}"
# create an instance of SlackOAuthV2ResponseAuthedUser from a JSON string
slack_o_auth_v2_response_authed_user_instance = SlackOAuthV2ResponseAuthedUser.from_json(json)
# print the JSON string representation of the object
print SlackOAuthV2ResponseAuthedUser.to_json()

# convert the object into a dict
slack_o_auth_v2_response_authed_user_dict = slack_o_auth_v2_response_authed_user_instance.to_dict()
# create an instance of SlackOAuthV2ResponseAuthedUser from a dict
slack_o_auth_v2_response_authed_user_form_dict = slack_o_auth_v2_response_authed_user.from_dict(slack_o_auth_v2_response_authed_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


