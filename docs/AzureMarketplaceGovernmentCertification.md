# AzureMarketplaceGovernmentCertification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | in patern of \&quot;^(http|https)://\&quot; | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_government_certification import AzureMarketplaceGovernmentCertification

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceGovernmentCertification from a JSON string
azure_marketplace_government_certification_instance = AzureMarketplaceGovernmentCertification.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceGovernmentCertification.to_json())

# convert the object into a dict
azure_marketplace_government_certification_dict = azure_marketplace_government_certification_instance.to_dict()
# create an instance of AzureMarketplaceGovernmentCertification from a dict
azure_marketplace_government_certification_from_dict = AzureMarketplaceGovernmentCertification.from_dict(azure_marketplace_government_certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


