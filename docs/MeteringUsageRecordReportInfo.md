# MeteringUsageRecordReportInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alibaba_metering_request** | [**ClientPushMeteringDataRequest**](ClientPushMeteringDataRequest.md) |  | [optional] 
**alibaba_metering_response** | [**ClientPushMeteringDataResponseBody**](ClientPushMeteringDataResponseBody.md) |  | [optional] 
**aws_metering_response** | [**MarketplacemeteringBatchMeterUsageOutput**](MarketplacemeteringBatchMeterUsageOutput.md) |  | [optional] 
**azure_metering_response** | [**GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1BatchUsageEventOkResponse**](GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1BatchUsageEventOkResponse.md) |  | [optional] 
**commit_amount** | **float** | The amount of the commit if applicable. | [optional] 
**credit_amount** | **float** | The amount of the credit if applicable. | [optional] 
**credit_records** | **Dict[str, float]** | The credit usage records in the map of &lt;DimensionKey, Count&gt; | [optional] 
**decimal_parts** | **Dict[str, float]** | The decimal parts of the usage dimension quantity in the map of &lt;DimensionKey, DecimalPart&gt;, before this usage record report. | [optional] 
**dimension_categories** | **Dict[str, str]** | The categories of the usage records in the map of &lt;DimensionKey, Category&gt;. The dimension category is required when reporting usage records to Alibaba Marketplace. It comes from the metering dimension category. | [optional] 
**dimension_unit_list_price** | **Dict[str, float]** | The public list price of each dimension in the map of &lt;DimensionKey, UnitPrice&gt;. | [optional] 
**dimension_unit_price** | **Dict[str, float]** | The unit price of each dimension in the map of &lt;DimensionKey, UnitPrice&gt;. It can be the negotiated price in the private offer or the public list price. | [optional] 
**end_time** | **datetime** | time in UTC when the UsageRecordReport ends | [optional] 
**gcp_metering_response** | [**ServicecontrolReportResponse**](ServicecontrolReportResponse.md) |  | [optional] 
**included_records** | **Dict[str, float]** | The included usage records in the map of &lt;DimensionKey, Count&gt; | [optional] 
**new_decimal_parts** | **Dict[str, float]** | The decimal parts of the usage dimension quantity in the map of &lt;DimensionKey, DecimalPart&gt;, after this usage record report. | [optional] 
**partner** | **str** | The partner where this usage record report is sent to. Such as AWS, AZURE or GCP. | [optional] 
**records_to_report_before_adjustment_at_list_price** | **Dict[str, float]** | The usage records to report before the adjustment by the commit with additional usage at list price, in the map of &lt;DimensionKey, Count&gt;. | [optional] 
**reported_records** | **Dict[str, float]** | The reported usage records in the map of &lt;DimensionKey, Count&gt; | [optional] 
**start_time** | **datetime** | time in UTC when the UsageRecordReport starts | [optional] 
**usage_record_group_ids** | **List[str]** | The IDs of UsageRecordGroups aggregated in this UsageRecordReport. | [optional] 
**used_commit_amount** | **float** | The amount of the used commit before this usage record report if applicable. | [optional] 
**used_commit_amount_increment** | **float** | The amount of the used commit increment in this usage record report if applicable. | [optional] 
**used_credit_amount** | **float** | The amount of the used credit before this usage record report if applicable. | [optional] 
**used_credit_amount_increment** | **float** | The amount of the used credit increment in this usage record report if applicable. | [optional] 

## Example

```python
from openapi_client.models.metering_usage_record_report_info import MeteringUsageRecordReportInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringUsageRecordReportInfo from a JSON string
metering_usage_record_report_info_instance = MeteringUsageRecordReportInfo.from_json(json)
# print the JSON string representation of the object
print MeteringUsageRecordReportInfo.to_json()

# convert the object into a dict
metering_usage_record_report_info_dict = metering_usage_record_report_info_instance.to_dict()
# create an instance of MeteringUsageRecordReportInfo from a dict
metering_usage_record_report_info_form_dict = metering_usage_record_report_info.from_dict(metering_usage_record_report_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


