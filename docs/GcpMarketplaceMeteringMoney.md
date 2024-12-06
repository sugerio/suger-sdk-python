# GcpMarketplaceMeteringMoney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | CurrencyCode: The three-letter currency code defined in ISO 4217. | [optional] 
**nanos** | **int** | Nanos: Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If &#x60;units&#x60; is positive, &#x60;nanos&#x60; must be positive or zero. If &#x60;units&#x60; is zero, &#x60;nanos&#x60; can be positive, zero, or negative. If &#x60;units&#x60; is negative, &#x60;nanos&#x60; must be negative or zero. For example $-1.75 is represented as &#x60;units&#x60;&#x3D;-1 and &#x60;nanos&#x60;&#x3D;-750,000,000. | [optional] 
**units** | **str** | Units: The whole units of the amount. For example if &#x60;currencyCode&#x60; is \&quot;USD\&quot;, then 1 unit is one US dollar. | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_metering_money import GcpMarketplaceMeteringMoney

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceMeteringMoney from a JSON string
gcp_marketplace_metering_money_instance = GcpMarketplaceMeteringMoney.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceMeteringMoney.to_json())

# convert the object into a dict
gcp_marketplace_metering_money_dict = gcp_marketplace_metering_money_instance.to_dict()
# create an instance of GcpMarketplaceMeteringMoney from a dict
gcp_marketplace_metering_money_from_dict = GcpMarketplaceMeteringMoney.from_dict(gcp_marketplace_metering_money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


