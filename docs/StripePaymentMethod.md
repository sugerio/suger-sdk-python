# StripePaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bacs_debit** | [**StripePaymentMethodBACSDebit**](StripePaymentMethodBACSDebit.md) |  | [optional] 
**card** | [**StripePaymentMethodCard**](StripePaymentMethodCard.md) |  | [optional] 
**created** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**id** | **str** | Unique identifier for the payment method on stripe. | [optional] 
**livemode** | **bool** | Has the value &#x60;true&#x60; if the object exists in live mode or the value &#x60;false&#x60; if the object exists in test mode. | [optional] 
**object** | **str** | String representing the object’s type. Always has the value &#x60;payment_method&#x60;. | [optional] 
**sepa_debit** | [**StripePaymentMethodSEPADebit**](StripePaymentMethodSEPADebit.md) |  | [optional] 
**us_bank_account** | [**StripePaymentMethodUSBankAccount**](StripePaymentMethodUSBankAccount.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_payment_method import StripePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of StripePaymentMethod from a JSON string
stripe_payment_method_instance = StripePaymentMethod.from_json(json)
# print the JSON string representation of the object
print(StripePaymentMethod.to_json())

# convert the object into a dict
stripe_payment_method_dict = stripe_payment_method_instance.to_dict()
# create an instance of StripePaymentMethod from a dict
stripe_payment_method_from_dict = StripePaymentMethod.from_dict(stripe_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


