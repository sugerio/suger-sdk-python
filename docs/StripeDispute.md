# StripeDispute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed). | [optional] 
**charge_id** | **str** | ID of the charge that&#39;s disputed. | [optional] 
**created** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**id** | **str** | Unique identifier for the object. | [optional] 
**is_charge_refundable** | **bool** | If true, it&#39;s still possible to refund the disputed payment. After the payment has been fully refunded, no further funds are withdrawn from your Stripe account as a result of this dispute. | [optional] 
**livemode** | **bool** | Has the value &#x60;true&#x60; if the object exists in live mode or the value &#x60;false&#x60; if the object exists in test mode. | [optional] 
**payment_intent_id** | **str** | ID of the PaymentIntent that&#39;s disputed. | [optional] 
**reason** | **str** | Reason given by cardholder for dispute. Possible values are &#x60;bank_cannot_process&#x60;, &#x60;check_returned&#x60;, &#x60;credit_not_processed&#x60;, &#x60;customer_initiated&#x60;, &#x60;debit_not_authorized&#x60;, &#x60;duplicate&#x60;, &#x60;fraudulent&#x60;, &#x60;general&#x60;, &#x60;incorrect_account_details&#x60;, &#x60;insufficient_funds&#x60;, &#x60;product_not_received&#x60;, &#x60;product_unacceptable&#x60;, &#x60;subscription_canceled&#x60;, or &#x60;unrecognized&#x60;. Learn more about [dispute reasons](https://stripe.com/docs/disputes/categories). | [optional] 
**status** | **str** | Current status of dispute. Possible values are &#x60;warning_needs_response&#x60;, &#x60;warning_under_review&#x60;, &#x60;warning_closed&#x60;, &#x60;needs_response&#x60;, &#x60;under_review&#x60;, &#x60;won&#x60;, or &#x60;lost&#x60;. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_dispute import StripeDispute

# TODO update the JSON string below
json = "{}"
# create an instance of StripeDispute from a JSON string
stripe_dispute_instance = StripeDispute.from_json(json)
# print the JSON string representation of the object
print(StripeDispute.to_json())

# convert the object into a dict
stripe_dispute_dict = stripe_dispute_instance.to_dict()
# create an instance of StripeDispute from a dict
stripe_dispute_from_dict = StripeDispute.from_dict(stripe_dispute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


