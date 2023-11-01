# AlibabaIntegrationCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** |  | [optional] 
**access_key_secret** | **str** |  | [optional] 
**region_id** | **str** |  | [optional] 
**spi_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.alibaba_integration_credential import AlibabaIntegrationCredential

# TODO update the JSON string below
json = "{}"
# create an instance of AlibabaIntegrationCredential from a JSON string
alibaba_integration_credential_instance = AlibabaIntegrationCredential.from_json(json)
# print the JSON string representation of the object
print AlibabaIntegrationCredential.to_json()

# convert the object into a dict
alibaba_integration_credential_dict = alibaba_integration_credential_instance.to_dict()
# create an instance of AlibabaIntegrationCredential from a dict
alibaba_integration_credential_form_dict = alibaba_integration_credential.from_dict(alibaba_integration_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


