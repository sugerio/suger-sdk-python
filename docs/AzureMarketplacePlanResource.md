# AzureMarketplacePlanResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**AzureMarketplacePlan**](AzureMarketplacePlan.md) |  | [optional] 
**plan_listing** | [**AzureMarketplacePlanListing**](AzureMarketplacePlanListing.md) |  | [optional] 
**price_and_availability_plan** | [**AzureMarketplacePriceAndAvailabilityPlan**](AzureMarketplacePriceAndAvailabilityPlan.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_plan_resource import AzureMarketplacePlanResource

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplacePlanResource from a JSON string
azure_marketplace_plan_resource_instance = AzureMarketplacePlanResource.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplacePlanResource.to_json())

# convert the object into a dict
azure_marketplace_plan_resource_dict = azure_marketplace_plan_resource_instance.to_dict()
# create an instance of AzureMarketplacePlanResource from a dict
azure_marketplace_plan_resource_from_dict = AzureMarketplacePlanResource.from_dict(azure_marketplace_plan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


