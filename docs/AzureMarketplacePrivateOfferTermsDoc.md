# AzureMarketplacePrivateOfferTermsDoc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_facing_document_name** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**sas_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_private_offer_terms_doc import AzureMarketplacePrivateOfferTermsDoc

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePrivateOfferTermsDoc from a JSON string
azure_marketplace_private_offer_terms_doc_instance = AzureMarketplacePrivateOfferTermsDoc.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePrivateOfferTermsDoc.to_json()

# convert the object into a dict
azure_marketplace_private_offer_terms_doc_dict = azure_marketplace_private_offer_terms_doc_instance.to_dict()
# create an instance of AzureMarketplacePrivateOfferTermsDoc from a dict
azure_marketplace_private_offer_terms_doc_form_dict = azure_marketplace_private_offer_terms_doc.from_dict(azure_marketplace_private_offer_terms_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


