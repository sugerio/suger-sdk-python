# AwsInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AWS Account ID (12 digits) | [optional] 
**amount_due** | **float** | Outstanding balance | [optional] 
**billing_entity** | **str** | AWS or AWS_MARKETPLACE - single source of truth for invoice type | [optional] 
**billing_month** | **int** | Month number (1-12) | [optional] 
**billing_period_end** | **str** | End of billing period | [optional] 
**billing_period_start** | **str** | Start of billing period | [optional] 
**billing_year** | **int** | Year (YYYY) | [optional] 
**charge_type** | **str** | Anniversary (AWS) or Subscription (Marketplace) | [optional] 
**currency_code** | **str** | CurrencyCode holds the value of the \&quot;currency_code\&quot; field. | [optional] 
**due_date** | **str** | Payment due date | [optional] 
**id** | **str** | AWS invoice ID (e.g., &#39;2289273833&#39;) | [optional] 
**invoice_type** | **str** | INVOICE or CREDIT_MEMO | [optional] 
**issued_date** | **str** | When invoice was issued | [optional] 
**line_items** | [**AwsInvoiceLineItems**](AwsInvoiceLineItems.md) | Extracted line items from PDF processing | [optional] 
**pdf_downloaded** | **bool** | PDF download status | [optional] 
**settle_date** | **str** | Invoice settle date | [optional] 
**status** | **str** | Due, PastDue, Scheduled, Processing, Paid | [optional] 
**sync_timestamp** | **str** | SyncTimestamp holds the value of the \&quot;sync_timestamp\&quot; field. | [optional] 
**system_identifier_arn** | **str** | ARN from console API (e.g., arn:aws:payments:us-east-1:account:invoice:id) | [optional] 
**tax_amount** | **float** | Tax amount | [optional] 
**total_amount** | **float** | Total invoice amount | [optional] 
**total_amount_before_tax** | **float** | Subtotal before tax | [optional] 
**transaction_status** | **str** | Forgive, Successful, or Unknown | [optional] 

## Example

```python
from suger_sdk_python.models.aws_invoice import AwsInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of AwsInvoice from a JSON string
aws_invoice_instance = AwsInvoice.from_json(json)
# print the JSON string representation of the object
print(AwsInvoice.to_json())

# convert the object into a dict
aws_invoice_dict = aws_invoice_instance.to_dict()
# create an instance of AwsInvoice from a dict
aws_invoice_from_dict = AwsInvoice.from_dict(aws_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


