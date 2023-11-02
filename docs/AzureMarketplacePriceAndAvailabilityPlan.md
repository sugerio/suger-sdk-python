# AzureMarketplacePriceAndAvailabilityPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**audience** | **str** |  | [optional] 
**billing_tag** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**markets** | **List[str]** |  | [optional] 
**meter_define** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**pricing** | [**AzureMarketplacePriceAndAvailabilityPrice**](AzureMarketplacePriceAndAvailabilityPrice.md) |  | [optional] 
**private_audiences** | [**List[AzureMarketplacePriceAndAvailabilityAudience]**](AzureMarketplacePriceAndAvailabilityAudience.md) |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**software_reservation** | [**List[AzureMarketplacePriceAndAvailabilitySoftwareReservation]**](AzureMarketplacePriceAndAvailabilitySoftwareReservation.md) |  | [optional] 
**trial** | [**AzureMarketplaceTerm**](AzureMarketplaceTerm.md) |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_marketplace_price_and_availability_plan import AzureMarketplacePriceAndAvailabilityPlan

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePriceAndAvailabilityPlan from a JSON string
azure_marketplace_price_and_availability_plan_instance = AzureMarketplacePriceAndAvailabilityPlan.from_json(json)
# print the JSON string representation of the object
print AzureMarketplacePriceAndAvailabilityPlan.to_json()

# convert the object into a dict
azure_marketplace_price_and_availability_plan_dict = azure_marketplace_price_and_availability_plan_instance.to_dict()
# create an instance of AzureMarketplacePriceAndAvailabilityPlan from a dict
azure_marketplace_price_and_availability_plan_form_dict = azure_marketplace_price_and_availability_plan.from_dict(azure_marketplace_price_and_availability_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


