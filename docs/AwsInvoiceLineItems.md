# AwsInvoiceLineItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[AwsInvoiceLineItemDetail]**](AwsInvoiceLineItemDetail.md) |  | [optional] 
**linked_account_allocations** | [**List[AwsInvoiceLinkedAccountAllocation]**](AwsInvoiceLinkedAccountAllocation.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_invoice_line_items import AwsInvoiceLineItems

# TODO update the JSON string below
json = "{}"
# create an instance of AwsInvoiceLineItems from a JSON string
aws_invoice_line_items_instance = AwsInvoiceLineItems.from_json(json)
# print the JSON string representation of the object
print(AwsInvoiceLineItems.to_json())

# convert the object into a dict
aws_invoice_line_items_dict = aws_invoice_line_items_instance.to_dict()
# create an instance of AwsInvoiceLineItems from a dict
aws_invoice_line_items_from_dict = AwsInvoiceLineItems.from_dict(aws_invoice_line_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


