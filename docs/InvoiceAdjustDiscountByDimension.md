# InvoiceAdjustDiscountByDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_key** | **str** |  | [optional] 
**discount** | [**BillingDiscount**](BillingDiscount.md) |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.invoice_adjust_discount_by_dimension import InvoiceAdjustDiscountByDimension

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustDiscountByDimension from a JSON string
invoice_adjust_discount_by_dimension_instance = InvoiceAdjustDiscountByDimension.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustDiscountByDimension.to_json())

# convert the object into a dict
invoice_adjust_discount_by_dimension_dict = invoice_adjust_discount_by_dimension_instance.to_dict()
# create an instance of InvoiceAdjustDiscountByDimension from a dict
invoice_adjust_discount_by_dimension_from_dict = InvoiceAdjustDiscountByDimension.from_dict(invoice_adjust_discount_by_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


