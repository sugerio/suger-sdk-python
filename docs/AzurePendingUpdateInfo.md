# AzurePendingUpdateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**update_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_pending_update_info import AzurePendingUpdateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePendingUpdateInfo from a JSON string
azure_pending_update_info_instance = AzurePendingUpdateInfo.from_json(json)
# print the JSON string representation of the object
print AzurePendingUpdateInfo.to_json()

# convert the object into a dict
azure_pending_update_info_dict = azure_pending_update_info_instance.to_dict()
# create an instance of AzurePendingUpdateInfo from a dict
azure_pending_update_info_form_dict = azure_pending_update_info.from_dict(azure_pending_update_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


