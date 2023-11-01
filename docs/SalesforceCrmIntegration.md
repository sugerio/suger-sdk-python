# SalesforceCrmIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**SalesforceCrmCredential**](SalesforceCrmCredential.md) |  | [optional] 
**filters** | [**List[SalesforceSyncFilter]**](SalesforceSyncFilter.md) |  | [optional] 
**instance_url** | **str** |  | [optional] 
**is_sandbox** | **bool** |  | [optional] 
**paused** | **bool** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**subdomain** | **str** | User defined when setting up the integration | [optional] 
**suger_app_installed** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_crm_integration import SalesforceCrmIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceCrmIntegration from a JSON string
salesforce_crm_integration_instance = SalesforceCrmIntegration.from_json(json)
# print the JSON string representation of the object
print SalesforceCrmIntegration.to_json()

# convert the object into a dict
salesforce_crm_integration_dict = salesforce_crm_integration_instance.to_dict()
# create an instance of SalesforceCrmIntegration from a dict
salesforce_crm_integration_form_dict = salesforce_crm_integration.from_dict(salesforce_crm_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


