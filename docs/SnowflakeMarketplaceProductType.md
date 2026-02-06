# SnowflakeMarketplaceProductType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_addon** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_product_type import SnowflakeMarketplaceProductType

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceProductType from a JSON string
snowflake_marketplace_product_type_instance = SnowflakeMarketplaceProductType.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceProductType.to_json())

# convert the object into a dict
snowflake_marketplace_product_type_dict = snowflake_marketplace_product_type_instance.to_dict()
# create an instance of SnowflakeMarketplaceProductType from a dict
snowflake_marketplace_product_type_from_dict = SnowflakeMarketplaceProductType.from_dict(snowflake_marketplace_product_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


