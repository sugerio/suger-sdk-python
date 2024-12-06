# StripePaymentMethodUSBankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_type** | **str** | Account holder type: individual or company. | [optional] 
**account_type** | **str** | Account type: checkings or savings. Defaults to checking if omitted. | [optional] 
**bank_name** | **str** | The name of the bank. | [optional] 
**fingerprint** | **str** | Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same. | [optional] 
**last4** | **str** | Last four digits of the bank account number. | [optional] 
**routing_number** | **str** | Routing number of the bank account. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_payment_method_us_bank_account import StripePaymentMethodUSBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of StripePaymentMethodUSBankAccount from a JSON string
stripe_payment_method_us_bank_account_instance = StripePaymentMethodUSBankAccount.from_json(json)
# print the JSON string representation of the object
print(StripePaymentMethodUSBankAccount.to_json())

# convert the object into a dict
stripe_payment_method_us_bank_account_dict = stripe_payment_method_us_bank_account_instance.to_dict()
# create an instance of StripePaymentMethodUSBankAccount from a dict
stripe_payment_method_us_bank_account_from_dict = StripePaymentMethodUSBankAccount.from_dict(stripe_payment_method_us_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


