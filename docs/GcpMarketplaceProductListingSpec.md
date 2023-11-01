# GcpMarketplaceProductListingSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_account_spec** | [**GcpMarketplaceProductExternalAccountSpec**](GcpMarketplaceProductExternalAccountSpec.md) |  | [optional] 
**listing_type** | **str** |  | [optional] 
**marketing_spec** | [**GcpMarketplaceProductMarketingSpec**](GcpMarketplaceProductMarketingSpec.md) |  | [optional] 
**purchase_spec** | [**GcpMarketplaceProductPurchaseSpec**](GcpMarketplaceProductPurchaseSpec.md) |  | [optional] 
**terms_spec** | [**GcpMarketplaceProductTermsSpec**](GcpMarketplaceProductTermsSpec.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_listing_spec import GcpMarketplaceProductListingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductListingSpec from a JSON string
gcp_marketplace_product_listing_spec_instance = GcpMarketplaceProductListingSpec.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductListingSpec.to_json()

# convert the object into a dict
gcp_marketplace_product_listing_spec_dict = gcp_marketplace_product_listing_spec_instance.to_dict()
# create an instance of GcpMarketplaceProductListingSpec from a dict
gcp_marketplace_product_listing_spec_form_dict = gcp_marketplace_product_listing_spec.from_dict(gcp_marketplace_product_listing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


