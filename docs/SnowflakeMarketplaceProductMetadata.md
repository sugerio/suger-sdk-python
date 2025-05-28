# SnowflakeMarketplaceProductMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**are_terms_provided_offline** | **bool** |  | [optional] 
**business_needs** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**has_free_sample_data** | **bool** |  | [optional] 
**is_with_standard_terms** | **bool** |  | [optional] 
**paid_attributes** | **object** |  | [optional] 
**share** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**usage** | **object** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_product_metadata import SnowflakeMarketplaceProductMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceProductMetadata from a JSON string
snowflake_marketplace_product_metadata_instance = SnowflakeMarketplaceProductMetadata.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceProductMetadata.to_json())

# convert the object into a dict
snowflake_marketplace_product_metadata_dict = snowflake_marketplace_product_metadata_instance.to_dict()
# create an instance of SnowflakeMarketplaceProductMetadata from a dict
snowflake_marketplace_product_metadata_from_dict = SnowflakeMarketplaceProductMetadata.from_dict(snowflake_marketplace_product_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


