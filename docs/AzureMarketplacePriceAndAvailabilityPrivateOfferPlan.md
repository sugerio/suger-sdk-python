# AzureMarketplacePriceAndAvailabilityPrivateOfferPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**offer_pricing_type** | [**AzureMarketplaceOfferPricingType**](AzureMarketplaceOfferPricingType.md) | default \&quot;editExistingOfferPricingOnly\&quot; | [optional] 
**plan** | **str** |  | [optional] 
**plan_name** | **str** | The azure plan friendly name, from the Azure Marketplace. | [optional] 
**pricing** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPrice**](AzureMarketplacePriceAndAvailabilityPrivateOfferPrice.md) |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**software_reservation** | [**AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlanSoftwareReservation.md) |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 
**visibility** | **str** | default \&quot;visible\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_price_and_availability_private_offer_plan import AzureMarketplacePriceAndAvailabilityPrivateOfferPlan

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPlan from a JSON string
azure_marketplace_price_and_availability_private_offer_plan_instance = AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.to_json())

# convert the object into a dict
azure_marketplace_price_and_availability_private_offer_plan_dict = azure_marketplace_price_and_availability_private_offer_plan_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPlan from a dict
azure_marketplace_price_and_availability_private_offer_plan_from_dict = AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.from_dict(azure_marketplace_price_and_availability_private_offer_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


