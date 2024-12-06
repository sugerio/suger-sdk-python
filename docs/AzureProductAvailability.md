# AzureProductAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_audiences** | [**List[AzureAudience]**](AzureAudience.md) |  | [optional] 
**enterprise_licensing** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**subscription_audiences** | [**List[AzureAudience]**](AzureAudience.md) |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_availability import AzureProductAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductAvailability from a JSON string
azure_product_availability_instance = AzureProductAvailability.from_json(json)
# print the JSON string representation of the object
print(AzureProductAvailability.to_json())

# convert the object into a dict
azure_product_availability_dict = azure_product_availability_instance.to_dict()
# create an instance of AzureProductAvailability from a dict
azure_product_availability_from_dict = AzureProductAvailability.from_dict(azure_product_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


