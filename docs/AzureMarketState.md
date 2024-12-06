# AzureMarketState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_code** | **str** | ISO Country Code | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_market_state import AzureMarketState

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketState from a JSON string
azure_market_state_instance = AzureMarketState.from_json(json)
# print the JSON string representation of the object
print(AzureMarketState.to_json())

# convert the object into a dict
azure_market_state_dict = azure_market_state_instance.to_dict()
# create an instance of AzureMarketState from a dict
azure_market_state_from_dict = AzureMarketState.from_dict(azure_market_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


