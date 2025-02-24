# GcpMarketplaceAgreementDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eula_agreement_document** | [**GcpMarketplaceDocument**](GcpMarketplaceDocument.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_agreement_document import GcpMarketplaceAgreementDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceAgreementDocument from a JSON string
gcp_marketplace_agreement_document_instance = GcpMarketplaceAgreementDocument.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceAgreementDocument.to_json())

# convert the object into a dict
gcp_marketplace_agreement_document_dict = gcp_marketplace_agreement_document_instance.to_dict()
# create an instance of GcpMarketplaceAgreementDocument from a dict
gcp_marketplace_agreement_document_from_dict = GcpMarketplaceAgreementDocument.from_dict(gcp_marketplace_agreement_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


