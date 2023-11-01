# AwsMarketplaceCppoPriceTerms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_consumption_unit_column_names** | **List[str]** |  | [optional] 
**detailed_view** | [**AwsMarketplaceCppoPriceTermDetailedView**](AwsMarketplaceCppoPriceTermDetailedView.md) |  | [optional] 
**entries** | [**List[AwsMarketplaceCppoPriceTermEntry]**](AwsMarketplaceCppoPriceTermEntry.md) |  | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_cppo_price_terms import AwsMarketplaceCppoPriceTerms

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoPriceTerms from a JSON string
aws_marketplace_cppo_price_terms_instance = AwsMarketplaceCppoPriceTerms.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceCppoPriceTerms.to_json()

# convert the object into a dict
aws_marketplace_cppo_price_terms_dict = aws_marketplace_cppo_price_terms_instance.to_dict()
# create an instance of AwsMarketplaceCppoPriceTerms from a dict
aws_marketplace_cppo_price_terms_form_dict = aws_marketplace_cppo_price_terms.from_dict(aws_marketplace_cppo_price_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


