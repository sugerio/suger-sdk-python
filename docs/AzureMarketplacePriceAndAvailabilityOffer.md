# AzureMarketplacePriceAndAvailabilityOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**preview_audiences** | [**List[AzureMarketplacePriceAndAvailabilityAudience]**](AzureMarketplacePriceAndAvailabilityAudience.md) |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_offer import AzureMarketplacePriceAndAvailabilityOffer

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityOffer from a JSON string
azure_marketplace_price_and_availability_offer_instance = AzureMarketplacePriceAndAvailabilityOffer.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilityOffer.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_offer_dict = azure_marketplace_price_and_availability_offer_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityOffer from a dict
azure_marketplace_price_and_availability_offer_form_dict = azure_marketplace_price_and_availability_offer.from_dict(azure_marketplace_price_and_availability_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


