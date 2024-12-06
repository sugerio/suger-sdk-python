# StripeProductPackageDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | Height, in inches. | [optional] 
**length** | **float** | Length, in inches. | [optional] 
**weight** | **float** | Weight, in ounces. | [optional] 
**width** | **float** | Width, in inches. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_product_package_dimensions import StripeProductPackageDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of StripeProductPackageDimensions from a JSON string
stripe_product_package_dimensions_instance = StripeProductPackageDimensions.from_json(json)
# print the JSON string representation of the object
print(StripeProductPackageDimensions.to_json())

# convert the object into a dict
stripe_product_package_dimensions_dict = stripe_product_package_dimensions_instance.to_dict()
# create an instance of StripeProductPackageDimensions from a dict
stripe_product_package_dimensions_from_dict = StripeProductPackageDimensions.from_dict(stripe_product_package_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


