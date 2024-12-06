# AzureProductBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_draft_instance_id** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**module** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**variant_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_branch import AzureProductBranch

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductBranch from a JSON string
azure_product_branch_instance = AzureProductBranch.from_json(json)
# print the JSON string representation of the object
print(AzureProductBranch.to_json())

# convert the object into a dict
azure_product_branch_dict = azure_product_branch_instance.to_dict()
# create an instance of AzureProductBranch from a dict
azure_product_branch_from_dict = AzureProductBranch.from_dict(azure_product_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


