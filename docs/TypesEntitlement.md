# TypesEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_identifier** | **str** | The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service. | [optional] 
**dimension** | **str** | The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace. | [optional] 
**expiration_date** | **str** | The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date. | [optional] 
**product_code** | **str** | The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created. | [optional] 
**value** | [**TypesEntitlementValue**](TypesEntitlementValue.md) | The EntitlementValue represents the amount of capacity that the customer is entitled to for the product. | [optional] 

## Example

```python
from suger_sdk_python.models.types_entitlement import TypesEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of TypesEntitlement from a JSON string
types_entitlement_instance = TypesEntitlement.from_json(json)
# print the JSON string representation of the object
print(TypesEntitlement.to_json())

# convert the object into a dict
types_entitlement_dict = types_entitlement_instance.to_dict()
# create an instance of TypesEntitlement from a dict
types_entitlement_from_dict = TypesEntitlement.from_dict(types_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


