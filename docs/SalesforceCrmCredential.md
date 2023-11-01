# SalesforceCrmCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**client_id** | **str** | NOTE(shiman) Debugging purpose only | [optional] 
**client_secret** | **str** |  | [optional] 
**exp** | **int** |  | [optional] 
**instance_url** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_crm_credential import SalesforceCrmCredential

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceCrmCredential from a JSON string
salesforce_crm_credential_instance = SalesforceCrmCredential.from_json(json)
# print the JSON string representation of the object
print SalesforceCrmCredential.to_json()

# convert the object into a dict
salesforce_crm_credential_dict = salesforce_crm_credential_instance.to_dict()
# create an instance of SalesforceCrmCredential from a dict
salesforce_crm_credential_form_dict = salesforce_crm_credential.from_dict(salesforce_crm_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


