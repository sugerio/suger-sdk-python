# AwsPaymentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AWS Account ID (payer) | [optional] 
**amount** | **float** | Payment amount (positive for payments, negative for refunds) | [optional] 
**billing_entity** | **str** | BillingEntity holds the value of the \&quot;billing_entity\&quot; field. | [optional] 
**billing_period_end** | **str** | End of billing period this payment covers | [optional] 
**billing_period_start** | **str** | Start of billing period this payment covers | [optional] 
**charge_type** | **str** | Anniversary (AWS) or Subscription (Marketplace) | [optional] 
**currency_code** | **str** | CurrencyCode holds the value of the \&quot;currency_code\&quot; field. | [optional] 
**id** | **str** |  | [optional] 
**invoice_id** | **str** | Links to buyer_aws_invoice.invoice_id | [optional] 
**organization_id** | **str** | OrganizationID holds the value of the \&quot;organization_id\&quot; field. | [optional] 
**payment_method_description** | **str** | User-friendly description (e.g., &#39;Bank account ending in 901&#39;) | [optional] 
**payment_method_type** | **str** | BankAccount or CreditCard | [optional] 
**sync_timestamp** | **str** | SyncTimestamp holds the value of the \&quot;sync_timestamp\&quot; field. | [optional] 
**system_identifier_arn** | **str** | ARN from console API | [optional] 
**transaction_date** | **str** | When payment was processed | [optional] 
**transaction_type** | **str** | TransactionType holds the value of the \&quot;transaction_type\&quot; field. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_payment_transaction import AwsPaymentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPaymentTransaction from a JSON string
aws_payment_transaction_instance = AwsPaymentTransaction.from_json(json)
# print the JSON string representation of the object
print(AwsPaymentTransaction.to_json())

# convert the object into a dict
aws_payment_transaction_dict = aws_payment_transaction_instance.to_dict()
# create an instance of AwsPaymentTransaction from a dict
aws_payment_transaction_from_dict = AwsPaymentTransaction.from_dict(aws_payment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


