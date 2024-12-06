# AzureProductVariantCustomMeter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**included_base_quantities** | [**List[AzureIncludedBaseQuantity]**](AzureIncludedBaseQuantity.md) |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**price_in_usd** | **float** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_variant_custom_meter import AzureProductVariantCustomMeter

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductVariantCustomMeter from a JSON string
azure_product_variant_custom_meter_instance = AzureProductVariantCustomMeter.from_json(json)
# print the JSON string representation of the object
print(AzureProductVariantCustomMeter.to_json())

# convert the object into a dict
azure_product_variant_custom_meter_dict = azure_product_variant_custom_meter_instance.to_dict()
# create an instance of AzureProductVariantCustomMeter from a dict
azure_product_variant_custom_meter_from_dict = AzureProductVariantCustomMeter.from_dict(azure_product_variant_custom_meter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


