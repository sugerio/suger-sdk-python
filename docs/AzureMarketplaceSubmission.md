# AzureMarketplaceSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**created** | **str** | Date-time string | [optional] 
**deprecation_schedule** | [**AzureMarketplaceDeprecationSchedule**](AzureMarketplaceDeprecationSchedule.md) |  | [optional] 
**id** | **str** |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**result** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**target** | [**AzureMarketplaceResourceTarget**](AzureMarketplaceResourceTarget.md) |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_submission import AzureMarketplaceSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceSubmission from a JSON string
azure_marketplace_submission_instance = AzureMarketplaceSubmission.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceSubmission.to_json())

# convert the object into a dict
azure_marketplace_submission_dict = azure_marketplace_submission_instance.to_dict()
# create an instance of AzureMarketplaceSubmission from a dict
azure_marketplace_submission_from_dict = AzureMarketplaceSubmission.from_dict(azure_marketplace_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


