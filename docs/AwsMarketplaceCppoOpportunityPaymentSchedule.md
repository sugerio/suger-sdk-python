# AwsMarketplaceCppoOpportunityPaymentSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_amount** | **str** |  | [optional] 
**charge_date** | **datetime** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_cppo_opportunity_payment_schedule import AwsMarketplaceCppoOpportunityPaymentSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoOpportunityPaymentSchedule from a JSON string
aws_marketplace_cppo_opportunity_payment_schedule_instance = AwsMarketplaceCppoOpportunityPaymentSchedule.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCppoOpportunityPaymentSchedule.to_json())

# convert the object into a dict
aws_marketplace_cppo_opportunity_payment_schedule_dict = aws_marketplace_cppo_opportunity_payment_schedule_instance.to_dict()
# create an instance of AwsMarketplaceCppoOpportunityPaymentSchedule from a dict
aws_marketplace_cppo_opportunity_payment_schedule_from_dict = AwsMarketplaceCppoOpportunityPaymentSchedule.from_dict(aws_marketplace_cppo_opportunity_payment_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


