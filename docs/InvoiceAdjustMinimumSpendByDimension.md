# InvoiceAdjustMinimumSpendByDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_key** | **str** |  | [optional] 
**minimum_spend** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.invoice_adjust_minimum_spend_by_dimension import InvoiceAdjustMinimumSpendByDimension

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustMinimumSpendByDimension from a JSON string
invoice_adjust_minimum_spend_by_dimension_instance = InvoiceAdjustMinimumSpendByDimension.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustMinimumSpendByDimension.to_json())

# convert the object into a dict
invoice_adjust_minimum_spend_by_dimension_dict = invoice_adjust_minimum_spend_by_dimension_instance.to_dict()
# create an instance of InvoiceAdjustMinimumSpendByDimension from a dict
invoice_adjust_minimum_spend_by_dimension_from_dict = InvoiceAdjustMinimumSpendByDimension.from_dict(invoice_adjust_minimum_spend_by_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


