# GcpMarketplacePrivateOfferReplacementMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coterm_alignment** | **str** |  | [optional] 
**replaced_offer** | **str** | The resource name of the private offer being replaced. in format of \&quot;projects/{projectNumber}/services/{productServiceName}/privateOffers/{privateOfferId}\&quot; | [optional] 
**replaced_offer_end_time** | **datetime** |  | [optional] 
**replacement_policy** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer_replacement_metadata import GcpMarketplacePrivateOfferReplacementMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferReplacementMetadata from a JSON string
gcp_marketplace_private_offer_replacement_metadata_instance = GcpMarketplacePrivateOfferReplacementMetadata.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOfferReplacementMetadata.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_replacement_metadata_dict = gcp_marketplace_private_offer_replacement_metadata_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferReplacementMetadata from a dict
gcp_marketplace_private_offer_replacement_metadata_form_dict = gcp_marketplace_private_offer_replacement_metadata.from_dict(gcp_marketplace_private_offer_replacement_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


