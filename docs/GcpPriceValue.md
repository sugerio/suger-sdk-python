# GcpPriceValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | such as \&quot;USD\&quot; | [optional] 
**nanos** | **int** | for the decimal part, such as 30000000 &#x3D; $0.03 | [optional] 
**units** | **str** | for the integer part, such as \&quot;500000\&quot; &#x3D; $50K | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_price_value import GcpPriceValue

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPriceValue from a JSON string
gcp_price_value_instance = GcpPriceValue.from_json(json)
# print the JSON string representation of the object
print(GcpPriceValue.to_json())

# convert the object into a dict
gcp_price_value_dict = gcp_price_value_instance.to_dict()
# create an instance of GcpPriceValue from a dict
gcp_price_value_from_dict = GcpPriceValue.from_dict(gcp_price_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


