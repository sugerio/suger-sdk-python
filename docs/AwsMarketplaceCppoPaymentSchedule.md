# AwsMarketplaceCppoPaymentSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_on** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_cppo_payment_schedule import AwsMarketplaceCppoPaymentSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoPaymentSchedule from a JSON string
aws_marketplace_cppo_payment_schedule_instance = AwsMarketplaceCppoPaymentSchedule.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceCppoPaymentSchedule.to_json()

# convert the object into a dict
aws_marketplace_cppo_payment_schedule_dict = aws_marketplace_cppo_payment_schedule_instance.to_dict()
# create an instance of AwsMarketplaceCppoPaymentSchedule from a dict
aws_marketplace_cppo_payment_schedule_form_dict = aws_marketplace_cppo_payment_schedule.from_dict(aws_marketplace_cppo_payment_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


