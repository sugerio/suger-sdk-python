# StripePaymentIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] 
**last_payment_error** | [**StripeError**](StripeError.md) | The payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason. | [optional] 
**livemode** | **bool** | Has the value &#x60;true&#x60; if the object exists in live mode or the value &#x60;false&#x60; if the object exists in test mode. | [optional] 
**status** | [**StripePaymentIntentStatus**](StripePaymentIntentStatus.md) | Status of this PaymentIntent. Read more about each PaymentIntent [status](https://stripe.com/docs/payments/intents#intent-statuses). | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_payment_intent import StripePaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of StripePaymentIntent from a JSON string
stripe_payment_intent_instance = StripePaymentIntent.from_json(json)
# print the JSON string representation of the object
print(StripePaymentIntent.to_json())

# convert the object into a dict
stripe_payment_intent_dict = stripe_payment_intent_instance.to_dict()
# create an instance of StripePaymentIntent from a dict
stripe_payment_intent_from_dict = StripePaymentIntent.from_dict(stripe_payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


