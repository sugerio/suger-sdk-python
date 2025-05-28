# SnowflakeMarketplaceBuyer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snowflake_customer_id** | **str** | The customer ID of the buyer in Snowflake Marketplace. | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_buyer import SnowflakeMarketplaceBuyer

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceBuyer from a JSON string
snowflake_marketplace_buyer_instance = SnowflakeMarketplaceBuyer.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceBuyer.to_json())

# convert the object into a dict
snowflake_marketplace_buyer_dict = snowflake_marketplace_buyer_instance.to_dict()
# create an instance of SnowflakeMarketplaceBuyer from a dict
snowflake_marketplace_buyer_from_dict = SnowflakeMarketplaceBuyer.from_dict(snowflake_marketplace_buyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


