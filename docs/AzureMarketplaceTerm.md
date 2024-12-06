# AzureMarketplaceTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **float** | default 0 | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_term import AzureMarketplaceTerm

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceTerm from a JSON string
azure_marketplace_term_instance = AzureMarketplaceTerm.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceTerm.to_json())

# convert the object into a dict
azure_marketplace_term_dict = azure_marketplace_term_instance.to_dict()
# create an instance of AzureMarketplaceTerm from a dict
azure_marketplace_term_from_dict = AzureMarketplaceTerm.from_dict(azure_marketplace_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


