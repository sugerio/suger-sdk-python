# InvoiceAdjustOverallMinimumSpend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_spend** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.invoice_adjust_overall_minimum_spend import InvoiceAdjustOverallMinimumSpend

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustOverallMinimumSpend from a JSON string
invoice_adjust_overall_minimum_spend_instance = InvoiceAdjustOverallMinimumSpend.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustOverallMinimumSpend.to_json())

# convert the object into a dict
invoice_adjust_overall_minimum_spend_dict = invoice_adjust_overall_minimum_spend_instance.to_dict()
# create an instance of InvoiceAdjustOverallMinimumSpend from a dict
invoice_adjust_overall_minimum_spend_from_dict = InvoiceAdjustOverallMinimumSpend.from_dict(invoice_adjust_overall_minimum_spend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


