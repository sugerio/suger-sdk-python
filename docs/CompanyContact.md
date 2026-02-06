# CompanyContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**company_domain** | **str** |  | [optional] 
**company_name** | **str** | Company information | [optional] 
**country** | **str** | Location information | [optional] 
**creation_time** | **str** | Timestamps | [optional] 
**email** | **str** | Contact information | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **str** | Core identification fields | [optional] 
**info** | [**CompanyContactInfo**](CompanyContactInfo.md) | Additional structured information | [optional] 
**job_function** | **str** |  | [optional] 
**job_title** | **str** | Professional information | [optional] 
**last_name** | **str** |  | [optional] 
**last_update_time** | **str** |  | [optional] 
**linked_in** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**s3_key_picture** | **str** | Media and social | [optional] 
**status** | [**EnrichmentDataStatus**](EnrichmentDataStatus.md) | active/stale/archived | [optional] 
**twitter** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.company_contact import CompanyContact

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyContact from a JSON string
company_contact_instance = CompanyContact.from_json(json)
# print the JSON string representation of the object
print(CompanyContact.to_json())

# convert the object into a dict
company_contact_dict = company_contact_instance.to_dict()
# create an instance of CompanyContact from a dict
company_contact_from_dict = CompanyContact.from_dict(company_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


