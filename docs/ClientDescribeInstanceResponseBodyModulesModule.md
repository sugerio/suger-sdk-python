# ClientDescribeInstanceResponseBodyModulesModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**properties** | [**ClientDescribeInstanceResponseBodyModulesModuleProperties**](ClientDescribeInstanceResponseBodyModulesModuleProperties.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.client_describe_instance_response_body_modules_module import ClientDescribeInstanceResponseBodyModulesModule

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDescribeInstanceResponseBodyModulesModule from a JSON string
client_describe_instance_response_body_modules_module_instance = ClientDescribeInstanceResponseBodyModulesModule.from_json(json)
# print the JSON string representation of the object
print(ClientDescribeInstanceResponseBodyModulesModule.to_json())

# convert the object into a dict
client_describe_instance_response_body_modules_module_dict = client_describe_instance_response_body_modules_module_instance.to_dict()
# create an instance of ClientDescribeInstanceResponseBodyModulesModule from a dict
client_describe_instance_response_body_modules_module_from_dict = ClientDescribeInstanceResponseBodyModulesModule.from_dict(client_describe_instance_response_body_modules_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


