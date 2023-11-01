# AzureMarketplacePrivateOfferBeneficiary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiary_recipients** | [**List[AzureMarketplacePrivateOfferBeneficiaryRecipient]**](AzureMarketplacePrivateOfferBeneficiaryRecipient.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** | the customer billing account id. | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_private_offer_beneficiary import AzureMarketplacePrivateOfferBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferBeneficiary from a JSON string
azure_marketplace_private_offer_beneficiary_instance = AzureMarketplacePrivateOfferBeneficiary.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePrivateOfferBeneficiary.to_json()

# convert the object into a dict
azure_marketplace_private_offer_beneficiary_dict = azure_marketplace_private_offer_beneficiary_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferBeneficiary from a dict
azure_marketplace_private_offer_beneficiary_form_dict = azure_marketplace_private_offer_beneficiary.from_dict(azure_marketplace_private_offer_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


