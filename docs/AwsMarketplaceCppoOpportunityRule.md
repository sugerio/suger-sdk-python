# AwsMarketplaceCppoOpportunityRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_end_date** | **str** |  | [optional] 
**id** | **str** | Output only. | [optional] 
**negative_targeting** | [**AwsMarketplaceCppoOpportunityNegativeTargeting**](AwsMarketplaceCppoOpportunityNegativeTargeting.md) | Negative targeting defines the criteria which any customer&#39;s profile should fulfill to be restricted to access the offer. | [optional] 
**offers_max_quantity** | **int** |  | [optional] 
**positive_targeting** | [**AwsMarketplaceCppoOpportunityPositiveTargeting**](AwsMarketplaceCppoOpportunityPositiveTargeting.md) | Positive targeting defines the criteria which any buyer&#39;s profile should fulfill in order to be allowed to access the offer. | [optional] 
**reseller_account_id** | **str** |  | [optional] 
**reseller_legal_name** | **str** |  | [optional] 
**type** | [**AwsMarketplaceCppoOpportunityRuleType**](AwsMarketplaceCppoOpportunityRuleType.md) |  | [optional] 
**usage** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_cppo_opportunity_rule import AwsMarketplaceCppoOpportunityRule

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoOpportunityRule from a JSON string
aws_marketplace_cppo_opportunity_rule_instance = AwsMarketplaceCppoOpportunityRule.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCppoOpportunityRule.to_json())

# convert the object into a dict
aws_marketplace_cppo_opportunity_rule_dict = aws_marketplace_cppo_opportunity_rule_instance.to_dict()
# create an instance of AwsMarketplaceCppoOpportunityRule from a dict
aws_marketplace_cppo_opportunity_rule_from_dict = AwsMarketplaceCppoOpportunityRule.from_dict(aws_marketplace_cppo_opportunity_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


