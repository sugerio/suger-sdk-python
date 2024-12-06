# StripePaymentMethodSEPADebit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code** | **str** | Bank code of bank associated with the bank account. | [optional] 
**branch_code** | **str** | Branch code of bank associated with the bank account. | [optional] 
**country** | **str** | Two-letter ISO code representing the country the bank account is located in. | [optional] 
**fingerprint** | **str** | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. | [optional] 
**last4** | **str** | Last four characters of the IBAN. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_payment_method_sepa_debit import StripePaymentMethodSEPADebit

# TODO update the JSON string below
json = "{}"
# create an instance of StripePaymentMethodSEPADebit from a JSON string
stripe_payment_method_sepa_debit_instance = StripePaymentMethodSEPADebit.from_json(json)
# print the JSON string representation of the object
print(StripePaymentMethodSEPADebit.to_json())

# convert the object into a dict
stripe_payment_method_sepa_debit_dict = stripe_payment_method_sepa_debit_instance.to_dict()
# create an instance of StripePaymentMethodSEPADebit from a dict
stripe_payment_method_sepa_debit_from_dict = StripePaymentMethodSEPADebit.from_dict(stripe_payment_method_sepa_debit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


