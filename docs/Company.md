# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**contact_email** | **str** | Contact | [optional] 
**country** | **str** | Location information | [optional] 
**creation_time** | **str** | Timestamps | [optional] 
**domain** | **str** |  | [optional] 
**employee_count** | **int** |  | [optional] 
**founded_year** | **str** |  | [optional] 
**id** | **str** | Core identification fields | [optional] 
**industry** | **str** |  | [optional] 
**is_vendor** | **bool** | Vendor flag | [optional] 
**last_update_time** | **str** |  | [optional] 
**linked_in** | **str** | The link to the linkedin profile | [optional] 
**meta_info** | [**CompanyMetaInfo**](CompanyMetaInfo.md) | Additional information about the company populated by Suger, such as partner engagement scores | [optional] 
**name** | **str** | Basic company information | [optional] 
**partner_global_company_contact_ids** | **List[str]** | Partner contacts associated with this buyer company (array of global_company_contact.id values) | [optional] 
**postal_code** | **str** |  | [optional] 
**s3_key_logo** | **str** | Media and social | [optional] 
**short_description** | **str** |  | [optional] 
**state_province** | **str** |  | [optional] 
**status** | [**EnrichmentDataStatus**](EnrichmentDataStatus.md) | active/stale/archived | [optional] 
**street** | **str** |  | [optional] 
**type** | **str** | Private, Public, Nonprofit, Franchise | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


