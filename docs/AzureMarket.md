# AzureMarket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendly_name** | **str** |  | [optional] 
**market_code** | **str** | ISO Country Code | [optional] 

## Example

```python
from openapi_client.models.azure_market import AzureMarket

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarket from a JSON string
azure_market_instance = AzureMarket.from_json(json)
# print the JSON string representation of the object
print AzureMarket.to_json()

# convert the object into a dict
azure_market_dict = azure_market_instance.to_dict()
# create an instance of AzureMarket from a dict
azure_market_form_dict = azure_market.from_dict(azure_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


