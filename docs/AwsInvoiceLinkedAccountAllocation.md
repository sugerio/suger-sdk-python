# AwsInvoiceLinkedAccountAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**allocated_total** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**details** | [**List[AwsInvoiceLineItemDetail]**](AwsInvoiceLineItemDetail.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_invoice_linked_account_allocation import AwsInvoiceLinkedAccountAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of AwsInvoiceLinkedAccountAllocation from a JSON string
aws_invoice_linked_account_allocation_instance = AwsInvoiceLinkedAccountAllocation.from_json(json)
# print the JSON string representation of the object
print(AwsInvoiceLinkedAccountAllocation.to_json())

# convert the object into a dict
aws_invoice_linked_account_allocation_dict = aws_invoice_linked_account_allocation_instance.to_dict()
# create an instance of AwsInvoiceLinkedAccountAllocation from a dict
aws_invoice_linked_account_allocation_from_dict = AwsInvoiceLinkedAccountAllocation.from_dict(aws_invoice_linked_account_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


