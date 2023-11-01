# CreateUsageRecordGroupParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_id** | **str** |  | 
**id** | **str** | The uuid of the UsageRecordGroup (the size is up to 36 characters). Optional, if not provided, suger will generate one. | [optional] 
**meta_info** | [**MeteringUsageRecordGroupMetaInfo**](MeteringUsageRecordGroupMetaInfo.md) |  | [optional] 
**organization_id** | **str** |  | 
**records** | **Dict[str, float]** |  | 
**timestamp** | **datetime** | The timestamp of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. This is not the timestamp of when the usage records were reported to Suger. | [optional] 

## Example

```python
from openapi_client.models.create_usage_record_group_params import CreateUsageRecordGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsageRecordGroupParams from a JSON string
create_usage_record_group_params_instance = CreateUsageRecordGroupParams.from_json(json)
# print the JSON string representation of the object
print CreateUsageRecordGroupParams.to_json()

# convert the object into a dict
create_usage_record_group_params_dict = create_usage_record_group_params_instance.to_dict()
# create an instance of CreateUsageRecordGroupParams from a dict
create_usage_record_group_params_form_dict = create_usage_record_group_params.from_dict(create_usage_record_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


