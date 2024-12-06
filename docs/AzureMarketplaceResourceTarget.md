# AzureMarketplaceResourceTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_resource_target import AzureMarketplaceResourceTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceResourceTarget from a JSON string
azure_marketplace_resource_target_instance = AzureMarketplaceResourceTarget.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceResourceTarget.to_json())

# convert the object into a dict
azure_marketplace_resource_target_dict = azure_marketplace_resource_target_instance.to_dict()
# create an instance of AzureMarketplaceResourceTarget from a dict
azure_marketplace_resource_target_from_dict = AzureMarketplaceResourceTarget.from_dict(azure_marketplace_resource_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


