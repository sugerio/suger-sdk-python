# GcpMarketplacePrivateOfferCustomerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the customer | [optional] 
**contact** | **str** | The contact name of the customer | [optional] 
**email** | **str** | The email address of the customer | [optional] 
**organization** | **str** | The company name of the customer | [optional] 
**unverified_billing_account** | **str** | The GCP billing account ID of the customer | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_private_offer_customer_info import GcpMarketplacePrivateOfferCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplacePrivateOfferCustomerInfo from a JSON string
gcp_marketplace_private_offer_customer_info_instance = GcpMarketplacePrivateOfferCustomerInfo.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplacePrivateOfferCustomerInfo.to_json())

# convert the object into a dict
gcp_marketplace_private_offer_customer_info_dict = gcp_marketplace_private_offer_customer_info_instance.to_dict()
# create an instance of GcpMarketplacePrivateOfferCustomerInfo from a dict
gcp_marketplace_private_offer_customer_info_from_dict = GcpMarketplacePrivateOfferCustomerInfo.from_dict(gcp_marketplace_private_offer_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


