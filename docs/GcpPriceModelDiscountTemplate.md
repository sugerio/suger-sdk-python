# GcpPriceModelDiscountTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_economics** | **str** |  | [optional] 
**discount_percentage** | [**GcpAmountConstraint**](GcpAmountConstraint.md) |  | [optional] 
**discounted_price** | [**GcpPriceValue**](GcpPriceValue.md) |  | [optional] 
**hide_discount_percentage** | **bool** |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_price_model_discount_template import GcpPriceModelDiscountTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPriceModelDiscountTemplate from a JSON string
gcp_price_model_discount_template_instance = GcpPriceModelDiscountTemplate.from_json(json)
# print the JSON string representation of the object
print(GcpPriceModelDiscountTemplate.to_json())

# convert the object into a dict
gcp_price_model_discount_template_dict = gcp_price_model_discount_template_instance.to_dict()
# create an instance of GcpPriceModelDiscountTemplate from a dict
gcp_price_model_discount_template_from_dict = GcpPriceModelDiscountTemplate.from_dict(gcp_price_model_discount_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


