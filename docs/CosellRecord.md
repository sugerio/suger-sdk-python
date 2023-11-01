# CosellRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**info** | **Dict[str, object]** |  | [optional] 
**meta_info** | **Dict[str, object]** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cosell_record import CosellRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CosellRecord from a JSON string
cosell_record_instance = CosellRecord.from_json(json)
# print the JSON string representation of the object
print CosellRecord.to_json()

# convert the object into a dict
cosell_record_dict = cosell_record_instance.to_dict()
# create an instance of CosellRecord from a dict
cosell_record_form_dict = cosell_record.from_dict(cosell_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


