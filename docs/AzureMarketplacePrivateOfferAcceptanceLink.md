# AzureMarketplacePrivateOfferAcceptanceLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiary_id** | **str** | The Customer Billing Account ID. | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_private_offer_acceptance_link import AzureMarketplacePrivateOfferAcceptanceLink

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferAcceptanceLink from a JSON string
azure_marketplace_private_offer_acceptance_link_instance = AzureMarketplacePrivateOfferAcceptanceLink.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePrivateOfferAcceptanceLink.to_json()

# convert the object into a dict
azure_marketplace_private_offer_acceptance_link_dict = azure_marketplace_private_offer_acceptance_link_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferAcceptanceLink from a dict
azure_marketplace_private_offer_acceptance_link_form_dict = azure_marketplace_private_offer_acceptance_link.from_dict(azure_marketplace_private_offer_acceptance_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


