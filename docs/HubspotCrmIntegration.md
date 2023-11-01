# HubspotCrmIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_fields** | **List[str]** |  | [optional] 
**contact_fields** | **List[str]** |  | [optional] 
**credential** | [**HubspotCrmCredential**](HubspotCrmCredential.md) |  | [optional] 
**deal_fields** | **List[str]** |  | [optional] 
**paused** | **bool** | Paused means the integration is not syncing. | [optional] 
**portal_id** | **int** | Hubspot Account Id | [optional] 
**secret_key** | **str** |  | [optional] 
**sync_filters** | [**List[HubspotSyncFilter]**](HubspotSyncFilter.md) | Can have at most 3 filters which will all be AND-ed. | [optional] 

## Example

```python
from openapi_client.models.hubspot_crm_integration import HubspotCrmIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of HubspotCrmIntegration from a JSON string
hubspot_crm_integration_instance = HubspotCrmIntegration.from_json(json)
# print the JSON string representation of the object
print HubspotCrmIntegration.to_json()

# convert the object into a dict
hubspot_crm_integration_dict = hubspot_crm_integration_instance.to_dict()
# create an instance of HubspotCrmIntegration from a dict
hubspot_crm_integration_form_dict = hubspot_crm_integration.from_dict(hubspot_crm_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


