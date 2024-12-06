# AzureProductPackageConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_active_directory_application_id** | **str** |  | [optional] 
**azure_active_directory_tenant_id** | **str** |  | [optional] 
**connection_webhook** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**landing_page_uri** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_package_configuration import AzureProductPackageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductPackageConfiguration from a JSON string
azure_product_package_configuration_instance = AzureProductPackageConfiguration.from_json(json)
# print the JSON string representation of the object
print(AzureProductPackageConfiguration.to_json())

# convert the object into a dict
azure_product_package_configuration_dict = azure_product_package_configuration_instance.to_dict()
# create an instance of AzureProductPackageConfiguration from a dict
azure_product_package_configuration_from_dict = AzureProductPackageConfiguration.from_dict(azure_product_package_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


