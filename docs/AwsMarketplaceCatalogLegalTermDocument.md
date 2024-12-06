# AwsMarketplaceCatalogLegalTermDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AwsMarketplaceCatalogLegalTermDocumentType**](AwsMarketplaceCatalogLegalTermDocumentType.md) |  | [optional] 
**url** | **str** | A URL to the legal document for buyers to read. Required when Type is one of the following [CustomEula, CustomDsa]. | [optional] 
**version** | **str** | Version of standard contracts provided by AWS Marketplace. Required when Type is one of the following [StandardEula, StandardDsa]. The version of StandardEula is \&quot;2022-07-14\&quot;. The version of StandardDsa is \&quot;2019-12-12\&quot;. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_catalog_legal_term_document import AwsMarketplaceCatalogLegalTermDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCatalogLegalTermDocument from a JSON string
aws_marketplace_catalog_legal_term_document_instance = AwsMarketplaceCatalogLegalTermDocument.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCatalogLegalTermDocument.to_json())

# convert the object into a dict
aws_marketplace_catalog_legal_term_document_dict = aws_marketplace_catalog_legal_term_document_instance.to_dict()
# create an instance of AwsMarketplaceCatalogLegalTermDocument from a dict
aws_marketplace_catalog_legal_term_document_from_dict = AwsMarketplaceCatalogLegalTermDocument.from_dict(aws_marketplace_catalog_legal_term_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


