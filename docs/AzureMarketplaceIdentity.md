# AzureMarketplaceIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_identity import AzureMarketplaceIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceIdentity from a JSON string
azure_marketplace_identity_instance = AzureMarketplaceIdentity.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceIdentity.to_json())

# convert the object into a dict
azure_marketplace_identity_dict = azure_marketplace_identity_instance.to_dict()
# create an instance of AzureMarketplaceIdentity from a dict
azure_marketplace_identity_from_dict = AzureMarketplaceIdentity.from_dict(azure_marketplace_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


