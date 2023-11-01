# CompanyInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**email_domain** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.company_info import CompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfo from a JSON string
company_info_instance = CompanyInfo.from_json(json)
# print the JSON string representation of the object
print CompanyInfo.to_json()

# convert the object into a dict
company_info_dict = company_info_instance.to_dict()
# create an instance of CompanyInfo from a dict
company_info_form_dict = company_info.from_dict(company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


