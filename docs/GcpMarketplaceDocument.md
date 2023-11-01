# GcpMarketplaceDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**document_type** | **str** | such as \&quot;PARTNER_EULA\&quot; | [optional] 
**external_google_link** | [**GcpMarketplaceExternalGoogleLink**](GcpMarketplaceExternalGoogleLink.md) |  | [optional] 
**name** | **str** | in format of \&quot;projects/{projectNumber}/agreements/{agreementId}/documents/{documentId}\&quot; | [optional] 
**unstructured_document** | [**GcpMarketplaceUnstructuredDocument**](GcpMarketplaceUnstructuredDocument.md) |  | [optional] 
**update_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_document import GcpMarketplaceDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceDocument from a JSON string
gcp_marketplace_document_instance = GcpMarketplaceDocument.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceDocument.to_json()

# convert the object into a dict
gcp_marketplace_document_dict = gcp_marketplace_document_instance.to_dict()
# create an instance of GcpMarketplaceDocument from a dict
gcp_marketplace_document_form_dict = gcp_marketplace_document.from_dict(gcp_marketplace_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


