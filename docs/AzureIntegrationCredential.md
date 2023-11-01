# AzureIntegrationCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**expires_on** | **str** | The time when the access token expires. | [optional] 
**refresh_token** | **str** | The refresh token used to refresh the access token. | [optional] 
**tenant_id** | **str** |  | [optional] 
**token_scope** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_integration_credential import AzureIntegrationCredential

# TODO update the JSON string below
json = "{}"
# create an instance of AzureIntegrationCredential from a JSON string
azure_integration_credential_instance = AzureIntegrationCredential.from_json(json)
# print the JSON string representation of the object
print AzureIntegrationCredential.to_json()

# convert the object into a dict
azure_integration_credential_dict = azure_integration_credential_instance.to_dict()
# create an instance of AzureIntegrationCredential from a dict
azure_integration_credential_form_dict = azure_integration_credential.from_dict(azure_integration_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


