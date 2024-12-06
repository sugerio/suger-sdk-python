# InvoiceAdjustOverallDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**BillingDiscount**](BillingDiscount.md) |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.invoice_adjust_overall_discount import InvoiceAdjustOverallDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustOverallDiscount from a JSON string
invoice_adjust_overall_discount_instance = InvoiceAdjustOverallDiscount.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustOverallDiscount.to_json())

# convert the object into a dict
invoice_adjust_overall_discount_dict = invoice_adjust_overall_discount_instance.to_dict()
# create an instance of InvoiceAdjustOverallDiscount from a dict
invoice_adjust_overall_discount_from_dict = InvoiceAdjustOverallDiscount.from_dict(invoice_adjust_overall_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


