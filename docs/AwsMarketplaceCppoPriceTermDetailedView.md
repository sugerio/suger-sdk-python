# AwsMarketplaceCppoPriceTermDetailedView


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_consumption_unit_column_names** | **List[str]** | For Usage metering dimensions | [optional] 
**additional_consumption_unit_entries** | [**List[AwsMarketplaceCppoPriceTermEntry]**](AwsMarketplaceCppoPriceTermEntry.md) | For Usage metering dimensions | [optional] 
**consumption_unit_column_names** | **List[str]** | For Commit dimensions | [optional] 
**consumption_unit_entries** | [**List[AwsMarketplaceCppoPriceTermEntry]**](AwsMarketplaceCppoPriceTermEntry.md) | For Commit dimensions | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_cppo_price_term_detailed_view import AwsMarketplaceCppoPriceTermDetailedView

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoPriceTermDetailedView from a JSON string
aws_marketplace_cppo_price_term_detailed_view_instance = AwsMarketplaceCppoPriceTermDetailedView.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceCppoPriceTermDetailedView.to_json()

# convert the object into a dict
aws_marketplace_cppo_price_term_detailed_view_dict = aws_marketplace_cppo_price_term_detailed_view_instance.to_dict()
# create an instance of AwsMarketplaceCppoPriceTermDetailedView from a dict
aws_marketplace_cppo_price_term_detailed_view_form_dict = aws_marketplace_cppo_price_term_detailed_view.from_dict(aws_marketplace_cppo_price_term_detailed_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


