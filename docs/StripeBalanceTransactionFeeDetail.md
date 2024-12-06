# StripeBalanceTransactionFeeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount of the fee, in cents. | [optional] 
**application** | **str** | ID of the Connect application that earned the fee. | [optional] 
**description** | **str** | An arbitrary string attached to the object. Often useful for displaying to users. | [optional] 
**type** | **str** | Type of the fee, one of: &#x60;application_fee&#x60;, &#x60;payment_method_passthrough_fee&#x60;, &#x60;stripe_fee&#x60; or &#x60;tax&#x60;. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_balance_transaction_fee_detail import StripeBalanceTransactionFeeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StripeBalanceTransactionFeeDetail from a JSON string
stripe_balance_transaction_fee_detail_instance = StripeBalanceTransactionFeeDetail.from_json(json)
# print the JSON string representation of the object
print(StripeBalanceTransactionFeeDetail.to_json())

# convert the object into a dict
stripe_balance_transaction_fee_detail_dict = stripe_balance_transaction_fee_detail_instance.to_dict()
# create an instance of StripeBalanceTransactionFeeDetail from a dict
stripe_balance_transaction_fee_detail_from_dict = StripeBalanceTransactionFeeDetail.from_dict(stripe_balance_transaction_fee_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


