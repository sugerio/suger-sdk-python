# StripeError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_error import StripeError

# TODO update the JSON string below
json = "{}"
# create an instance of StripeError from a JSON string
stripe_error_instance = StripeError.from_json(json)
# print the JSON string representation of the object
print(StripeError.to_json())

# convert the object into a dict
stripe_error_dict = stripe_error_instance.to_dict()
# create an instance of StripeError from a dict
stripe_error_from_dict = StripeError.from_dict(stripe_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


