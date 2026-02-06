# CompanyMetaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_engagement_score** | **str** | Partner engagement scores | [optional] 
**azure_engagement_score** | **str** | Azure partner engagement score (High/Medium/Low) | [optional] 
**gcp_engagement_score** | **str** | GCP partner engagement score (High/Medium/Low) | [optional] 

## Example

```python
from suger_sdk_python.models.company_meta_info import CompanyMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyMetaInfo from a JSON string
company_meta_info_instance = CompanyMetaInfo.from_json(json)
# print the JSON string representation of the object
print(CompanyMetaInfo.to_json())

# convert the object into a dict
company_meta_info_dict = company_meta_info_instance.to_dict()
# create an instance of CompanyMetaInfo from a dict
company_meta_info_from_dict = CompanyMetaInfo.from_dict(company_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


