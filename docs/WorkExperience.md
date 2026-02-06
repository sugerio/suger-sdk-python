# WorkExperience


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **bool** | true if the work experience is current | [optional] 
**end_date** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.work_experience import WorkExperience

# TODO update the JSON string below
json = "{}"
# create an instance of WorkExperience from a JSON string
work_experience_instance = WorkExperience.from_json(json)
# print the JSON string representation of the object
print(WorkExperience.to_json())

# convert the object into a dict
work_experience_dict = work_experience_instance.to_dict()
# create an instance of WorkExperience from a dict
work_experience_from_dict = WorkExperience.from_dict(work_experience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


