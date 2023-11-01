# AwsSnsSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**status** | [**AwsSnsSubscriptionStatus**](AwsSnsSubscriptionStatus.md) |  | [optional] 
**subscription_arn** | **str** |  | [optional] 
**topic_arn** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_sns_subscription import AwsSnsSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSnsSubscription from a JSON string
aws_sns_subscription_instance = AwsSnsSubscription.from_json(json)
# print the JSON string representation of the object
print AwsSnsSubscription.to_json()

# convert the object into a dict
aws_sns_subscription_dict = aws_sns_subscription_instance.to_dict()
# create an instance of AwsSnsSubscription from a dict
aws_sns_subscription_form_dict = aws_sns_subscription.from_dict(aws_sns_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


