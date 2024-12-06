# StripeCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**StripeCustomerAddress**](StripeCustomerAddress.md) |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** | The customer ID on the stripe platform. | [optional] 
**metadata** | **Dict[str, str]** | Set of key-value pairs that you can attach to store additional information about customer. | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_customer import StripeCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomer from a JSON string
stripe_customer_instance = StripeCustomer.from_json(json)
# print the JSON string representation of the object
print(StripeCustomer.to_json())

# convert the object into a dict
stripe_customer_dict = stripe_customer_instance.to_dict()
# create an instance of StripeCustomer from a dict
stripe_customer_from_dict = StripeCustomer.from_dict(stripe_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


