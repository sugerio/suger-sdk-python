# AwsMarketplaceCppoOpportunityPositiveTargeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_accounts** | [**List[AwsMarketplaceBuyerAccount]**](AwsMarketplaceBuyerAccount.md) | List of AWS account IDs that are allowed to subscribe to the offer. | [optional] 
**country_codes** | **List[str]** | List as option for allowing targeting based on country. If the intention isn’t to target the offer to a country, this field should be omitted. If it’s present, the list must contain at least one country code. Each element in this list should be a valid 2-letter country code, using this format: ISO 3166-1 alpha-2. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_cppo_opportunity_positive_targeting import AwsMarketplaceCppoOpportunityPositiveTargeting

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoOpportunityPositiveTargeting from a JSON string
aws_marketplace_cppo_opportunity_positive_targeting_instance = AwsMarketplaceCppoOpportunityPositiveTargeting.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCppoOpportunityPositiveTargeting.to_json())

# convert the object into a dict
aws_marketplace_cppo_opportunity_positive_targeting_dict = aws_marketplace_cppo_opportunity_positive_targeting_instance.to_dict()
# create an instance of AwsMarketplaceCppoOpportunityPositiveTargeting from a dict
aws_marketplace_cppo_opportunity_positive_targeting_from_dict = AwsMarketplaceCppoOpportunityPositiveTargeting.from_dict(aws_marketplace_cppo_opportunity_positive_targeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


