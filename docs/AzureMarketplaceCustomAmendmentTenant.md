# AzureMarketplaceCustomAmendmentTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_entries** | [**List[AzureMarketplaceCustomAmendmentTenantManualEntry]**](AzureMarketplaceCustomAmendmentTenantManualEntry.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_custom_amendment_tenant import AzureMarketplaceCustomAmendmentTenant

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceCustomAmendmentTenant from a JSON string
azure_marketplace_custom_amendment_tenant_instance = AzureMarketplaceCustomAmendmentTenant.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceCustomAmendmentTenant.to_json())

# convert the object into a dict
azure_marketplace_custom_amendment_tenant_dict = azure_marketplace_custom_amendment_tenant_instance.to_dict()
# create an instance of AzureMarketplaceCustomAmendmentTenant from a dict
azure_marketplace_custom_amendment_tenant_from_dict = AzureMarketplaceCustomAmendmentTenant.from_dict(azure_marketplace_custom_amendment_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


