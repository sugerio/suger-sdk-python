# MeteringUsageRecordGroupMetaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_validation** | **bool** | If it is true, the validation of the usage record group is skipped. | [optional] 
**billable_records** | [**List[MeteringUsageRecord]**](MeteringUsageRecord.md) | for usage metering API v2 | [optional] 
**lago_amount** | **float** | The lago amount (in dollars) of the customer. This field keeps the largest of the monthly amount. So it can only be updated when the invoice month increases. | [optional] 
**lago_subscription_id** | **str** | The lago subscription ID of the customer. | [optional] 
**lago_usage_start_time** | **datetime** | The lago usage start time of the customer usage. | [optional] 
**metronome_daily_cost_amount** | **float** | The metronome daily cost amount (in dollars) of the customer. | [optional] 
**metronome_invoice_id** | **str** | The metronome invoice ID of the customer. | [optional] 
**metronome_monthly_invoice_amount** | **float** | The metronome monthly invoice amount (in dollars) of the customer. This field keeps the largest amount of the invoice month. So it can only be updated when the invoice month increases. | [optional] 
**metronome_monthly_invoice_amount_adjusted** | **float** | The metronome monthly invoice amount (in dollars) of the customer, which is adjusted by the seller. This field is populated only when the invoice amount is decreased by the seller via credit granting. | [optional] 
**origin_records** | **Dict[str, float]** | The original records reported by the customer before convertion. If no dimension mapping is applied, this field is the same as the records field. | [optional] 
**source** | [**UsageRecordGroupSource**](UsageRecordGroupSource.md) | The source of the usage record group. Can be from Suger API or other third party services, such as Metronome. | [optional] 
**stripe_invoice_id** | **str** |  | [optional] 
**stripe_period_end_time** | **datetime** | The stripe period end time of the summary or invoice. UTC time in format \&quot;YYYY-MM-DDTHH:MM:SSZ\&quot;. | [optional] 
**stripe_period_start_time** | **datetime** | The stripe period start time of the summary or invoice. UTC time in format \&quot;YYYY-MM-DDTHH:MM:SSZ\&quot;. | [optional] 
**stripe_subscription_item_id** | **str** |  | [optional] 
**stripe_usage_record_summary_id** | **str** |  | [optional] 
**stripe_usage_record_summary_total_usage** | **int** |  | [optional] 
**timestamp** | **datetime** | The timestamp (UTC)) of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. | [optional] 

## Example

```python
from suger_sdk_python.models.metering_usage_record_group_meta_info import MeteringUsageRecordGroupMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecordGroupMetaInfo from a JSON string
metering_usage_record_group_meta_info_instance = MeteringUsageRecordGroupMetaInfo.from_json(json)
# print the JSON string representation of the object
print(MeteringUsageRecordGroupMetaInfo.to_json())

# convert the object into a dict
metering_usage_record_group_meta_info_dict = metering_usage_record_group_meta_info_instance.to_dict()
# create an instance of MeteringUsageRecordGroupMetaInfo from a dict
metering_usage_record_group_meta_info_from_dict = MeteringUsageRecordGroupMetaInfo.from_dict(metering_usage_record_group_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


