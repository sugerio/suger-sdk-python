# SnowflakeMarketplaceTrialDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**trial_time_limit** | **float** |  | [optional] 
**trial_type** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_trial_details import SnowflakeMarketplaceTrialDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceTrialDetails from a JSON string
snowflake_marketplace_trial_details_instance = SnowflakeMarketplaceTrialDetails.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceTrialDetails.to_json())

# convert the object into a dict
snowflake_marketplace_trial_details_dict = snowflake_marketplace_trial_details_instance.to_dict()
# create an instance of SnowflakeMarketplaceTrialDetails from a dict
snowflake_marketplace_trial_details_from_dict = SnowflakeMarketplaceTrialDetails.from_dict(snowflake_marketplace_trial_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


