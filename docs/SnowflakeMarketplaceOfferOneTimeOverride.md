# SnowflakeMarketplaceOfferOneTimeOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **float** | This is the total contract value for the one time offer. | [optional] 
**billing_duration_months** | **int** | This is the billing duration months for the one time offer. | [optional] 
**currency** | **str** | Must be USD | [optional] 
**pricing_model** | **str** | Must be FLAT_FEE for one time offer. | [optional] 
**version** | **str** | Must be V2 | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_offer_one_time_override import SnowflakeMarketplaceOfferOneTimeOverride

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceOfferOneTimeOverride from a JSON string
snowflake_marketplace_offer_one_time_override_instance = SnowflakeMarketplaceOfferOneTimeOverride.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceOfferOneTimeOverride.to_json())

# convert the object into a dict
snowflake_marketplace_offer_one_time_override_dict = snowflake_marketplace_offer_one_time_override_instance.to_dict()
# create an instance of SnowflakeMarketplaceOfferOneTimeOverride from a dict
snowflake_marketplace_offer_one_time_override_from_dict = SnowflakeMarketplaceOfferOneTimeOverride.from_dict(snowflake_marketplace_offer_one_time_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


