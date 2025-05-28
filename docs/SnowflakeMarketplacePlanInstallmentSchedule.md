# SnowflakeMarketplacePlanInstallmentSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_installment_amount** | **float** |  | [optional] 
**installment_duration** | **float** |  | [optional] 
**overridden_installments** | [**List[SnowflakeMarketplacePlanInstallment]**](SnowflakeMarketplacePlanInstallment.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_plan_installment_schedule import SnowflakeMarketplacePlanInstallmentSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplacePlanInstallmentSchedule from a JSON string
snowflake_marketplace_plan_installment_schedule_instance = SnowflakeMarketplacePlanInstallmentSchedule.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplacePlanInstallmentSchedule.to_json())

# convert the object into a dict
snowflake_marketplace_plan_installment_schedule_dict = snowflake_marketplace_plan_installment_schedule_instance.to_dict()
# create an instance of SnowflakeMarketplacePlanInstallmentSchedule from a dict
snowflake_marketplace_plan_installment_schedule_from_dict = SnowflakeMarketplacePlanInstallmentSchedule.from_dict(snowflake_marketplace_plan_installment_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


