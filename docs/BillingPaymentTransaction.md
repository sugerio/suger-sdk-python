# BillingPaymentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**buyer_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**BillingPaymentTransactionInfo**](BillingPaymentTransactionInfo.md) |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**status** | [**BillingPaymentStatus**](BillingPaymentStatus.md) |  | [optional] 
**type** | [**BillingPaymentTransactionType**](BillingPaymentTransactionType.md) |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**wallet_type** | [**BillingWalletType**](BillingWalletType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_payment_transaction import BillingPaymentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPaymentTransaction from a JSON string
billing_payment_transaction_instance = BillingPaymentTransaction.from_json(json)
# print the JSON string representation of the object
print(BillingPaymentTransaction.to_json())

# convert the object into a dict
billing_payment_transaction_dict = billing_payment_transaction_instance.to_dict()
# create an instance of BillingPaymentTransaction from a dict
billing_payment_transaction_from_dict = BillingPaymentTransaction.from_dict(billing_payment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


