# AwsMarketplaceCppoPaymentTerms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**entitlement** | [**List[AwsMarketplaceCppoPaymentTermsEntitlement]**](AwsMarketplaceCppoPaymentTermsEntitlement.md) |  | [optional] 
**schedule** | [**List[AwsMarketplaceCppoPaymentSchedule]**](AwsMarketplaceCppoPaymentSchedule.md) |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**selected_duration** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_cppo_payment_terms import AwsMarketplaceCppoPaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoPaymentTerms from a JSON string
aws_marketplace_cppo_payment_terms_instance = AwsMarketplaceCppoPaymentTerms.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceCppoPaymentTerms.to_json()

# convert the object into a dict
aws_marketplace_cppo_payment_terms_dict = aws_marketplace_cppo_payment_terms_instance.to_dict()
# create an instance of AwsMarketplaceCppoPaymentTerms from a dict
aws_marketplace_cppo_payment_terms_form_dict = aws_marketplace_cppo_payment_terms.from_dict(aws_marketplace_cppo_payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


