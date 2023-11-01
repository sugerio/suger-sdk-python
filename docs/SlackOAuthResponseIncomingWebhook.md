# SlackOAuthResponseIncomingWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**configuration_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.slack_o_auth_response_incoming_webhook import SlackOAuthResponseIncomingWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SlackOAuthResponseIncomingWebhook from a JSON string
slack_o_auth_response_incoming_webhook_instance = SlackOAuthResponseIncomingWebhook.from_json(json)
# print the JSON string representation of the object
print SlackOAuthResponseIncomingWebhook.to_json()

# convert the object into a dict
slack_o_auth_response_incoming_webhook_dict = slack_o_auth_response_incoming_webhook_instance.to_dict()
# create an instance of SlackOAuthResponseIncomingWebhook from a dict
slack_o_auth_response_incoming_webhook_form_dict = slack_o_auth_response_incoming_webhook.from_dict(slack_o_auth_response_incoming_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


