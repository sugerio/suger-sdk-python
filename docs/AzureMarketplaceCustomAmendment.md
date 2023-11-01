# AzureMarketplaceCustomAmendment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**AzureMarketplaceCustomAmendmentTenant**](AzureMarketplaceCustomAmendmentTenant.md) |  | [optional] 
**terms** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_custom_amendment import AzureMarketplaceCustomAmendment

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceCustomAmendment from a JSON string
azure_marketplace_custom_amendment_instance = AzureMarketplaceCustomAmendment.from_json(json)
# print the JSON string representation of the object
print AzureMarketplaceCustomAmendment.to_json()

# convert the object into a dict
azure_marketplace_custom_amendment_dict = azure_marketplace_custom_amendment_instance.to_dict()
# create an instance of AzureMarketplaceCustomAmendment from a dict
azure_marketplace_custom_amendment_form_dict = azure_marketplace_custom_amendment.from_dict(azure_marketplace_custom_amendment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


