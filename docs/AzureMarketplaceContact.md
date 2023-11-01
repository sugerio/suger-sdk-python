# AzureMarketplaceContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**url** | **str** | in patern of \&quot;^(http|https)://\&quot; | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_contact import AzureMarketplaceContact

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceContact from a JSON string
azure_marketplace_contact_instance = AzureMarketplaceContact.from_json(json)
# print the JSON string representation of the object
print AzureMarketplaceContact.to_json()

# convert the object into a dict
azure_marketplace_contact_dict = azure_marketplace_contact_instance.to_dict()
# create an instance of AzureMarketplaceContact from a dict
azure_marketplace_contact_form_dict = azure_marketplace_contact.from_dict(azure_marketplace_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


