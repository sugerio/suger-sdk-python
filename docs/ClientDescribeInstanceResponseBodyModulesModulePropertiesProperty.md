# ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_unit** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**property_values** | [**ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues**](ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues.md) |  | [optional] 
**show_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.client_describe_instance_response_body_modules_module_properties_property import ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty from a JSON string
client_describe_instance_response_body_modules_module_properties_property_instance = ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty.from_json(json)
# print the JSON string representation of the object
print ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty.to_json()

# convert the object into a dict
client_describe_instance_response_body_modules_module_properties_property_dict = client_describe_instance_response_body_modules_module_properties_property_instance.to_dict()
# create an instance of ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty from a dict
client_describe_instance_response_body_modules_module_properties_property_form_dict = client_describe_instance_response_body_modules_module_properties_property.from_dict(client_describe_instance_response_body_modules_module_properties_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


