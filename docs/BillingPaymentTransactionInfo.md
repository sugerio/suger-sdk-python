# BillingPaymentTransactionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_date** | **datetime** | The invoice issue date. | [optional] 
**refund_exists** | **bool** | Refund flag marks whether the transaction has any refund records. | [optional] 
**stripe_balance_transaction** | [**StripeBalanceTransaction**](StripeBalanceTransaction.md) | Balance transaction that describes the impact of this charge on your account balance. | [optional] 
**stripe_disputes** | [**List[StripeDispute]**](StripeDispute.md) | Stripe dispute result, got by Dispute API, there may be multiple disputes. | [optional] 
**stripe_error** | [**StripeError**](StripeError.md) | Error of stripe API call | [optional] 
**stripe_payment_intent** | [**StripePaymentIntent**](StripePaymentIntent.md) | Stripe payment intent result, got by PaymentIntent API | [optional] 
**stripe_refund** | [**StripeRefund**](StripeRefund.md) | Stripe refund result, got by Refund API | [optional] 

## Example

```python
from suger_sdk_python.models.billing_payment_transaction_info import BillingPaymentTransactionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPaymentTransactionInfo from a JSON string
billing_payment_transaction_info_instance = BillingPaymentTransactionInfo.from_json(json)
# print the JSON string representation of the object
print(BillingPaymentTransactionInfo.to_json())

# convert the object into a dict
billing_payment_transaction_info_dict = billing_payment_transaction_info_instance.to_dict()
# create an instance of BillingPaymentTransactionInfo from a dict
billing_payment_transaction_info_from_dict = BillingPaymentTransactionInfo.from_dict(billing_payment_transaction_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


