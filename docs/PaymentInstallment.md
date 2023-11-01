# PaymentInstallment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount the buyer has paid for this installment. If there is a discount off the original price, the amount is the discounted price. | [optional] 
**charge_on** | **datetime** | When the buyer will be charged for this installment. If it is null, the buyer will be charged on the effective date of the entitlement. | [optional] 
**charge_on_str** | **str** | The charge on date in string format. It is used for front-end display only. | [optional] 
**credit** | **float** | Used in GCP Marketplace private offer as one-time credit. Default as zero if there is no credit. | [optional] 
**discount_percentage** | **float** | The discount percentage off the original price. For GCP Marketplace, it can be discount off the commitment amount or discount off the usage price. The value is between 0 to 100. For example, 20 means 20% off. Default as zero if there is no discount. | [optional] 
**original_amount** | **float** | The original amount before discount if there is a discount off the original price. nil if there is no discount. | [optional] 

## Example

```python
from openapi_client.models.payment_installment import PaymentInstallment

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstallment from a JSON string
payment_installment_instance = PaymentInstallment.from_json(json)
# print the JSON string representation of the object
print PaymentInstallment.to_json()

# convert the object into a dict
payment_installment_dict = payment_installment_instance.to_dict()
# create an instance of PaymentInstallment from a dict
payment_installment_form_dict = payment_installment.from_dict(payment_installment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


