# AwsMarketplaceMeteringBatchMeterUsageInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product. | [optional] 
**usage_records** | [**List[AwsMarketplaceMeteringUsageRecord]**](AwsMarketplaceMeteringUsageRecord.md) | The set of UsageRecords to submit. BatchMeterUsage accepts up to 25 UsageRecords at a time. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_metering_batch_meter_usage_input import AwsMarketplaceMeteringBatchMeterUsageInput

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceMeteringBatchMeterUsageInput from a JSON string
aws_marketplace_metering_batch_meter_usage_input_instance = AwsMarketplaceMeteringBatchMeterUsageInput.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceMeteringBatchMeterUsageInput.to_json())

# convert the object into a dict
aws_marketplace_metering_batch_meter_usage_input_dict = aws_marketplace_metering_batch_meter_usage_input_instance.to_dict()
# create an instance of AwsMarketplaceMeteringBatchMeterUsageInput from a dict
aws_marketplace_metering_batch_meter_usage_input_from_dict = AwsMarketplaceMeteringBatchMeterUsageInput.from_dict(aws_marketplace_metering_batch_meter_usage_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


