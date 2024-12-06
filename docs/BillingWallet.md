# BillingWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**expire_time** | **datetime** | nullable | [optional] 
**external_id** | **str** | The payment method id in payment provider, such as stripe payment method id. | [optional] 
**id** | **str** |  | [optional] 
**info** | [**BillingWalletInfo**](BillingWalletInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | [**BillingWalletStatus**](BillingWalletStatus.md) |  | [optional] 
**total_amount** | **float** |  | [optional] 
**type** | [**BillingWalletType**](BillingWalletType.md) |  | [optional] 
**used_amount** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_wallet import BillingWallet

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWallet from a JSON string
billing_wallet_instance = BillingWallet.from_json(json)
# print the JSON string representation of the object
print(BillingWallet.to_json())

# convert the object into a dict
billing_wallet_dict = billing_wallet_instance.to_dict()
# create an instance of BillingWallet from a dict
billing_wallet_from_dict = BillingWallet.from_dict(billing_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


