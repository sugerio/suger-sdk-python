# AzureGovernmentCertification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**validation_results** | [**List[AzureValidationResult]**](AzureValidationResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_government_certification import AzureGovernmentCertification

# TODO update the JSON string below
json = "{}"
# create an instance of AzureGovernmentCertification from a JSON string
azure_government_certification_instance = AzureGovernmentCertification.from_json(json)
# print the JSON string representation of the object
print AzureGovernmentCertification.to_json()

# convert the object into a dict
azure_government_certification_dict = azure_government_certification_instance.to_dict()
# create an instance of AzureGovernmentCertification from a dict
azure_government_certification_form_dict = azure_government_certification.from_dict(azure_government_certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


