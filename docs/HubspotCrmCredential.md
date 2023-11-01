# HubspotCrmCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**acquired_on** | **int** | UTC timestamp on receiving the auth response | [optional] 
**expires_in** | **int** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hubspot_crm_credential import HubspotCrmCredential

# TODO update the JSON string below
json = "{}"
# create an instance of HubspotCrmCredential from a JSON string
hubspot_crm_credential_instance = HubspotCrmCredential.from_json(json)
# print the JSON string representation of the object
print HubspotCrmCredential.to_json()

# convert the object into a dict
hubspot_crm_credential_dict = hubspot_crm_credential_instance.to_dict()
# create an instance of HubspotCrmCredential from a dict
hubspot_crm_credential_form_dict = hubspot_crm_credential.from_dict(hubspot_crm_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


