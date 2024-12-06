# AwsMarketplaceMeteringUsageRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_identifier** | **str** | The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application. | [optional] 
**dimension** | **str** | During the process of registering a product on AWS Marketplace, dimensions are specified. These represent different units of value in your application. | [optional] 
**quantity** | **int** | The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified. | [optional] 
**timestamp** | **datetime** | Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage. | [optional] 
**usage_allocations** | [**List[AwsMarketplaceMeteringUsageAllocation]**](AwsMarketplaceMeteringUsageAllocation.md) | The set of UsageAllocations to submit. The sum of all UsageAllocation quantities must equal the Quantity of the UsageRecord. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_metering_usage_record import AwsMarketplaceMeteringUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceMeteringUsageRecord from a JSON string
aws_marketplace_metering_usage_record_instance = AwsMarketplaceMeteringUsageRecord.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceMeteringUsageRecord.to_json())

# convert the object into a dict
aws_marketplace_metering_usage_record_dict = aws_marketplace_metering_usage_record_instance.to_dict()
# create an instance of AwsMarketplaceMeteringUsageRecord from a dict
aws_marketplace_metering_usage_record_from_dict = AwsMarketplaceMeteringUsageRecord.from_dict(aws_marketplace_metering_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


