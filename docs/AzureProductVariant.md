# AzureProductVariant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_government_certifications** | [**List[AzureGovernmentCertification]**](AzureGovernmentCertification.md) |  | [optional] 
**cloud_availabilities** | **List[str]** |  | [optional] 
**conversion_paths** | **str** |  | [optional] 
**extended_properties** | [**List[AzureTypeValue]**](AzureTypeValue.md) |  | [optional] 
**external_id** | **str** |  | [optional] 
**feature_availabilities** | [**List[AzureProductFeatureAvailability]**](AzureProductFeatureAvailability.md) | Not original fields. They are populated by other API calls | [optional] 
**friendly_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lead_gen_id** | **str** |  | [optional] 
**reference_variant_id** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_product_variant import AzureProductVariant

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductVariant from a JSON string
azure_product_variant_instance = AzureProductVariant.from_json(json)
# print the JSON string representation of the object
print AzureProductVariant.to_json()

# convert the object into a dict
azure_product_variant_dict = azure_product_variant_instance.to_dict()
# create an instance of AzureProductVariant from a dict
azure_product_variant_form_dict = azure_product_variant.from_dict(azure_product_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


