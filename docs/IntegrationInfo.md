# IntegrationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alibaba_integration** | [**AlibabaMarketplaceIntegration**](AlibabaMarketplaceIntegration.md) |  | [optional] 
**aws_ace_integration** | [**AwsAceIntegration**](AwsAceIntegration.md) |  | [optional] 
**aws_integration** | [**AwsMarketplaceIntegration**](AwsMarketplaceIntegration.md) |  | [optional] 
**azure_integration** | [**AzureIntegration**](AzureIntegration.md) |  | [optional] 
**gcp_integration** | [**GcpIntegration**](GcpIntegration.md) |  | [optional] 
**hubspot_crm_integration** | [**HubspotCrmIntegration**](HubspotCrmIntegration.md) |  | [optional] 
**metronome_integration** | [**MetronomeIntegration**](MetronomeIntegration.md) |  | [optional] 
**orb_integration** | [**OrbIntegration**](OrbIntegration.md) |  | [optional] 
**salesforce_crm_integration** | [**SalesforceCrmIntegration**](SalesforceCrmIntegration.md) |  | [optional] 
**slack_integration** | [**SlackIntegration**](SlackIntegration.md) |  | [optional] 

## Example

```python
from openapi_client.models.integration_info import IntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationInfo from a JSON string
integration_info_instance = IntegrationInfo.from_json(json)
# print the JSON string representation of the object
print IntegrationInfo.to_json()

# convert the object into a dict
integration_info_dict = integration_info_instance.to_dict()
# create an instance of IntegrationInfo from a dict
integration_info_form_dict = integration_info.from_dict(integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


