# CompanyContactInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_experiences** | [**List[WorkExperience]**](WorkExperience.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.company_contact_info import CompanyContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyContactInfo from a JSON string
company_contact_info_instance = CompanyContactInfo.from_json(json)
# print the JSON string representation of the object
print(CompanyContactInfo.to_json())

# convert the object into a dict
company_contact_info_dict = company_contact_info_instance.to_dict()
# create an instance of CompanyContactInfo from a dict
company_contact_info_from_dict = CompanyContactInfo.from_dict(company_contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


