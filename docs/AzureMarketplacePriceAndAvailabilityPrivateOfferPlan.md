# AzureMarketplacePriceAndAvailabilityPrivateOfferPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**plan_name** | **str** | The azure plan friendly name, from the Azure Marketplace. | [optional] 
**pricing** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPrice**](AzureMarketplacePriceAndAvailabilityPrivateOfferPrice.md) |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_private_offer_plan import AzureMarketplacePriceAndAvailabilityPrivateOfferPlan

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPlan from a JSON string
azure_marketplace_price_and_availability_private_offer_plan_instance = AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_private_offer_plan_dict = azure_marketplace_price_and_availability_private_offer_plan_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPlan from a dict
azure_marketplace_price_and_availability_private_offer_plan_form_dict = azure_marketplace_price_and_availability_private_offer_plan.from_dict(azure_marketplace_price_and_availability_private_offer_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


