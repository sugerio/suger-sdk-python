# AzureProductVariantTrial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time_range** | [**AzureLocalizedTimeRange**](AzureLocalizedTimeRange.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**duration_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_variant_trial import AzureProductVariantTrial

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductVariantTrial from a JSON string
azure_product_variant_trial_instance = AzureProductVariantTrial.from_json(json)
# print the JSON string representation of the object
print(AzureProductVariantTrial.to_json())

# convert the object into a dict
azure_product_variant_trial_dict = azure_product_variant_trial_instance.to_dict()
# create an instance of AzureProductVariantTrial from a dict
azure_product_variant_trial_from_dict = AzureProductVariantTrial.from_dict(azure_product_variant_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


