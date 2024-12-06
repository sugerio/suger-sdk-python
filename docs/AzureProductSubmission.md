# AzureProductSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**are_resources_ready** | **bool** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**pending_update_info** | [**AzurePendingUpdateInfo**](AzurePendingUpdateInfo.md) |  | [optional] 
**published_time_in_utc** | **datetime** |  | [optional] 
**release_number** | **int** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**resources** | [**List[AzureTypeValue]**](AzureTypeValue.md) |  | [optional] 
**state** | **str** |  | [optional] 
**sub_state** | **str** |  | [optional] 
**targets** | [**List[AzureTypeValue]**](AzureTypeValue.md) |  | [optional] 
**variant_resources** | [**List[AzureVariantResource]**](AzureVariantResource.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_product_submission import AzureProductSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProductSubmission from a JSON string
azure_product_submission_instance = AzureProductSubmission.from_json(json)
# print the JSON string representation of the object
print(AzureProductSubmission.to_json())

# convert the object into a dict
azure_product_submission_dict = azure_product_submission_instance.to_dict()
# create an instance of AzureProductSubmission from a dict
azure_product_submission_from_dict = AzureProductSubmission.from_dict(azure_product_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


