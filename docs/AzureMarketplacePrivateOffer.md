# AzureMarketplacePrivateOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**accept_by** | **datetime** | in format YYYY-MM-DD | [optional] 
**acceptance_links** | [**List[AzureMarketplacePrivateOfferAcceptanceLink]**](AzureMarketplacePrivateOfferAcceptanceLink.md) |  | [optional] 
**beneficiaries** | [**List[AzureMarketplacePrivateOfferBeneficiary]**](AzureMarketplacePrivateOfferBeneficiary.md) |  | [optional] 
**e_tag** | **str** |  | [optional] 
**end** | **datetime** | in format YYYY-MM-DD | [optional] 
**id** | **str** | in format of \&quot;private-offer/private-offer-durable-id\&quot; | [optional] 
**last_modified** | **datetime** | in format YYYY-MM-DD | [optional] 
**name** | **str** |  | [optional] 
**notification_contacts** | **List[str]** | array of email addresses of the users to be notified of any changes in the private offer status. | [optional] 
**offer_pricing_type** | [**AzureMarketplaceOfferPricingType**](AzureMarketplaceOfferPricingType.md) |  | [optional] 
**partners** | [**List[AzureMarketplacePrivateOfferPartner]**](AzureMarketplacePrivateOfferPartner.md) |  | [optional] 
**prepared_by** | **str** |  | [optional] 
**pricing** | [**List[AzureMarketplacePrivateOfferPricing]**](AzureMarketplacePrivateOfferPricing.md) | Up to 10 pricing entries are allowed. | [optional] 
**private_offer_type** | [**AzureMarketplacePrivateOfferType**](AzureMarketplacePrivateOfferType.md) |  | [optional] 
**resource_name** | **str** |  | [optional] 
**start** | **datetime** | in format YYYY-MM-DD, if VariableStartDate &#x3D; true, this field should be empty. | [optional] 
**state** | [**AzureMarketplacePrivateOfferState**](AzureMarketplacePrivateOfferState.md) |  | [optional] 
**sub_state** | [**AzureMarketplacePrivateOfferSubState**](AzureMarketplacePrivateOfferSubState.md) |  | [optional] 
**terms_and_conditions_doc_sas_url** | **str** | Only applicable to private offers with privateOfferType &#x3D; customerPromotion || cspPromotion | [optional] 
**terms_and_conditions_docs** | [**List[AzureMarketplacePrivateOfferTermsDoc]**](AzureMarketplacePrivateOfferTermsDoc.md) | Only applicable to private offers with privateOfferType &#x3D; multipartyPromotionOriginator || multipartyPromotionChannelPartner | [optional] 
**upgraded_from** | [**AzureMarketplacePrivateOfferPromotionReference**](AzureMarketplacePrivateOfferPromotionReference.md) |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 
**variable_start_date** | **bool** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_private_offer import AzureMarketplacePrivateOffer

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOffer from a JSON string
azure_marketplace_private_offer_instance = AzureMarketplacePrivateOffer.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePrivateOffer.to_json())

# convert the object into a dict
azure_marketplace_private_offer_dict = azure_marketplace_private_offer_instance.to_dict()
# create an instance of AzureMarketplacePrivateOffer from a dict
azure_marketplace_private_offer_from_dict = AzureMarketplacePrivateOffer.from_dict(azure_marketplace_private_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


