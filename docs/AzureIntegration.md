# AzureIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cma_full_sync_done** | **bool** | Is Azure Commercial Marketplace Analytics (CMA) full-sync done. | [optional] 
**credential** | [**AzureIntegrationCredential**](AzureIntegrationCredential.md) |  | [optional] 
**partner_center_referral_sync_paused** | **bool** | Is Microsoft Partner Center referral sync paused. | [optional] 
**revenue_record_full_sync_done** | **bool** | Is AZURE Marketplace Revenue Record full-sync done. | [optional] 
**secret_key** | **str** | The secret key used to store the AzureIntegrationCredential in AWS Secret manager. for internal usage only. | [optional] 

## Example

```python
from openapi_client.models.azure_integration import AzureIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AzureIntegration from a JSON string
azure_integration_instance = AzureIntegration.from_json(json)
# print the JSON string representation of the object
print AzureIntegration.to_json()

# convert the object into a dict
azure_integration_dict = azure_integration_instance.to_dict()
# create an instance of AzureIntegration from a dict
azure_integration_form_dict = azure_integration.from_dict(azure_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


