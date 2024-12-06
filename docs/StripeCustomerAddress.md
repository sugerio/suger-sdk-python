# StripeCustomerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City, district, suburb, town, or village. | [optional] 
**country** | **str** | Two-letter country code (ISO 3166-1 alpha-2) | [optional] 
**line1** | **str** | Address line 1 (e.g., street, PO Box, or company name). | [optional] 
**line2** | **str** | Address line 2 (e.g., apartment, suite, unit, or building). | [optional] 
**postal_code** | **str** | ZIP or postal code. | [optional] 
**state** | **str** | State, county, province, or region. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_customer_address import StripeCustomerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerAddress from a JSON string
stripe_customer_address_instance = StripeCustomerAddress.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerAddress.to_json())

# convert the object into a dict
stripe_customer_address_dict = stripe_customer_address_instance.to_dict()
# create an instance of StripeCustomerAddress from a dict
stripe_customer_address_from_dict = StripeCustomerAddress.from_dict(stripe_customer_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


