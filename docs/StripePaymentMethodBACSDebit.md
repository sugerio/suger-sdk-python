# StripePaymentMethodBACSDebit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. | [optional] 
**last4** | **str** | Last four digits of the bank account number. | [optional] 
**sort_code** | **str** | Sort code of the bank account. (e.g., &#x60;10-20-30&#x60;) | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_payment_method_bacs_debit import StripePaymentMethodBACSDebit

# TODO update the JSON string below
json = "{}"
# create an instance of StripePaymentMethodBACSDebit from a JSON string
stripe_payment_method_bacs_debit_instance = StripePaymentMethodBACSDebit.from_json(json)
# print the JSON string representation of the object
print(StripePaymentMethodBACSDebit.to_json())

# convert the object into a dict
stripe_payment_method_bacs_debit_dict = stripe_payment_method_bacs_debit_instance.to_dict()
# create an instance of StripePaymentMethodBACSDebit from a dict
stripe_payment_method_bacs_debit_from_dict = StripePaymentMethodBACSDebit.from_dict(stripe_payment_method_bacs_debit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


