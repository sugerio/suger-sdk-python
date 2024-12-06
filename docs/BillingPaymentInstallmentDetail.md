# BillingPaymentInstallmentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_on** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_payment_installment_detail import BillingPaymentInstallmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPaymentInstallmentDetail from a JSON string
billing_payment_installment_detail_instance = BillingPaymentInstallmentDetail.from_json(json)
# print the JSON string representation of the object
print(BillingPaymentInstallmentDetail.to_json())

# convert the object into a dict
billing_payment_installment_detail_dict = billing_payment_installment_detail_instance.to_dict()
# create an instance of BillingPaymentInstallmentDetail from a dict
billing_payment_installment_detail_from_dict = BillingPaymentInstallmentDetail.from_dict(billing_payment_installment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


