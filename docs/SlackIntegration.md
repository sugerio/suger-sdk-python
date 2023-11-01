# SlackIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**authed_user** | [**SlackOAuthV2ResponseAuthedUser**](SlackOAuthV2ResponseAuthedUser.md) |  | [optional] 
**bot_user_id** | **str** |  | [optional] 
**enterprise** | [**SlackOAuthV2ResponseEnterprise**](SlackOAuthV2ResponseEnterprise.md) |  | [optional] 
**expires_in** | **int** |  | [optional] 
**incoming_webhook** | [**SlackOAuthResponseIncomingWebhook**](SlackOAuthResponseIncomingWebhook.md) |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**scope** | **str** | The scope of the access token. multiple scopes are separated by comma. | [optional] 
**team** | [**SlackOAuthV2ResponseTeam**](SlackOAuthV2ResponseTeam.md) |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.slack_integration import SlackIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of SlackIntegration from a JSON string
slack_integration_instance = SlackIntegration.from_json(json)
# print the JSON string representation of the object
print SlackIntegration.to_json()

# convert the object into a dict
slack_integration_dict = slack_integration_instance.to_dict()
# create an instance of SlackIntegration from a dict
slack_integration_form_dict = slack_integration.from_dict(slack_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


