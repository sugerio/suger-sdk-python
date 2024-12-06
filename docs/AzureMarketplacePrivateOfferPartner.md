# AzureMarketplacePrivateOfferPartner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**partner_name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_private_offer_partner import AzureMarketplacePrivateOfferPartner

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferPartner from a JSON string
azure_marketplace_private_offer_partner_instance = AzureMarketplacePrivateOfferPartner.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePrivateOfferPartner.to_json())

# convert the object into a dict
azure_marketplace_private_offer_partner_dict = azure_marketplace_private_offer_partner_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferPartner from a dict
azure_marketplace_private_offer_partner_from_dict = AzureMarketplacePrivateOfferPartner.from_dict(azure_marketplace_private_offer_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


