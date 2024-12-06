# StripeBalanceTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Gross amount of this transaction (in cents (or local equivalent)). A positive value represents funds charged to another party, and a negative value represents funds sent to another party. | [optional] 
**available_on** | **int** | The date that the transaction&#39;s net funds become available in the Stripe balance. | [optional] 
**charge_id** | **str** | ID of the charge which the balance transaction comes from. | [optional] 
**created** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**description** | **str** | An arbitrary string attached to the object. Often useful for displaying to users. | [optional] 
**exchange_rate** | **float** | If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the &#x60;amount&#x60; in currency A, multipled by the &#x60;exchange_rate&#x60;, equals the &#x60;amount&#x60; in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent&#39;s &#x60;amount&#x60; is &#x60;1000&#x60; and &#x60;currency&#x60; is &#x60;eur&#x60;. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction&#39;s &#x60;amount&#x60; is &#x60;1234&#x60;, its &#x60;currency&#x60; is &#x60;usd&#x60;, and the &#x60;exchange_rate&#x60; is &#x60;1.234&#x60;. | [optional] 
**fee** | **int** | Fees (in cents (or local equivalent)) paid for this transaction. Represented as a positive integer when assessed. | [optional] 
**fee_details** | [**List[StripeBalanceTransactionFeeDetail]**](StripeBalanceTransactionFeeDetail.md) | Detailed breakdown of fees (in cents (or local equivalent)) paid for this transaction. | [optional] 
**id** | **str** | Unique identifier for the object. | [optional] 
**net** | **int** | Net impact to a Stripe balance (in cents (or local equivalent)). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by &#x60;amount&#x60; - &#x60;fee&#x60; | [optional] 
**status** | **str** | The transaction&#39;s net funds status in the Stripe balance, which are either &#x60;available&#x60; or &#x60;pending&#x60;. | [optional] 
**type** | **str** | Transaction type: &#x60;adjustment&#x60;, &#x60;advance&#x60;, &#x60;advance_funding&#x60;, &#x60;anticipation_repayment&#x60;, &#x60;application_fee&#x60;, &#x60;application_fee_refund&#x60;, &#x60;charge&#x60;, &#x60;climate_order_purchase&#x60;, &#x60;climate_order_refund&#x60;, &#x60;connect_collection_transfer&#x60;, &#x60;contribution&#x60;, &#x60;issuing_authorization_hold&#x60;, &#x60;issuing_authorization_release&#x60;, &#x60;issuing_dispute&#x60;, &#x60;issuing_transaction&#x60;, &#x60;obligation_outbound&#x60;, &#x60;obligation_reversal_inbound&#x60;, &#x60;payment&#x60;, &#x60;payment_failure_refund&#x60;, &#x60;payment_network_reserve_hold&#x60;, &#x60;payment_network_reserve_release&#x60;, &#x60;payment_refund&#x60;, &#x60;payment_reversal&#x60;, &#x60;payment_unreconciled&#x60;, &#x60;payout&#x60;, &#x60;payout_cancel&#x60;, &#x60;payout_failure&#x60;, &#x60;refund&#x60;, &#x60;refund_failure&#x60;, &#x60;reserve_transaction&#x60;, &#x60;reserved_funds&#x60;, &#x60;stripe_fee&#x60;, &#x60;stripe_fx_fee&#x60;, &#x60;tax_fee&#x60;, &#x60;topup&#x60;, &#x60;topup_reversal&#x60;, &#x60;transfer&#x60;, &#x60;transfer_cancel&#x60;, &#x60;transfer_failure&#x60;, or &#x60;transfer_refund&#x60;. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider &#x60;reporting_category&#x60; instead. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_balance_transaction import StripeBalanceTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of StripeBalanceTransaction from a JSON string
stripe_balance_transaction_instance = StripeBalanceTransaction.from_json(json)
# print the JSON string representation of the object
print(StripeBalanceTransaction.to_json())

# convert the object into a dict
stripe_balance_transaction_dict = stripe_balance_transaction_instance.to_dict()
# create an instance of StripeBalanceTransaction from a dict
stripe_balance_transaction_from_dict = StripeBalanceTransaction.from_dict(stripe_balance_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


