# GcpPriceTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_amount** | **float** | such as 0 | [optional] 
**price** | [**GcpPriceValue**](GcpPriceValue.md) |  | [optional] 
**starting_usage_amount** | **str** | such as \&quot;0\&quot; | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_price_tier import GcpPriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPriceTier from a JSON string
gcp_price_tier_instance = GcpPriceTier.from_json(json)
# print the JSON string representation of the object
print(GcpPriceTier.to_json())

# convert the object into a dict
gcp_price_tier_dict = gcp_price_tier_instance.to_dict()
# create an instance of GcpPriceTier from a dict
gcp_price_tier_from_dict = GcpPriceTier.from_dict(gcp_price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


