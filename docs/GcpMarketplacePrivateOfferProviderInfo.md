# GcpMarketplacePrivateOfferProviderInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_email_address** | **str** | The email address of who create the private offer in the provider. | [optional] 
**sales_contact_email** | **str** | The sales contact email of the provider. | [optional] 
**sales_contact_name** | **str** | The sales contact name of the provider. | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_private_offer_provider_info import GcpMarketplacePrivateOfferProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferProviderInfo from a JSON string
gcp_marketplace_private_offer_provider_info_instance = GcpMarketplacePrivateOfferProviderInfo.from_json(json)
# print the JSON string representation of the object
print GcpMarketplacePrivateOfferProviderInfo.to_json()

# convert the object into a dict
gcp_marketplace_private_offer_provider_info_dict = gcp_marketplace_private_offer_provider_info_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferProviderInfo from a dict
gcp_marketplace_private_offer_provider_info_form_dict = gcp_marketplace_private_offer_provider_info.from_dict(gcp_marketplace_private_offer_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


