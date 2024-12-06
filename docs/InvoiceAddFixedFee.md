# InvoiceAddFixedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** |  | [optional] 
**quantity** | **int** |  | [optional] 
**rate** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from suger_sdk_python.models.invoice_add_fixed_fee import InvoiceAddFixedFee

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAddFixedFee from a JSON string
invoice_add_fixed_fee_instance = InvoiceAddFixedFee.from_json(json)
# print the JSON string representation of the object
print(InvoiceAddFixedFee.to_json())

# convert the object into a dict
invoice_add_fixed_fee_dict = invoice_add_fixed_fee_instance.to_dict()
# create an instance of InvoiceAddFixedFee from a dict
invoice_add_fixed_fee_from_dict = InvoiceAddFixedFee.from_dict(invoice_add_fixed_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


