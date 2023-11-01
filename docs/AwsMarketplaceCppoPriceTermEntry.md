# AwsMarketplaceCppoPriceTermEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumption_unit_column_names** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** | the dimension display name | [optional] 
**is_custom_dimension** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**name** | **str** | The dimension Key | [optional] 
**price_per_consumption_unit** | **Dict[str, str]** | Key: the unit in ConsumptionUnitColumnName, Value: the unit price | [optional] 
**pricing_dimension** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_cppo_price_term_entry import AwsMarketplaceCppoPriceTermEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoPriceTermEntry from a JSON string
aws_marketplace_cppo_price_term_entry_instance = AwsMarketplaceCppoPriceTermEntry.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceCppoPriceTermEntry.to_json()

# convert the object into a dict
aws_marketplace_cppo_price_term_entry_dict = aws_marketplace_cppo_price_term_entry_instance.to_dict()
# create an instance of AwsMarketplaceCppoPriceTermEntry from a dict
aws_marketplace_cppo_price_term_entry_form_dict = aws_marketplace_cppo_price_term_entry.from_dict(aws_marketplace_cppo_price_term_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


