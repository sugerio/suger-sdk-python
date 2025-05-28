# SnowflakeMarketplacePlanInstallment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_amount** | **float** |  | [optional] 
**installment_number** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_plan_installment import SnowflakeMarketplacePlanInstallment

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplacePlanInstallment from a JSON string
snowflake_marketplace_plan_installment_instance = SnowflakeMarketplacePlanInstallment.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplacePlanInstallment.to_json())

# convert the object into a dict
snowflake_marketplace_plan_installment_dict = snowflake_marketplace_plan_installment_instance.to_dict()
# create an instance of SnowflakeMarketplacePlanInstallment from a dict
snowflake_marketplace_plan_installment_from_dict = SnowflakeMarketplacePlanInstallment.from_dict(snowflake_marketplace_plan_installment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


