# AzureVariantResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[AzureTypeValue]**](AzureTypeValue.md) |  | [optional] 
**variant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_variant_resource import AzureVariantResource

# TODO update the JSON string below
json = "{}"
# create an instance of AzureVariantResource from a JSON string
azure_variant_resource_instance = AzureVariantResource.from_json(json)
# print the JSON string representation of the object
print AzureVariantResource.to_json()

# convert the object into a dict
azure_variant_resource_dict = azure_variant_resource_instance.to_dict()
# create an instance of AzureVariantResource from a dict
azure_variant_resource_form_dict = azure_variant_resource.from_dict(azure_variant_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


