# BillingDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | [**BillingDiscountType**](BillingDiscountType.md) |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_discount import BillingDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDiscount from a JSON string
billing_discount_instance = BillingDiscount.from_json(json)
# print the JSON string representation of the object
print(BillingDiscount.to_json())

# convert the object into a dict
billing_discount_dict = billing_discount_instance.to_dict()
# create an instance of BillingDiscount from a dict
billing_discount_from_dict = BillingDiscount.from_dict(billing_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


