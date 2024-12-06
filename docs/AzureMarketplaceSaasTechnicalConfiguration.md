# AzureMarketplaceSaasTechnicalConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**azure_ad_app_id** | **str** | Azure AD Application Id | [optional] 
**azure_ad_tenant_id** | **str** | Azure AD Tenant Id | [optional] 
**connection_webhook** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**landing_page_url** | **str** |  | [optional] 
**product** | **str** | in format of \&quot;product/product-durable-id\&quot; | [optional] 
**resource_name** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_saas_technical_configuration import AzureMarketplaceSaasTechnicalConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceSaasTechnicalConfiguration from a JSON string
azure_marketplace_saas_technical_configuration_instance = AzureMarketplaceSaasTechnicalConfiguration.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceSaasTechnicalConfiguration.to_json())

# convert the object into a dict
azure_marketplace_saas_technical_configuration_dict = azure_marketplace_saas_technical_configuration_instance.to_dict()
# create an instance of AzureMarketplaceSaasTechnicalConfiguration from a dict
azure_marketplace_saas_technical_configuration_from_dict = AzureMarketplaceSaasTechnicalConfiguration.from_dict(azure_marketplace_saas_technical_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


