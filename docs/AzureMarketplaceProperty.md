# AzureMarketplaceProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**categories** | **Dict[str, List[str]]** |  | [optional] 
**cloud_industries** | **Dict[str, List[str]]** |  | [optional] 
**custom_amendments** | [**List[AzureMarketplaceCustomAmendment]**](AzureMarketplaceCustomAmendment.md) |  | [optional] 
**id** | **str** |  | [optional] 
**industries** | **Dict[str, List[str]]** |  | [optional] 
**kind** | **str** |  | [optional] 
**lifecycle_state** | [**AzureMarketplaceResourceLifecycleState**](AzureMarketplaceResourceLifecycleState.md) |  | [optional] 
**product** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**standard_contract_amendment** | **str** |  | [optional] 
**terms_conditions** | **str** |  | [optional] 
**terms_of_use** | **str** |  | [optional] 
**terms_of_use_url** | **str** |  | [optional] 
**validations** | [**List[AzureMarketplaceValidation]**](AzureMarketplaceValidation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_property import AzureMarketplaceProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceProperty from a JSON string
azure_marketplace_property_instance = AzureMarketplaceProperty.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceProperty.to_json())

# convert the object into a dict
azure_marketplace_property_dict = azure_marketplace_property_instance.to_dict()
# create an instance of AzureMarketplaceProperty from a dict
azure_marketplace_property_from_dict = AzureMarketplaceProperty.from_dict(azure_marketplace_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


