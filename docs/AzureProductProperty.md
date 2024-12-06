# AzureProductProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_categories** | **List[str]** |  | [optional] 
**app_version** | **str** |  | [optional] 
**applicable_products** | **List[str]** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**custom_amendments** | **List[str]** |  | [optional] 
**extended_properties** | **List[str]** |  | [optional] 
**global_amendment_terms** | **str** |  | [optional] 
**hide_keys** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**industries** | **List[str]** |  | [optional] 
**leveled_categories** | **Dict[str, object]** |  | [optional] 
**leveled_industries** | **Dict[str, object]** |  | [optional] 
**marketing_only_change** | **bool** |  | [optional] 
**product_tags** | **List[str]** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**submission_version** | **str** |  | [optional] 
**terms_of_use** | **str** |  | [optional] 
**use_enterprise_contract** | **bool** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_property import AzureProductProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductProperty from a JSON string
azure_product_property_instance = AzureProductProperty.from_json(json)
# print the JSON string representation of the object
print(AzureProductProperty.to_json())

# convert the object into a dict
azure_product_property_dict = azure_product_property_instance.to_dict()
# create an instance of AzureProductProperty from a dict
azure_product_property_from_dict = AzureProductProperty.from_dict(azure_product_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


