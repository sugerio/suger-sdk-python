# AwsInvoiceLineItemDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_invoice_line_item_detail import AwsInvoiceLineItemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AwsInvoiceLineItemDetail from a JSON string
aws_invoice_line_item_detail_instance = AwsInvoiceLineItemDetail.from_json(json)
# print the JSON string representation of the object
print(AwsInvoiceLineItemDetail.to_json())

# convert the object into a dict
aws_invoice_line_item_detail_dict = aws_invoice_line_item_detail_instance.to_dict()
# create an instance of AwsInvoiceLineItemDetail from a dict
aws_invoice_line_item_detail_from_dict = AwsInvoiceLineItemDetail.from_dict(aws_invoice_line_item_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


