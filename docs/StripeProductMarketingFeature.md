# StripeProductMarketingFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The marketing feature name. Up to 80 characters long. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_product_marketing_feature import StripeProductMarketingFeature

# TODO update the JSON string below
json = "{}"
# create an instance of StripeProductMarketingFeature from a JSON string
stripe_product_marketing_feature_instance = StripeProductMarketingFeature.from_json(json)
# print the JSON string representation of the object
print(StripeProductMarketingFeature.to_json())

# convert the object into a dict
stripe_product_marketing_feature_dict = stripe_product_marketing_feature_instance.to_dict()
# create an instance of StripeProductMarketingFeature from a dict
stripe_product_marketing_feature_from_dict = StripeProductMarketingFeature.from_dict(stripe_product_marketing_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


