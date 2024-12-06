# BillingWalletInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_date** | **datetime** | The close date of the wallet if applicable. | [optional] 
**stripe_payment_method** | [**StripePaymentMethod**](StripePaymentMethod.md) |  | [optional] 
**stripe_setup_intent_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_wallet_info import BillingWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWalletInfo from a JSON string
billing_wallet_info_instance = BillingWalletInfo.from_json(json)
# print the JSON string representation of the object
print(BillingWalletInfo.to_json())

# convert the object into a dict
billing_wallet_info_dict = billing_wallet_info_instance.to_dict()
# create an instance of BillingWalletInfo from a dict
billing_wallet_info_from_dict = BillingWalletInfo.from_dict(billing_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


