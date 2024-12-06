# AzureMarketplaceCustomerLeads


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**blob_lead_configuration** | **object** |  | [optional] 
**dynamics_lead_configuration** | **object** |  | [optional] 
**email_lead_configuration** | **object** |  | [optional] 
**https_endpoint_lead_configuration** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**lead_destination** | **str** |  | [optional] 
**marketo_lead_configuration** | **object** |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**salesforce_lead_configuration** | **object** |  | [optional] 
**table_lead_configuration** | **object** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_customer_leads import AzureMarketplaceCustomerLeads

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceCustomerLeads from a JSON string
azure_marketplace_customer_leads_instance = AzureMarketplaceCustomerLeads.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceCustomerLeads.to_json())

# convert the object into a dict
azure_marketplace_customer_leads_dict = azure_marketplace_customer_leads_instance.to_dict()
# create an instance of AzureMarketplaceCustomerLeads from a dict
azure_marketplace_customer_leads_from_dict = AzureMarketplaceCustomerLeads.from_dict(azure_marketplace_customer_leads_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


