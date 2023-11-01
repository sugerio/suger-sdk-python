# AzureProductFeatureAvailability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_meters** | [**List[AzureProductVariantCustomMeter]**](AzureProductVariantCustomMeter.md) |  | [optional] 
**id** | **str** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**market_states** | [**List[AzureMarketState]**](AzureMarketState.md) |  | [optional] 
**markets** | [**List[AzureMarket]**](AzureMarket.md) |  | [optional] 
**price_schedules** | [**List[AzureProductVariantPriceSchedule]**](AzureProductVariantPriceSchedule.md) |  | [optional] 
**properties** | [**List[AzureTypeValue]**](AzureTypeValue.md) |  | [optional] 
**resource_type** | **str** | ResourceType &#x3D; FeatureAvailability | [optional] 
**subscription_audiences** | [**List[AzureAudience]**](AzureAudience.md) |  | [optional] 
**tenant_audiences** | [**List[AzureAudience]**](AzureAudience.md) |  | [optional] 
**trial** | [**AzureProductVariantTrial**](AzureProductVariantTrial.md) |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_product_feature_availability import AzureProductFeatureAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductFeatureAvailability from a JSON string
azure_product_feature_availability_instance = AzureProductFeatureAvailability.from_json(json)
# print the JSON string representation of the object
print AzureProductFeatureAvailability.to_json()

# convert the object into a dict
azure_product_feature_availability_dict = azure_product_feature_availability_instance.to_dict()
# create an instance of AzureProductFeatureAvailability from a dict
azure_product_feature_availability_form_dict = azure_product_feature_availability.from_dict(azure_product_feature_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


