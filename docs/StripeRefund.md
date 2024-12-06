# StripeRefund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_id** | **str** | ID of the charge that&#39;s refunded. | [optional] 
**estination_details** | [**StripeRefundDestinationDetails**](StripeRefundDestinationDetails.md) | Transaction-specific details for the refund. | [optional] 
**failure_balance_transaction_id** | **str** | After the refund fails, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction. | [optional] 
**failure_reason** | **str** | Provides the reason for the refund failure. Possible values are: &#x60;lost_or_stolen_card&#x60;, &#x60;expired_or_canceled_card&#x60;, &#x60;charge_for_pending_refund_disputed&#x60;, &#x60;insufficient_funds&#x60;, &#x60;declined&#x60;, &#x60;merchant_request&#x60;, or &#x60;unknown&#x60;. | [optional] 
**id** | **str** |  | [optional] 
**payment_intent_id** | **str** | ID of the PaymentIntent that&#39;s refunded. | [optional] 
**status** | [**StripeRefundStatus**](StripeRefundStatus.md) | Status of the refund. This can be &#x60;pending&#x60;, &#x60;requires_action&#x60;, &#x60;succeeded&#x60;, &#x60;failed&#x60;, or &#x60;canceled&#x60;. Learn more about [failed refunds](https://stripe.com/docs/refunds#failed-refunds). | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_refund import StripeRefund

# TODO update the JSON string below
json = "{}"
# create an instance of StripeRefund from a JSON string
stripe_refund_instance = StripeRefund.from_json(json)
# print the JSON string representation of the object
print(StripeRefund.to_json())

# convert the object into a dict
stripe_refund_dict = stripe_refund_instance.to_dict()
# create an instance of StripeRefund from a dict
stripe_refund_from_dict = StripeRefund.from_dict(stripe_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


