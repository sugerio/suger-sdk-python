# AzureMarketplacePrivateOfferBeneficiaryRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_private_offer_beneficiary_recipient import AzureMarketplacePrivateOfferBeneficiaryRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferBeneficiaryRecipient from a JSON string
azure_marketplace_private_offer_beneficiary_recipient_instance = AzureMarketplacePrivateOfferBeneficiaryRecipient.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePrivateOfferBeneficiaryRecipient.to_json())

# convert the object into a dict
azure_marketplace_private_offer_beneficiary_recipient_dict = azure_marketplace_private_offer_beneficiary_recipient_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferBeneficiaryRecipient from a dict
azure_marketplace_private_offer_beneficiary_recipient_from_dict = AzureMarketplacePrivateOfferBeneficiaryRecipient.from_dict(azure_marketplace_private_offer_beneficiary_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


