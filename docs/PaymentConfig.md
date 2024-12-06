# PaymentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_wallet_types** | [**List[BillingWalletType]**](BillingWalletType.md) | Allowed wallet types for this buyer, include payment methods from payment provider such as card, us_bank_account and credit. | [optional] 
**currency** | **str** | Currency used for billing. | [optional] 
**default_wallet_id** | **str** | Default wallet id which is a stripe payment method used to invoice. | [optional] 

## Example

```python
from suger_sdk_python.models.payment_config import PaymentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentConfig from a JSON string
payment_config_instance = PaymentConfig.from_json(json)
# print the JSON string representation of the object
print(PaymentConfig.to_json())

# convert the object into a dict
payment_config_dict = payment_config_instance.to_dict()
# create an instance of PaymentConfig from a dict
payment_config_from_dict = PaymentConfig.from_dict(payment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


