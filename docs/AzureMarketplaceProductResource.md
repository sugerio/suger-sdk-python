# AzureMarketplaceProductResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_leads** | [**AzureMarketplaceCustomerLeads**](AzureMarketplaceCustomerLeads.md) |  | [optional] 
**listing** | [**AzureMarketplaceListing**](AzureMarketplaceListing.md) |  | [optional] 
**listing_assets** | [**List[AzureMarketplaceListingAsset]**](AzureMarketplaceListingAsset.md) |  | [optional] 
**plans** | [**List[AzureMarketplacePlanResource]**](AzureMarketplacePlanResource.md) |  | [optional] 
**price_and_availability_custom_meter** | [**AzureMarketplacePriceAndAvailabilityCustomMeter**](AzureMarketplacePriceAndAvailabilityCustomMeter.md) |  | [optional] 
**price_and_availability_offer** | [**AzureMarketplacePriceAndAvailabilityOffer**](AzureMarketplacePriceAndAvailabilityOffer.md) |  | [optional] 
**product** | [**AzureMarketplaceProduct**](AzureMarketplaceProduct.md) |  | [optional] 
**var_property** | [**AzureMarketplaceProperty**](AzureMarketplaceProperty.md) |  | [optional] 
**reseller** | [**AzureMarketplaceReseller**](AzureMarketplaceReseller.md) |  | [optional] 
**setup** | [**AzureCommercialMarketplaceSetup**](AzureCommercialMarketplaceSetup.md) |  | [optional] 
**submission** | [**AzureMarketplaceSubmission**](AzureMarketplaceSubmission.md) |  | [optional] 
**technical_configuration** | [**AzureMarketplaceSaasTechnicalConfiguration**](AzureMarketplaceSaasTechnicalConfiguration.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_product_resource import AzureMarketplaceProductResource

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceProductResource from a JSON string
azure_marketplace_product_resource_instance = AzureMarketplaceProductResource.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceProductResource.to_json())

# convert the object into a dict
azure_marketplace_product_resource_dict = azure_marketplace_product_resource_instance.to_dict()
# create an instance of AzureMarketplaceProductResource from a dict
azure_marketplace_product_resource_from_dict = AzureMarketplaceProductResource.from_dict(azure_marketplace_product_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


