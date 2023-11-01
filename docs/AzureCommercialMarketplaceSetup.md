# AzureCommercialMarketplaceSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**access_url** | **str** | in patern of \&quot;^(http|https)://\&quot; | [optional] 
**call_to_action** | **str** |  | [optional] 
**id** | **str** | In format of \&quot;commercial-marketplace-setup/setup-durable-id\&quot; | [optional] 
**product** | **str** | Product resource name, in format of \&quot;product/product-durable-id\&quot; | [optional] 
**require_license_for_install** | **bool** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**sell_through_microsoft** | **bool** |  | [optional] 
**use_microsoft_license_management_service** | **bool** | If true, only per_user pricing model is allowed. | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_commercial_marketplace_setup import AzureCommercialMarketplaceSetup

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCommercialMarketplaceSetup from a JSON string
azure_commercial_marketplace_setup_instance = AzureCommercialMarketplaceSetup.from_json(json)
# print the JSON string representation of the object
print AzureCommercialMarketplaceSetup.to_json()

# convert the object into a dict
azure_commercial_marketplace_setup_dict = azure_commercial_marketplace_setup_instance.to_dict()
# create an instance of AzureCommercialMarketplaceSetup from a dict
azure_commercial_marketplace_setup_form_dict = azure_commercial_marketplace_setup.from_dict(azure_commercial_marketplace_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


